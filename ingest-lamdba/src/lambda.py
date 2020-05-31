import os
import requests
from string import Template
import json
import boto3
import uuid
import shutil
import sys
from PIL import Image
from skimage import feature
from skimage.filters import gaussian
from fil_finder import FilFinder2D
from astropy import units as u
import numpy as np
import networkx as nx

# https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5000/VNP46A1/2020/150.json
baseUrl = "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5000/VNP46A1/$year/$day"
translate_command = "gdal_translate -a_nodata 'nan' 'HDF5:$temp_file_name://HDFEOS/GRIDS/VNP_Grid_DNB/Data_Fields/DNB_At_Sensor_Radiance_500m' $jpg_name"
s3 = boto3.client('s3')
db = boto3.client('dynamodb', region_name='eu-central-1')
USERAGENT = 'tis/download.py_1.0--' + sys.version.replace('\n','').replace('\r','')

def handler(event):
  # Search for valid file names
  url = Template(baseUrl).safe_substitute(event)
  response = requests.get(url + '.json')

  response_body = response.json()

  found_file_descriptors = list(filter(
    lambda descriptor: ('name' in descriptor) & (event['hv_coords'] in descriptor['name']),
    response_body
  ))
  
  requested_file_name = found_file_descriptors[0]['name']
  
  # Prepare to download h5 file
  token = os.environ['LAADS_TOKEN']
  headers = {
    'user-agent' : USERAGENT,
    'Authorization' : 'Bearer ' + token
  }
  file_id = str(uuid.uuid4())
  temp_file_name = 'temp' + file_id + '.h5'

  # Download h5 file
  with requests.get(url + '/' + requested_file_name, stream = True, headers = headers) as file_response:
    file_response.raise_for_status()
    file_response.raw.decode_content = True
    with open(temp_file_name, 'wb') as temp_file:
      shutil.copyfileobj(file_response.raw, temp_file)

  # Prepare to translate h5 -> jpg
  jpg_name = requested_file_name + '.jpg'
  full_translate_command = Template(translate_command).safe_substitute(dict(
    temp_file_name=temp_file_name,
    jpg_name=jpg_name
  ))
  print(full_translate_command)

  # Translate h5 -> jpg
  os.system(full_translate_command)

  # Load image into numpy array, then preprocess with blur and edge detection
  img = np.asarray(Image.open(jpg_name)) / 255
  edges = feature.canny(img, sigma=1).astype(np.float64)
  edges = gaussian(edges, sigma=3)
  edges = edges.astype(np.float64)

  # Load the edge detected image into a filament finder object
  fil = FilFinder2D(edges)

  # Preprocess the image by flattening to cap outliers and mask the image so that
  # only the most significant structures are analyzed
  fil.preprocess_image(flatten_percent=95)
  fil.create_mask(
    adapt_thresh=10.0*u.pix,
    smooth_size=1.0*u.pix,
    size_thresh=500.0*u.pix**2,
    fill_hole_size=1.0*u.pix**2
  )

  # Generate a rough skeleton overlayed on the image
  fil.medskel()

  # Analyze the skeleton to generate a fine-grained graph and networkx graph
  fil.analyze_skeletons(skel_thresh=1.0*u.pix)

  skeleton_image_file_name = 'skeleton' + jpg_name
  Image.fromarray(fil.skeleton * 255).convert('L').save(skeleton_image_file_name)

  # Calculate the total clustering by summing the average clustering of each filament
  total_clustering = 0.0
  for filament in fil.filaments:
    total_clustering += (nx.average_clustering(filament.graph))

  # Upload jpg to S3 bucket
  s3.upload_file(
    jpg_name, 'space-apps-imagery', jpg_name,
    ExtraArgs={'ACL':'public-read'}
  )
  s3.upload_file(
    skeleton_image_file_name, 'space-apps-imagery', skeleton_image_file_name,
    ExtraArgs={'ACL':'public-read'}
  )
  
  # Upload record to dynamodb
  db.put_item(
    TableName = 'space-apps-imagery',
    Item = {
      'label': { 'S': event['label'] },
      'original_image': { 'S': jpg_name },
      'skeleton_image': { 'S': skeleton_image_file_name },
      'total_clustering': { 'N': str(total_clustering) }
    }
  )

  # Clean up
  os.remove(temp_file_name)
  os.remove(skeleton_image_file_name)
  os.remove(jpg_name)
  os.remove(jpg_name + '.aux.xml')


handler(dict(
  label="china_test",
  year="2020",
  day="148",
  hv_coords="h29v06"
))
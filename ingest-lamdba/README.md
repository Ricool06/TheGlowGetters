# THIS IS NOT ACTUALLY A LAMBDA
We tried to reduce the package size to fit in AWS lambda, but even using lambda layers, compression, etc we could not.
We are still able to ingest data by calling the script locally.

To begin developing:
* open VSCode
* install the VSCode Remote: Containers extension
* open this folder in the dev container using the .devcontainer/devcontainer.json file
* now run `pip install -r requirements.txt`
* set the `LAADS_TOKEN` environment variable to your App Token from the LAADS website

#!/usr/bin/env bash

set -euo pipefail

rm -rf ./build ./layer

# build lambda layer

mkdir ./layer
cd ./layer
cp ../requirements.txt ./
CFLAGS="-Os -g0 -Wl,--strip-all" pip install -r requirements.txt --no-cache-dir --compile -t ./lib/python3.7/site-packages/
find . -name "*.py" -type f -delete
find . -name "tests" -type d -delete
rm -rf ./lib/python3.7/site-packages/scipy ./lib/python3.7/site-packages/numpy
zip -r9 ../layer.zip .

# build lambda
cd ../src
zip -r9 ../function.zip .

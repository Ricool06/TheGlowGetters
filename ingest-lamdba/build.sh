#!/usr/bin/env bash

rm -rf ./build
pip install -r requirements.txt -t ./build
cd ./build
zip -r9 ../function.zip .

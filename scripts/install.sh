#!/bin/bash
# Installation script for linux/osx
# TODO: check correct version of python
if command -v git &> /dev/null; then
    python -m pip install git+https://github.com/GuptaAyush19/pyviva.git
    exit 1
fi

SOURCE=https://github.com/GuptaAyush19/pyviva/archive/master.zip
BASE_DIR=~/Downloads/pyviva.zip

echo -e "\n git is not already installed, instead downloading the project zip at $BASE_DIR \n"

# download the project zip file and save it in $BASE_DIR
wget $SOURCE -O $BASE_DIR

python -m pip install $BASE_DIR -q

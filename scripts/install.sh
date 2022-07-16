#!/bin/bash
if ! command -v git &> /dev/null; then
    BASE_DIR=~/Downloads/pyviva.zip
    echo -e "\n git is not already installed, instead downloading the project zip at $BASE_DIR \n"
    wget https://github.com/GuptaAyush19/pyviva/archive/master.zip -O $BASE_DIR
    python -m pip install $BASE_DIR
else
    python -m pip install git+https://github.com/GuptaAyush19/pyviva.git
fi

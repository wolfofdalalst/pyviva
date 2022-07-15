# pyviva: tui based quiz app 
pyviva is a quiz app written in python and uses [textual](https://github.com/Textualize/textual) as frontend. This project is os independent and can be seamlessly installed using [poetry](https://python-poetry.org/docs/). \
It requires python 3.7+ to run.


## Project setup
Install using pip or directly from source
```
pip install git+https://github.com/GuptaAyush19/pyviva.git
```
Users can also use [poetry](https://python-poetry.org/docs/) to install this repository (recommended for developers looking to contribute)
```
pip install --user poetry
git clone https://github.com/GuptaAyush19/pyviva.git && cd ./pyviva
python -m poetry install
```

## Basic usage
After the installation process is complete, run this command to start using the quiz app
```
python -m pyviva
```

## Run unittests
This package uses python's in-built unittest module for unittesting
```
python -m unittest discover -v
```

## TODO
- Frontend implementation
- Include more questions in csv file
- Installation script
- Automated testing on github

## License
This repository falls under [GPL-3.0 License](https://raw.githubusercontent.com/GuptaAyush19/pyviva/master/LICENSE)
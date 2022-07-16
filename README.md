# pyviva: tui based quiz app 
pyviva is a quiz app written in python and uses [textual](https://github.com/Textualize/textual) as frontend. This project is os independent and can be seamlessly installed using [poetry](https://python-poetry.org/docs/). \
It requires python 3.8+ to run. \
_NOTE: The project is still under development, and is still in alpha stage._

## Quick project setup
For users on windows, run the following command in powershell to automatically install this python package on your system. One can also install directly from source using python-pip3 the details of which are given [here](https://github.com/GuptaAyush19/pyviva#download-from-source).
```ps1
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/GuptaAyush19/pyviva/master/scripts/install.ps1).Content | Invoke-Expression
```
And for linux/osx users run this bash command
```bash
wget -O - https://raw.githubusercontent.com/GuptaAyush19/pyviva/master/scripts/install.sh | bash
```
### Start using the quiz app
After the installation process is complete, run this command to start using the quiz app
```
pyviva
# python -m pyviva
```

## Download from source
### Using git and poetry
Developers looking to contribute can install this repository using [poetry](https://python-poetry.org/docs/).
```
pip install --user poetry
git clone https://github.com/GuptaAyush19/pyviva.git && cd ./pyviva
python -m poetry install
```
### Download zip file and use python-pip3
Zip file for the project can be obtained from [here](https://github.com/GuptaAyush19/pyviva/archive/master.zip). Once the zip file has been downloaded, change current directory and run the following command to install using python-pip3
```
pip install ./pyviva-master.zip
```
### Manual testing
This package uses python's in-built unittest module for testing
```
python -m unittest discover -v
```

## TODO
- Frontend implementation
- Include more questions in csv file
- Automated testing on github

## License
This repository falls under [GPL-3.0 License](https://raw.githubusercontent.com/GuptaAyush19/pyviva/master/LICENSE)

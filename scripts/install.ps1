[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$SOURCE = "https://github.com/GuptaAyush19/pyviva/archive/master.zip"
$DESTINATION=  "$HOME\Downloads\pyviva.zip"

Invoke-RestMethod -Uri $source -OutFile $destination

if (Get-Command 'python') {
    # TODO: check for correct version of python
    python -m pip install $DESTINATION
} else {
    Write-Host "this project requires python3.8+ to run, you can download it from https://www.python.org/"
}

# credit to https://stackoverflow.com/users/5640342/chrisb
# https://stackoverflow.com/questions/23070299/get-the-windows-download-folders-path
Function GetDownloadsPath() As String
    GetDownloadsPath = Environ$("USERPROFILE") & "\Downloads"
End Function

$SOURCE = "https://github.com/GuptaAyush19/pyviva/archive/master.zip"
$DESTINATION= GetDownloadsPath() & "\pyviva.zip"

Invoke-RestMethod -Uri $source -OutFile $destination

if (Get-Command 'python') {
    # TODO: check for correct version of python
    python -m pip install $DESTINATION
} else {
    Write-Host "this project requires python3.7+ to run, you can download it from https://www.python.org/"
}
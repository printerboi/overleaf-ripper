# Overleaf Ripper

An open source selenium-based tool to programmaticly download pdfs from an overleaf instance.
The tool uses your personal login to authenticate with overleaf. After the authentication the given project will be accessed and downloaded, if the compilation has finished.

## Setup

In order to work properly the ripper will need some enviroment variables. Plese set the following variables in the enviroment of your system or use an .env file.

`BASEURL`: Base-Url of your overleaf instance. Starting with http(s) and ending without a /

`PROJECTID`: Id of the project to rip the pdf from. Can be found in the url of the project in overleaf.

`EMAIL`: The email used for your overleaf-account

`PASSWORD`: The password used for your overleaf-account

`DOWNLOADPATH`: Absolute path of the folder where the .pdf should be stored
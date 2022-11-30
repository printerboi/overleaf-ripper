from dotenv import load_dotenv
from ripper import Ripper
import os

load_dotenv()

url = os.getenv("BASEURL")
projectId = os.getenv("PROJECTID")
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
downloadPath = os.getenv("DOWNLOADPATH")


JohnThe = Ripper(url, projectId)
JohnThe.ripSel(email, password, downloadPath)
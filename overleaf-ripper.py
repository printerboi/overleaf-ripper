from dotenv import load_dotenv
from auther import Auther
from ripper import Ripper
import os

load_dotenv()

url = os.getenv("BASEURL")
projectId = os.getenv("PROJECTID")
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

A = Auther(url)
cookies = A.login(email, password)

JohnThe = Ripper(url, projectId, cookies)
JohnThe.ripSel()
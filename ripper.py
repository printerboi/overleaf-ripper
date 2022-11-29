import requests
from http.cookiejar import MozillaCookieJar
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

class Ripper:
    url = ""
    project = ""
    cookies = None

    def __init__(self, baseurl, projectId, cookies) -> None:
        self.url = baseurl
        self.project = projectId
        self.cookies = cookies

    def rip(self) -> None:
        print(self.cookies.get_dict())
        html = requests.get("{}/project/{}".format(self.url, self.project), cookies=self.cookies)
        parsed = BeautifulSoup(html.text)
        print(parsed.find('a', attrs={"tooltip": "Download PDF"}))

    def ripSel(self) -> None:
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        driver.add_cookie(self.cookies.get_dict())
        driver.get("{}/project/{}".format(self.url, self.project))
        downloadElement = driver.find_elements(By.cssSelector, "a[tooltip='Download PDF']")
        print(downloadElement)

        driver.quit()
import requests
import os.path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep






class Ripper:
    url = ""
    project = ""
    cookies = None

    def __init__(self, baseurl, projectId) -> None:
        self.url = baseurl
        self.project = projectId


    def ripSel(self, email, password, downloadPath) -> None:
        if(not os.path.isdir("files")):
            os.mkdir("files")

        service = FirefoxService(executable_path=GeckoDriverManager().install())
        profile = webdriver.FirefoxProfile()
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.dir", downloadPath)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")
        driver = webdriver.Firefox(service=service, firefox_profile=profile, options=options)
        driver.get("{}".format(self.url))

        nameInput = driver.find_element(By.NAME, "email")
        nameInput.click()
        nameInput.send_keys(email)

        nameInput = driver.find_element(By.NAME, "password")
        nameInput.click()
        nameInput.send_keys(password)

        loginForm = driver.find_element(By.NAME, "loginForm")
        loginForm.submit()

        sleep(3)
        
        driver.get("{}/project/{}".format(self.url, self.project))
        
        compileLabels = driver.find_elements_by_class_name("btn-recompile-label")
        
        while self.isCompiling(compileLabels):
            sleep(1)


        projectnameContainer = driver.find_element(By.CSS_SELECTOR, '.name');
        projectName = projectnameContainer.text.replace(" ", "_")

        projectLink = driver.find_element(By.CSS_SELECTOR, 'a[tooltip="Download PDF"]'.format(self.project))
        projectLink.click()
        
        filename = "{}.pdf".format(projectName)
        self.handleSaving(filename)

        driver.quit()


    def isCompiling(self, elements) -> bool:
        if(elements[0].is_displayed()):
            return False
        else:
            return True

    def handleSaving(self, filename) -> None:
        while not os.path.exists("files/{}".format(filename)):
            sleep(15)

        if os.path.isfile("files/{}".format(filename)):
            if os.path.isfile("files/{}".format("output.pdf")):
                os.remove("files/{}".format("output.pdf"))
            os.rename("files/{}".format(filename), "files/{}".format("output.pdf"))
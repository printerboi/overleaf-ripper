from twill.commands import *
from http.cookiejar import CookieJar

class Auther:
    url = ""

    def __init__(self, baseurl) -> None:
        self.url = baseurl

    def login(self, email, password) -> CookieJar: 
        go(self.url)
        showforms()

        fv('loginForm', 'email', email)
        fv('loginForm', 'password', password)
        submit()
        code(200)
        return browser.cookies()

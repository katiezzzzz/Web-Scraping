import requests
from bs4 import BeautifulSoup
'''
class WebClass:

    def __init__(self, URL):

        self.URL = URL
        #self.cache = BeautifulSoup(request.content, "html.parser")

    def getText(self):
        page = requests.get(self.URL)
        self.soup = BeautifulSoup(page.text, 'html.parser')
        # Pull all text from the closed-tab sliding_box activo div
        parent = self.soup.find(class_='closed-tab sliding_box activo')

        # Pull text from all instances of <a> tag within closed-tab sliding_box activo div
        link1_items = link1.find_all('span')

        # Create for loop to print out all links
        for link_name in link1_items:
            print(link_name.prettify())

        for link_name in link1_items:
            names = link_name.contents[0]
            links = 'https://www.cnmv.es/' + link_name.get('href')
            print(names)
            print(links)

    def compare(self):
        newrequest = requests.get(self.URL)
        new = BeautifulSoup(newrequest.content,"html.parser")

        if new == self.cache:
            print("No new updates")
        else:


        self.cache = new

CompanyDict = {}
'''
import requests
from bs4 import BeautifulSoup

class CNMV:

    def __init__(self):
        self.URL = 'https://www.cnmv.es/portal/HR/HRAldia.aspx?lang=en'
        soup = BeautifulSoup(requests.get(self.URL).text, 'html.parser')
        self.classes = soup.find_all(class_='container content-primary')

    def keyword(self,keyword):
        for classes in self.classes:
            text = classes.get_text()
            text = text.replace('\n\n', ' ')
            if keyword in text:
                text = text.split('\n')
                for line in text:
                    if keyword in line:
                        print(line)


'''
    def compare(self):
        newrequest = requests.get(self.URL)
        new = BeautifulSoup(newrequest.content,"html.parser")

        if new == self.cache:
            print("No new updates")
        else:


        self.cache = new
'''

Spanish = CNMV()
Spanish.keyword('Warrants')
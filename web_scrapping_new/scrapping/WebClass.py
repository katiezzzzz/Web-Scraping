from bs4 import BeautifulSoup
import requests
import os.path
import pickle

class WebClass:

    def __init__(self,URL, keywords, company, page):
        #cache companypage is unique for each website
        self.company = company
        self.companypage = (company + " " + page)
        self.URL = URL
        self.keywords = keywords

    def initializeCache(self):
        # extract text from the website and convert all to lower case
        if os.path.exists('cache ' + str(self.companypage) + '.p'):
            self.cache = pickle.load(open(('cache ' + str(self.companypage) + '.p'), 'rb'))
        else:
            soup = BeautifulSoup(requests.get(self.URL).text, 'html.parser')
            self.cache = soup.get_text().lower()
            self.cache = self.cache.replace('\n\n', ' ')
            self.cache = self.cache.split('\n')
            # generate initial cache file
            # check if the text file can be re-written
            pickle.dump(self.cache,open(('cache ' + str(self.companypage) + '.p'), 'wb'))

    def generateCache(self):
        self.old_line = []
        old_line = ""
        for line in self.cache:
            for word in self.keywords:
                if word in line:
                    self.old_line.append(line + old_line)
            old_line = line

    def compare(self):
        self.new_line = []
        # compare the previous website to updated version
        newsoup = BeautifulSoup(requests.get(self.URL).text, "html.parser")
        new = newsoup.get_text().lower()
        new = new.replace('\n\n', ' ')
        new = new.split('\n')
        if new == self.cache:
            print("No new updates at " + self.companypage)
        else:
            print("New updates at " + self.companypage)
            new_line = ""
            for line in new:
                for word in self.keywords:
                    if word in line:
                        self.new_line.append(line + new_line)
                new_line = line
        self.cache = new
        pickle.dump(self.cache, open(('cache ' + str(self.companypage) + '.p'), 'wb'))

    def alert(self):
        self.new_line.reverse()
        for line in self.old_line:
            if line in self.new_line:
                self.new_line.remove(line)
        if self.new_line != []:
            self.new_line.reverse()
            self.message = ["New updates at " + self.companypage + ":" + self.URL]
            print(self.URL)
            for line in self.new_line:
                print(line)
                self.message.append(line)

    def createMessage(self):
        if self.new_line != []:
            if self.message == None:
                pass
            else:
                return ''.join(self.message)
'''
create a class with the following functions:
1. initializeCache - extract existing cache files or write new cache file
2, generateCache - generate info inside the class
1. compare - compare the updated website to original text file
3. alert - search for keywords in the compared file and send alerts
then update every 5 min
'''

from bs4 import BeautifulSoup
import requests
import threading
import time
import os.path
import pickle
import smtplib
import csv

# lists of keywords and websites
keywords_spanish = ['santander','amadeus','banco bilbao vizcava','bbva','iberdrola','inditex',
                    'industria de diseno textil','telefonica']
keywords_rest = ['dividend','amount','agm','annual general meeting','ex-dividend','ex-dividend date',
                 'payment date','results']
website_spanish = ['https://www.cnmv.es/portal/HR/HRAldia.aspx?lang=en']
websites_rest = ['https://www.societegenerale.com/en/investors',
                'https://www.societegenerale.com/en/measuring-our-performance/information-and-publications/dividend',
                'https://www.societegenerale.com/en/about-us/governance/annual-general-meeting',
                'https://www.daimler.com/investors/share/dividend/',
                'https://www.daimler.com/investors/events/annual-meetings/',
                'https://www.daimler.com/investors/events/financial-calendar/',
                'https://www.daimler.com/investors/reports-news/',
                'https://www.telekom.com/en/investor-relations',
                'https://www.telekom.com/en/investor-relations/publications/financial-results#571070',
                'https://www.telekom.com/en/investor-relations/publications',
                'https://www.telekom.com/en/investor-relations/share/dividend',
                'https://www.telekom.com/en/investor-relations/service/financial-calendar',
                'https://www.investor.bayer.de/en/reports/annual-reports/overview/',
                'https://www.investor.bayer.de/en/events/calendar/',
                'https://www.investor.bayer.de/en/stock/dividends/',
                'https://invest.bnpparibas.com/en/results',
                'https://invest.bnpparibas.com/en/bnp-paribas-share/dividend',
                'https://invest.bnpparibas.com/en/calendar',
                'https://www.group.intesasanpaolo.com/scriptIsir0/si09/investor_relations/eng_wp_investor_relations.jsp#/investor_relations/eng_wp_investor_relations.jsp',
                'https://www.group.intesasanpaolo.com/scriptIsir0/si09/investor_relations/eng_wp_investor_relations.jsp#/investor_relations/eng_financial_calendar.jsp',
                'https://www.group.intesasanpaolo.com/scriptIsir0/si09/investor_relations/eng_wp_investor_relations.jsp#/investor_relations/eng_bilanci_relazioni.jsp',
                'https://www.group.intesasanpaolo.com/scriptIsir0/si09/investor_relations/eng_wp_investor_relations.jsp#/investor_relations/eng_azioni_dividendi.jsp']

class WebClass:

    def __init__(self,URL, keywords, company, page):
        #cache companypage is unique for each website
        self.company = company
        self.companypage = (company + " " + page)
        self.URL = URL
        self.keywords = keywords

    def initializeCache(self):
        # extract text from the website and convert all to lower case
        if os.path.exists('cache' + str(self.companypage) + '.p'):
            self.cache = pickle.load(open(('cache' + str(self.companypage) + '.p'), 'rb'))
        else:
            soup = BeautifulSoup(requests.get(self.URL).text, 'html.parser')
            self.cache = soup.get_text().lower()
            self.cache = self.cache.replace('\n\n', ' ')
            self.cache = self.cache.split('\n')
            # generate initial cache file
            # check if the text file can be re-written
            pickle.dump(self.cache,open(('cache' + str(self.companypage) + '.p'), 'wb'))

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
            print("No new updates at " + str(self.companypage))
        else:
            print("New updates at " + str(self.companypage))
            new_line = None
            for line in new:
                for word in self.keywords:
                    if word in line:
                        self.new_line.append(line + new_line)
                new_line = line
        self.cache = new
        pickle.dump(self.cache, open(('cache' + str(self.companypage) + '.p'), 'wb'))

    def alert(self):
        self.new_line.reverse()
        for line in self.old_line:
            if line in self.new_line:
                self.new_line.remove(line)
        if self.new_line:
            self.new_line.reverse()
            print(self.URL)
        for line in self.new_line:
            print(line)

    def sendEmail(self):
        mailserver = smtplib.SMTP('smtp.office365.com', 587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.login('Katie.Zeng@mako.com', 'password')
        mailserver.sendmail('Katie.Zeng@mako.com', 'Jane.Jiang@company.com', 'python email')
        mailserver.quit()

# timer
class RepeatEvery(threading.Thread):
    def __init__(self, interval, func, *args, **kwargs):
        threading.Thread.__init__(self)
        self.interval = interval  # seconds between calls
        self.func = func          # function to call
        self.args = args          # optional positional argument(s) for call
        self.kwargs = kwargs      # optional keyword argument(s) for call
        self.runable = True
    def run(self):
        while self.runable:
            self.func(*self.args, **self.kwargs)
            time.sleep(self.interval)
    def stop(self):
        self.runable = False

# initialize
def update():
    if os.path.exists('Directory.csv'):
        with open('Directory.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                company = str(row[0])
                URL = str(row[1])
                page = str(row[2])
                keywords = row[3].split(",")
                scrap = WebClass(URL, keywords, company, page)
                scrap.initializeCache()
                scrap.generateCache()
                scrap.compare()
                scrap.alert()
    else:
        print("Please install manual.")
'''
# function used to update
def update():
    with open('Directory.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            company = str(row[0])
            URL = str(row[1])
            page = str(row[2])
            #keywords = row[3]
            scrap = WebClass(URL, keywords_spanish, company, page)
            scrap.compare()
            scrap.alert()
            scrap.generateCache()
'''

thread = RepeatEvery(300, update)
print("starting")
thread.start()

'''
create a class with the following functions:
1. compare - compare the updated website to original text file
2, generateCache - generate chache files and save them outside the python file
3. alert - search for keywords in the compared file and send alerts
then update every 5 min
'''

from bs4 import BeautifulSoup
import requests
import threading

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

    def __init__(self, URL, keywords):
        #self.Company = Company
        self.URL = URL
        soup = BeautifulSoup(requests.get(self.URL).text, 'html.parser')
        self.cache = soup.get_text().lower()
        self.cache = self.cache.replace('\n\n', ' ')
        self.keywords = keywords

    def generateCache(self):
        self.old_line = []
        for word in self.keywords:
            if word in self.cache:
                self.cacheSplit = self.cache.split('\n')
                for line in self.cacheSplit:
                    if word in line:
                        self.old_line = self.old_line.append(line)

    def compare(self):
        self.new_line = []
        #newrequest = requests.get(self.URL)
        newsoup = BeautifulSoup(requests.get(self.URL).text, "html.parser")
        new = newsoup.get_text().lower()
        new = new.replace('\n\n', ' ')

        if new == self.cache:
            print("No new updates")
        else:
            print("New updates")
            for word in self.keywords:
                if word in new:
                    newSplit = new.split('\n')
                    for line in newSplit:
                        if word in line:
                            self.new_line = self.new_line.append(line)
        self.cache = new

    def alert(self):
        for line in self.new_line:
            if line in self.old_line:
                pass
            else:
                for word in self.keywords:
                    if word in line:
                        print('word')
                        print(line)
                        print(self.URL)


# initialize
example = WebClass("https://www.cnmv.es/portal/HR/HRAldia.aspx?lang=en", keywords_spanish)
example.generateCache()

# use self.compare to update every 5 min
def update():
    threading.Timer(5.0, update).start() # called every minute
    example.compare()
    example.generateCache()

update()
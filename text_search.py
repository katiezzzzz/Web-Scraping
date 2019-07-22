import requests
from bs4 import BeautifulSoup

# Create a BeautifulSoup object
def getText(arg):
    soup = BeautifulSoup(requests.get(arg).text, 'html.parser')
    text = soup.get_text()
    text = text.replace('\n\n',' ')
    return text


def keyword(arg,keyword):
    if keyword in arg:
        arg = arg.split('\n')
        for line in arg:
            if keyword in line:
                print(line)
    else:
        pass
    return

keywords_spanish = ['Santander','Amadeus','Banco Bilbao Vizcaya','BBVA','Iberdrola','Inditex',
                    'Industria de Diseno Textil','Telefonica','SANTANDER','AMADEUS','BANCO BILBAO VIZCAVA',
                    'IBERDROLA','INDITEX','INDUSTRIA DE DISENO TEXTIL','TELEFONICA','santander','amadeus',
                    'banco bilbao vizcava','bbva','iberdrola','inditex','industria de diseno textil',
                    'telefonica']
keywords_rest = ['Dividend','Amount','AGM','Annual General Meeting','Ex-dividend','Ex-dividend Date','Payment Date',
                 'Results','DIVIDEND','AMOUNT','ANNUAL GENERAL MEETING','EX-DIVIDEND','EX-DIVIDEND DATE',
                 'PAYMENT DATE','RESULTS','dividend','amount','agm','annual general meeting','ex-dividend','ex-dividend date',
                 'payment date','results']

for key in keywords_spanish:
    keyword(getText('https://www.cnmv.es/portal/HR/HRAldia.aspx?lang=en'),key)

websites = ['https://www.societegenerale.com/en/investors',
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

for website in websites:
    text = getText(website)
    for key_rest in keywords_rest:
        keyword(text,key_rest)

import requests
from bs4 import BeautifulSoup



# Create a BeautifulSoup object
def getText(arg):
    page = requests.get(arg)
    soup = BeautifulSoup(page.text, 'html.parser')
    text = soup.get_text()
    withoutspace = text.replace('\n\n',' ')
    return withoutspace.strip()


def keyword(arg,keyword):
    if keyword in arg:
        arg = arg.split('\n')
        for line in arg:
            if keyword in line:
                print(line)
    else:
        pass
    return

keyword(getText('https://www.cnmv.es/portal/HR/HRAldia.aspx?lang=en'),'Warrants')
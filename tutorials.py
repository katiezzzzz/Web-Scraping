import requests
from bs4 import BeautifulSoup


# Create a BeautifulSoup object
def getText(arg):
    page = requests.get(arg)
    soup = BeautifulSoup(page.text, 'html.parser')
    print(soup.find_all(class_='div'))

'''
def keyword(arg, keyword):
    if keyword in arg:
        arg = arg.split('\n')
        for line in arg:
            if keyword in line:
                print(line)
    else:
        pass
    return




# withoutspace = text.replace('\n\n',' ')
'''
keyword(getText('https://www.cnmv.es/portal/HR/HRAldia.aspx?lang=en'), 'Warrants')
'''
# Pull all text from the closed-tab sliding_box activo div
link1 = soup.find(class_='closed-tab sliding_box activo')

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

link2 = soup.find(class_='padding-r resumen')

link2_items = link1.find_all('li')

# Create for loop to print out all links
for link2_name in link2_items:
    names2 = link2_name.contents[0]
    names2 = names2.strip()
    print(names2)
'''
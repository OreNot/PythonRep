
from bs4 import BeautifulSoup
from selenium import webdriver

print('')
print('Парсер HTML для Лёни')
print('')

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--disable-extensions')
chrome = webdriver.Chrome("C:/chromedriver.exe")



def parseTitleString(parseString):
    parseString = str(parseString)
    startSym = parseString.rfind('">')
    returnStr = parseString[startSym + 2 : parseString.__len__()]
    endSym = returnStr.find('</a>')
    returnStr = returnStr[0 : endSym].replace(' ', '').replace('\n', '')

    return returnStr

def parseEmailString(parseString):
    parseString = str(parseString)
    startSym = parseString.find('.ru">')
    returnStr = parseString[startSym + 5 : parseString.__len__()]
    endSym = returnStr.find('</a>')
    returnStr = returnStr[0 : endSym]

    return returnStr

i = 0;



for num in range(1, 6) :
    chrome.get('http://mosgorzdrav.ru/ru-RU/citizens/medical.html?medical_type=1&p=' + str(num) + '&per=10#list')


    html = chrome.page_source

    soup = BeautifulSoup(html, 'lxml')
    emails = soup.findAll(attrs={"class": "medical-main"})

    for em in emails:
        i += 1
        print('')
        title = em.find(attrs={"class": "med-title"})

        email = em.find(attrs={"class": "med-email"})

        parseTitleString(title)

        print(i, ' : ')
        print('Title :', parseTitleString(title))
        print('Email :', parseEmailString(email))


chrome.quit()


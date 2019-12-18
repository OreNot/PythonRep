import time
import win32api
import sys  # sys нужен для передачи argv в QApplication

import self as self
from PyQt5 import QtWidgets
import getpass
import design  # Это наш конвертированный файл дизайна

import win32con
from selenium import webdriver

VK_CODE = {'backspace': 0x08,
               'tab': 0x09,
               'clear': 0x0C,
               'enter': 0x0D,
               'shift': 0x10,
               'ctrl': 0x11,
               'alt': 0x12,
               'pause': 0x13,
               'caps_lock': 0x14,
               'esc': 0x1B,
               'spacebar': 0x20,
               'page_up': 0x21,
               'page_down': 0x22,
               'end': 0x23,
               'home': 0x24,
               'left_arrow': 0x25,
               'up_arrow': 0x26,
               'right_arrow': 0x27,
               'down_arrow': 0x28,
               'select': 0x29,
               'print': 0x2A,
               'execute': 0x2B,
               'print_screen': 0x2C,
               'ins': 0x2D,
               'del': 0x2E,
               'help': 0x2F,
               '0': 0x30,
               '1': 0x31,
               '2': 0x32,
               '3': 0x33,
               '4': 0x34,
               '5': 0x35,
               '6': 0x36,
               '7': 0x37,
               '8': 0x38,
               '9': 0x39,
               'a': 0x41,
               'b': 0x42,
               'c': 0x43,
               'd': 0x44,
               'e': 0x45,
               'f': 0x46,
               'g': 0x47,
               'h': 0x48,
               'i': 0x49,
               'j': 0x4A,
               'k': 0x4B,
               'l': 0x4C,
               'm': 0x4D,
               'n': 0x4E,
               'o': 0x4F,
               'p': 0x50,
               'q': 0x51,
               'r': 0x52,
               's': 0x53,
               't': 0x54,
               'u': 0x55,
               'v': 0x56,
               'w': 0x57,
               'x': 0x58,
               'y': 0x59,
               'z': 0x5A,
               'numpad_0': 0x60,
               'numpad_1': 0x61,
               'numpad_2': 0x62,
               'numpad_3': 0x63,
               'numpad_4': 0x64,
               'numpad_5': 0x65,
               'numpad_6': 0x66,
               'numpad_7': 0x67,
               'numpad_8': 0x68,
               'numpad_9': 0x69,
               'multiply_key': 0x6A,
               'add_key': 0x6B,
               'separator_key': 0x6C,
               'subtract_key': 0x6D,
               'decimal_key': 0x6E,
               'divide_key': 0x6F,
               'F1': 0x70,
               'F2': 0x71,
               'F3': 0x72,
               'F4': 0x73,
               'F5': 0x74,
               'F6': 0x75,
               'F7': 0x76,
               'F8': 0x77,
               'F9': 0x78,
               'F10': 0x79,
               'F11': 0x7A,
               'F12': 0x7B,
               'F13': 0x7C,
               'F14': 0x7D,
               'F15': 0x7E,
               'F16': 0x7F,
               'F17': 0x80,
               'F18': 0x81,
               'F19': 0x82,
               'F20': 0x83,
               'F21': 0x84,
               'F22': 0x85,
               'F23': 0x86,
               'F24': 0x87,
               'num_lock': 0x90,
               'scroll_lock': 0x91,
               'left_shift': 0xA0,
               'right_shift ': 0xA1,
               'left_control': 0xA2,
               'right_control': 0xA3,
               'left_menu': 0xA4,
               'right_menu': 0xA5,
               'browser_back': 0xA6,
               'browser_forward': 0xA7,
               'browser_refresh': 0xA8,
               'browser_stop': 0xA9,
               'browser_search': 0xAA,
               'browser_favorites': 0xAB,
               'browser_start_and_home': 0xAC,
               'volume_mute': 0xAD,
               'volume_Down': 0xAE,
               'volume_up': 0xAF,
               'next_track': 0xB0,
               'previous_track': 0xB1,
               'stop_media': 0xB2,
               'play/pause_media': 0xB3,
               'start_mail': 0xB4,
               'select_media': 0xB5,
               'start_application_1': 0xB6,
               'start_application_2': 0xB7,
               'attn_key': 0xF6,
               'crsel_key': 0xF7,
               'exsel_key': 0xF8,
               'play_key': 0xFA,
               'zoom_key': 0xFB,
               'clear_key': 0xFE,
               '+': 0xBB,
               ',': 0xBC,
               '-': 0xBD,
               '.': 0xBE,
               '/': 0xBF,
               '`': 0xC0,
               ';': 0xBA,
               '[': 0xDB,
               '\\': 0xDC,
               ']': 0xDD,
               "'": 0xDE,
               '`': 0xC0}


def press(*args):
    for i in args:
        win32api.keybd_event(VK_CODE[i], 0, 0, 0)
        time.sleep(.05)
        win32api.keybd_event(VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP, 0)



class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.btnBrowse.clicked.connect(self.mainFunc)

    def mainFunc(self):

            # print(hex(win32api.GetKeyboardLayout()))
            print("Login: ")
            loginName = design.Ui_MainWindow.countEdit.text
            print(loginName)
            # loginName = input();
            passwOfLogin = design.Ui_MainWindow.passEdit.text()
            # passwOfLogin = getpass.getpass("Pass: ")
            print(passwOfLogin)
            # tabcount = 32
            print("Количество обращений: ")
            # count = int(input());
            count = design.Ui_MainWindow.countEdit.text()
            print(count)
            '''
            if loginName.lower() == "ASReutova".lower():
                tabcount = 33
            else:
                tabcount = 32
            '''
            chromeOptions = webdriver.ChromeOptions()
            chromeOptions.add_argument('--disable-extensions')
            chrome = webdriver.Chrome("C:/chromedriver.exe")
            chrome.maximize_window();
            chrome.get('https://support.rosatom.ru/sm/index.do')
            html = chrome.page_source
            login = chrome.find_element_by_id("username")
            login.click()
            login.send_keys("gk\\" + loginName)
            password = chrome.find_element_by_id("password")
            password.click()
            password.send_keys(passwOfLogin)
            submit = chrome.find_element_by_id("SubmitCreds")
            submit.click()
            time.sleep(40)
            '''
            for num in range(tabcount):
                win32api.keybd_event(win32con.VK_TAB, 0, 0, 0)
                time.sleep(1)
            press('f', 'd', 'n', 'j')
            time.sleep(1)
            win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
            time.sleep(5)
            '''
            time.sleep(20)
            win32api.keybd_event(win32con.VK_SPACE, 0, 0, 0)
            time.sleep(5)
            win32api.keybd_event(win32con.VK_TAB, 0, 0, 0)
            time.sleep(5)
            for num in range(count):
                win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
                time.sleep(20)
                win32api.SetCursorPos((609, 215))
                time.sleep(1)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 609, 215, 0, 0)
                time.sleep(1)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 609, 215, 0, 0)
                time.sleep(25)
                for number in range(9):
                    win32api.keybd_event(win32con.VK_TAB, 0, 0, 0)
                    time.sleep(1)
                press('3', '0')
                time.sleep(1)
                win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
                time.sleep(2)
                # win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
                time.sleep(2)
                for number in range(4):
                    win32api.keybd_event(win32con.VK_TAB, 0, 0, 0)
                    time.sleep(1)
                press('c', 't', 'h', 'n', 'b', 'a', 'b', 'r', 'f', 'n', 'spacebar', 'd', 's', 'g', 'e', 'o', 't', 'y',
                      '/')
                for number in range(2):
                    win32api.keybd_event(win32con.VK_TAB, 0, 0, 0)
                    time.sleep(1)
                press('h', 't', 'i', 't', 'y', 'j')
                time.sleep(1)
                win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
                win32api.SetCursorPos((733, 215))
                time.sleep(3)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 733, 215, 0, 0)
                time.sleep(1)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 733, 215, 0, 0)
                time.sleep(30)
                win32api.SetCursorPos((382, 215))
                time.sleep(3)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 382, 215, 0, 0)
                time.sleep(1)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 382, 215, 0, 0)
                time.sleep(15)
            time.sleep(1020)
            chrome.quit()

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
'''
SERVER = "Core-s-exh01.gk.rosatom.local"
FROM = "aamartynyuk@greenatom.ru"
TO = ["listOfEmails"] # must be a list

SUBJECT = "Subject"
TEXT = "Your Text"

# Prepare actual message
message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail

server = smtplib.SMTP(SERVER)
server.sendmail(FROM, TO, message)
server.quit()
'''





'''
    print('Номер телефона (без +7): ', end='')
    phoneNum = input();
    phoneNumber = chrome.find_element_by_css_selector("#phone")
    phoneNumber.click()
    phoneNumber.send_keys(phoneNum)
    submit = chrome.find_element_by_css_selector(".login-form__button")
    submit.click()

    print('Код sms: ', end='')
    sms_text = input();
    sms = chrome.find_element_by_css_selector("#sms")
    sms.click()
    sms.send_keys(sms_text)

    time.sleep(30)

    generatedHtml = chrome.page_source
    chrome.quit()
    return generatedHtml

def parseString(parseString):
    parseString = str(parseString)
    startSym = parseString.find('>')
    endSym = parseString.rfind('<')
    returnStr = parseString[startSym + 1 : endSym]
    return returnStr

def get_all_cards(html):
    soup = BeautifulSoup(html, 'lxml')
    cards = soup.findAll(attrs = {"class" : "card-list__item"})

    i = 0;
    for card in cards:
        i += 1
        print('')
        print('Карта № ', i)
        cardType = card.find(attrs = {"class" : "card__type"})
        cardNumber = card.find(attrs = {"class" : "card__number"})
        cardBalance = card.find(attrs = {"class" : "card__balance-count"})

        print('Тип карты : ', parseString(cardType))
        print('Номер карты : ', parseString(cardNumber))
        print('Баланс : ', parseString(cardBalance))

'''
#html = get_html()
#get_all_cards(html)


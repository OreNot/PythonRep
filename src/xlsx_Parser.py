import codecs
import os
import time
import win32gui

import xlrd
import win32api
import win32con
import win32com.client


VK_CODE = {'backspace':0x08,
           'tab':0x09,
           'clear':0x0C,
           'enter':0x0D,
           'shift':0x10,
           'ctrl':0x11,
           'alt':0x12,
           'pause':0x13,
           'caps_lock':0x14,
           'esc':0x1B,
           ' ':0x20,
           'page_up':0x21,
           'page_down':0x22,
           'end':0x23,
           'home':0x24,
           'left_arrow':0x25,
           'up_arrow':0x26,
           'right_arrow':0x27,
           'down_arrow':0x28,
           'select':0x29,
           'print':0x2A,
           'execute':0x2B,
           'print_screen':0x2C,
           'ins':0x2D,
           'del':0x2E,
           'help':0x2F,
           '0':0x30,
           '1':0x31,
           '2':0x32,
           '3':0x33,
           '4':0x34,
           '5':0x35,
           '6':0x36,
           '7':0x37,
           '8':0x38,
           '9':0x39,
           '(':0x39,
           'ф':0x41,
           'a':0x41,
           'и':0x42,
           'с':0x43,
           'в':0x44,
           'у':0x45,
           'а':0x46,
           'п':0x47,
           'р':0x48,
           'ш':0x49,
           'о':0x4A,
           'л':0x4B,
           'д':0x4C,
           'ь':0x4D,
           'т':0x4E,
           'щ':0x4F,
           'з':0x50,
           'й':0x51,
           'к':0x52,
           'ы':0x53,
           'е':0x54,
           'г':0x55,
           'м':0x56,
           'ц':0x57,
           'ч':0x58,
           'н':0x59,
           'я':0x5A,
           'numpad_0':0x60,
           'numpad_1':0x61,
           'numpad_2':0x62,
           'numpad_3':0x63,
           'numpad_4':0x64,
           'numpad_5':0x65,
           'numpad_6':0x66,
           'numpad_7':0x67,
           'numpad_8':0x68,
           'numpad_9':0x69,
           'multiply_key':0x6A,
           'add_key':0x6B,
           'separator_key':0x6C,
           'subtract_key':0x6D,
           'decimal_key':0x6E,
           'divide_key':0x6F,
           'F1':0x70,
           'F2':0x71,
           'F3':0x72,
           'F4':0x73,
           'F5':0x74,
           'F6':0x75,
           'F7':0x76,
           'F8':0x77,
           'F9':0x78,
           'F10':0x79,
           'F11':0x7A,
           'F12':0x7B,
           'F13':0x7C,
           'F14':0x7D,
           'F15':0x7E,
           'F16':0x7F,
           'F17':0x80,
           'F18':0x81,
           'F19':0x82,
           'F20':0x83,
           'F21':0x84,
           'F22':0x85,
           'F23':0x86,
           'F24':0x87,
           'num_lock':0x90,
           'scroll_lock':0x91,
           'left_shift':0xA0,
           'right_shift ':0xA1,
           'left_control':0xA2,
           'right_control':0xA3,
           'left_menu':0xA4,
           'right_menu':0xA5,
           'browser_back':0xA6,
           'browser_forward':0xA7,
           'browser_refresh':0xA8,
           'browser_stop':0xA9,
           'browser_search':0xAA,
           'browser_favorites':0xAB,
           'browser_start_and_home':0xAC,
           'volume_mute':0xAD,
           'volume_Down':0xAE,
           'volume_up':0xAF,
           'next_track':0xB0,
           'previous_track':0xB1,
           'stop_media':0xB2,
           'play/pause_media':0xB3,
           'start_mail':0xB4,
           'select_media':0xB5,
           'start_application_1':0xB6,
           'start_application_2':0xB7,
           'attn_key':0xF6,
           'crsel_key':0xF7,
           'exsel_key':0xF8,
           'play_key':0xFA,
           'zoom_key':0xFB,
           'clear_key':0xFE,
           '+':0xBB,
           ',':0xBC,
           '-':0xBD,
           '.':0xBE,
           '/':0xBF,
           '`':0xC0,
           ';':0xBA,
           '[':0xDB,
           '\\':0xDC,
           ']':0xDD,
           "'":0xDE,
           '`':0xC0,
           'ё':0xC0}

def press(*args):
    '''
    one press, one release.
    accepts as many arguments as you want. e.g. press('left_arrow', 'a','b').
    '''

    for i in args:

        win32api.keybd_event(VK_CODE[i], 0,0,0)
        time.sleep(.05)
        win32api.keybd_event(VK_CODE[i],0 ,win32con.KEYEVENTF_KEYUP ,0)

def openItNow(hwnd, windowText):
        if windowText in win32gui.GetWindowText(hwnd):
            win32gui.SetForegroundWindow(hwnd)
def chLang():
    win32api.keybd_event(VK_CODE['alt'], 0, 0, 0)
    time.sleep(.05)
    win32api.keybd_event(VK_CODE['left_shift'], 0, 0, 0)
    time.sleep(.05)
    win32api.keybd_event(VK_CODE['alt'], 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(.05)
    win32api.keybd_event(VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
def chLangMy():
    win32api.keybd_event(VK_CODE['left_control'], 0, 0, 0)
    time.sleep(.05)
    win32api.keybd_event(VK_CODE['left_shift'], 0, 0, 0)
    time.sleep(.05)
    win32api.keybd_event(VK_CODE['left_control'], 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(.05)
    win32api.keybd_event(VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
def ctrlA():
    win32api.keybd_event(VK_CODE['left_control'], 0, 0, 0)
    time.sleep(.05)
    win32api.keybd_event(VK_CODE['a'], 0, 0, 0)
    time.sleep(.05)
    win32api.keybd_event(VK_CODE['left_control'], 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(.05)
    win32api.keybd_event(VK_CODE['a'], 0, win32con.KEYEVENTF_KEYUP, 0)
def click(x,y):
    # сначала выставляем позицию
    win32api.SetCursorPos((x,y))
    time.sleep(0.2)
    # а потом кликаем (небольшая задержка для большей человечности)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    time.sleep(0.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
directory = 'C:\\pt\\XLS\\Users'
#directory = 'D:\\Users'
files = os.listdir(directory)

contacts = []
contactsW = []
contactsEng = []
users = {}

time.sleep(5)

for file in range (files.__len__()):
    print(files[file])
    fileName = directory + '\\' + files[file]
    f = codecs.open(fileName, "r", "utf_8_sig")
    for line in f:
        if line.__contains__('FN') and not line.__contains__('АП'):
            if line.__contains__('\\'):
                line = line[0: line.find('\\')]
            if line.__contains__('@'):
                line = line[line.find('@') + 1: line.__len__()]
            if line[0: line.find(' ')].__contains__('Гринатом') or line[line.rfind('.'): line.__len__()].__contains__(
                    '11296'):
                continue
            line = line.replace('[', '').replace(']', '').replace('FN:', '')
            if not ("a" in line.lower() or "o" in line.lower() or "q" in line.lower() or "g" in line.lower()) and ("а" in line.lower() or "о" in line.lower() or "в" in line.lower() or "н" in line.lower() or "к" in line.lower()):
                contactsW.append(line)

    userName = files[file][0: files[file].find(' ')]

    for contact in contactsW:
        if contact.__contains__('('):
            contact = contact[0 : contact.find('(')]
        if contact.__contains__(userName[0: userName.find(' ')]):
            continue
        if not contacts.__contains__(contact):
                contacts.append(contact.replace('\n', '').replace('\r',''))




    #userName = files[file][files[file].find('Гринатом ') + 10: files[file].rfind(' ')]
    #userName = files[file][0 : files[file].find('.txt')]




    if userName.__contains__('('):
        userName = userName[0 :  userName.find('(')]

    print(contacts.__len__() + contactsEng.__len__())
    for i in contacts:
        print(i)
    print()
    for i in contactsEng:
        print(i)
    contacts = contacts + contactsEng
    print(contacts.__len__())
    for i in contacts:
        print(i)
    users[userName] = contacts


#win32gui.EnumWindows(openItNow, 'Блокнот')
# нажимать на клавиши будет с помощью shell
shell = win32com.client.Dispatch('WScript.Shell')

# метод SendKeys программно нажимает на клавиши, поэтому далее записана последовательность нажатий
i = 0

for user in users:
    #print ("%s -> %s" % (user, users[user]))

    #for tab in range (3):
     #  win32api.keybd_event(win32con.VK_TAB, 0, 0, 0)
      #  time.sleep(2)

    if i == 0:
        shell.SendKeys("{TAB 3}")
        i += 1
    else:
        shell.SendKeys("{TAB 20}")
        time.sleep(1)
        ctrlA()
        time.sleep(1)
        press('del')

    time.sleep(2)
    shell.SendKeys(user)
#    for i in list(user.lower()):
#        press(i)

    time.sleep(2)
    #win32api.keybd_event(win32con.VK_TAB, 0, 0, 0)
    shell.SendKeys("{TAB}")
    time.sleep(2)
    #press('+')
    shell.SendKeys("{+}")
    #shell.SendKeys("{ }")
    time.sleep(2)
    #win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
    shell.SendKeys("{ENTER}")
    time.sleep(2)

    '''
    for tab in range (6):
        win32api.keybd_event(win32con.VK_TAB, 0, 0, 0)
        time.sleep(2)
    for tab in range (4):
        press('down_arrow')
        time.sleep(2)
    '''
    shell.SendKeys("{TAB 6}")
    time.sleep(2)
    shell.SendKeys("{DOWN 4}")
    time.sleep(2)
    #shell.SendKey("^+{}")
    time.sleep(2)

    click(1037, 661)
    time.sleep(2)
    shell.SendKeys("{DOWN}")
    time.sleep(2)
    shell.SendKeys("{ENTER}")
    time.sleep(2)
    click(543, 248)
    time.sleep(5)
    click(634, 247)
    time.sleep(5)
    shell.SendKeys("{TAB 4}")
    time.sleep(5)
    for contact in contacts:
        if ("a" in contact.lower() or "o" in contact.lower() or "q" in contact.lower() or "g" in contact.lower()) and not ("а" in contact.lower() or "о" in contact.lower() or "в" in contact.lower() or "н" in contact.lower() or "к" in contact.lower()):
            chLang()
        time.sleep(1)
        shell.SendKeys(contact)
        time.sleep(10)
        click(401, 283)
        time.sleep(5)
        shell.SendKeys("{TAB 2}")
        time.sleep(5)
        #shell.SendKey("^{a}")
        ctrlA()
        time.sleep(3)
        #shell.SendKey("{DELETE}")
        press('del')
        if ("a" in contact.lower() or "o" in contact.lower() or "q" in contact.lower() or "g" in contact.lower()) and not ("а" in contact.lower() or "о" in contact.lower() or "в" in contact.lower() or "н" in contact.lower() or "к" in contact.lower()):
            chLang()
            time.sleep(1)

print(users)
print(contacts)
print(contactsEng)
'''
win32api.keybd_event(VK_CODE['left_shift'] + VK_CODE['п'], 0,0,0)
time.sleep(.05)
win32api.keybd_event(VK_CODE['п'], 0,0,0)
time.sleep(.05)
win32api.keybd_event(VK_CODE['п'],0 ,win32con.KEYEVENTF_KEYUP ,0)
time.sleep(.05)
win32api.keybd_event(VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
'''




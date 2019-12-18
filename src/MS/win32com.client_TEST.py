

import win32api, win32con, win32gui
import time, win32com.client



shell = win32com.client.Dispatch("WScript.Shell")
if (str(win32api.GetKeyboardLayout()).__eq__('67699721')):
    print(str(win32api.GetKeyboardLayout()))
    shell.SendKeys("^+")
    time.sleep(1)

time.sleep(3)
shell.SendKeys("F,jytyncrbq geyrn hfpdthyen yf FHV gjkmpjdfntkz? ghjdtltyj j,extybt hf,jnt c Ltkjdjq gjxnjq? ghjbpdtlty ex`n CRPB? ljrevtyns gthtlfys d JRP")
              # ' Абонентский пункт развернут на АРМ пользователя, проведено обучение работе с Деловой почтой, произведен учёт СКЗИ, документы переданы в ОКЗ.')

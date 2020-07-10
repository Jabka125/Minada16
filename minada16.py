import psutil
import platform
from winreg import *
from distutils.util import get_platform
import wmi
import subprocess
import time
import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

language = input('Select Language: (ru, en)\nAuto: en\n')
clear()
avgloadproc = []
for x in range(3):
    avgloadproc.append(psutil.cpu_percent(interval=1))

aReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
aKey = OpenKey(aReg, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0")
name = QueryValueEx(aKey, 'ProcessorNameString')[0]

cmd = "wmic memorychip get speed, partnumber"
returned_output = subprocess.check_output(cmd) 
ram_speed = (returned_output.decode("utf-8")) 

computer = wmi.WMI()
computer_info = computer.Win32_ComputerSystem()[0]
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()
disks_info = computer.Win32_Diskdrive()
os_name = os_info.Name.encode('utf-8').split(b'|')[0]
os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) / (1024**2)

Video_cards = "\n".join(["Graphics Card: " + gpu_info.Name for gpu_info in computer.Win32_VideoController()])
Disks = "\n".join(["Disk: " + disks_info.Model + "\n\tSize: " + str(round(int(disks_info.Size) / (1024**3))) + ' GB' for disks_info in computer.Win32_Diskdrive()])

if language.lower() == 'en':
    Video_cards = "\n".join(["Graphics Card: " + gpu_info.Name for gpu_info in computer.Win32_VideoController()])
    Disks = "\n".join(["Disk: " + disks_info.Model + "\n\tSize: " + str(round(int(disks_info.Size) / (1024**3))) + ' GB' for disks_info in computer.Win32_Diskdrive()])
    print('\t\t\tDeveloped by Jabka125\n\t\t\tVersion: 0.2\n')
    print(
f'''Processor: {name}
    Frequence: {round(psutil.cpu_freq().current)} Ghz
    Cores: {psutil.cpu_count(logical=False)}
    Threads: {psutil.cpu_count()} 
    Avg Loading Processor: {round(sorted(avgloadproc)[len(avgloadproc) // 2])} %
Motherboard: {computer.Win32_BaseBoard()[0].Manufacturer} {computer.Win32_BaseBoard()[0].Product}
RAM: {ram_speed.split()[2]}
    Size of RAM: {round(system_ram)} GB
    Speed of RAM: {ram_speed.split()[3]} MHz
OS: {platform.system()} {platform.win32_ver()[0]}
{Disks}
{Video_cards}''')
    input('\nPush Enter button...')


elif language.lower() == 'ru':
    Video_cards = "\n".join(["Видеокарта: " + gpu_info.Name for gpu_info in computer.Win32_VideoController()])
    Disks = "\n".join(["Диск: " + disks_info.Model + "\n\tРазмер: " + str(round(int(disks_info.Size) / (1024**3))) + ' GB' for disks_info in computer.Win32_Diskdrive()])
    print('\t\t\tРазработан Jabka125\n\t\t\tВерсия: 0.2\n')
    print(
f'''Процессор: {name}
    Частота: {round(psutil.cpu_freq().current)} Ghz
    Ядра: {psutil.cpu_count(logical=False)}
    Потоки: {psutil.cpu_count()} 
    Средняя загрузка процессора: {round(sorted(avgloadproc)[len(avgloadproc) // 2])} %
Материнская плата: {computer.Win32_BaseBoard()[0].Manufacturer} {computer.Win32_BaseBoard()[0].Product}
ОЗУ: {ram_speed.split()[2]}
    Размер ОЗУ: {round(system_ram)} GB
    Частота ОЗУ: {ram_speed.split()[3]} MHz
Система: {platform.system()} {platform.win32_ver()[0]}
{Disks}
{Video_cards}''')
    input('\nНажмите Enter...')
else:
    print('\t\t\tDeveloped by Jabka125\n\t\t\tVersion: 0.2\n')
    print(
f'''Processor: {name}
    Frequence: {round(psutil.cpu_freq().current)} Ghz
    Cores: {psutil.cpu_count(logical=False)}
    Threads: {psutil.cpu_count()} 
    Avg Loading Processor: {round(sorted(avgloadproc)[len(avgloadproc) // 2])} %
Motherboard: {computer.Win32_BaseBoard()[0].Manufacturer} {computer.Win32_BaseBoard()[0].Product}
RAM: {ram_speed.split()[2]}
    Size of RAM: {round(system_ram)} GB
    Speed of RAM: {ram_speed.split()[3]} MHz
OS: {platform.system()} {platform.win32_ver()[0]}
{Disks}
{Video_cards}''')
    input('\nPush Enter button...')
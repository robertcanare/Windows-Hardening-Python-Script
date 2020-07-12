# Windows 10 hardening script
# Robert John Canare
# 6/23/20

# Please use the Excel file to follow the sequence of tasks that need to be executed
# To convert it to EXE file, please use this command;
# pyinstaller --onefile --icon="Smile.ico" windows_hardening.py

################################################
# DON'T FUCKING RUN THIS ON ANY FUCKING SERVER #
################################################

import os
import platform
import smtplib
import getpass
import socket
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime


# Verify if it's Windows 10
sysinfo = platform.platform()
win10 = sysinfo[0:10]

# Email sender
email = 'email@gmail.com'
password = 'password'

# Email receiver
to_email = "email@gmail.com"
to_email_1 = "email@gmail.com"

# Get the timestamp
datetime.now(tz=None)
date = datetime.now()

def send_email( status ):
    mail_content = f'''
    As of {date} user {getpass.getuser()} on computer {socket.gethostname()} has {status} executed the Windows Hardening script.
    
    [THIS IS AN AUTOMATED MESSAGE - PLEASE DO NOT REPLY DIRECTLY TO THIS EMAIL]'''

    message = MIMEMultipart()
    message['From'] = email
    message['To'] = to_email
    message['Subject'] = f'Windows 10 script'
    message.attach(MIMEText(mail_content, 'plain'))

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(email, password)
    text = message.as_string()
    session.sendmail(email, to_email, text)
    session.sendmail(email, to_email_1, text)
    session.quit()

if win10 == "Windows-10":

    # Remove shared folder & disable network discovery
    os.system("wmic path Win32_Share delete")

    # Enable Windows Defender real-time protection
    os.system("PowerShell Set-MpPreference -DisableRealtimeMonitoring $false")

    # Enable Windows Defender cloud-delivered protection
    os.system("PowerShell Set-MpPreference -MAPSReporting Advanced")

    # Enable Windows Defender automatic submission
    os.system("powershell Set-MpPreference -SubmitSamplesConsent SendAllSamples")

    # Turn on all firewalls
    os.system("NetSh Advfirewall set allprofiles state on")

    # Disable RDP access
    os.system('reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 1 /f')

    # Force windows update
    os.system("reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update" /v AUOptions /t REG_DWORD /d 0 /f")
    os.system("net start wuauserv")
    os.system("sc config wuauserv start= auto")

    send_email("successfully")


else:
    send_email("Failed to ")


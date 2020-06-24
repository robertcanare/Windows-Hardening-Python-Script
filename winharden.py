# Windows hardening script
# Robert John Canare
# 6/23/20


# Please use the Excell file to follow the sequence of tasks that need to be executed
# To convert it to EXE file, please use this command;
# pyinstaller --onefile --icon="Smile.ico" bordogs_windows_hardening.py

################################################
# DON'T FUCKING RUN THIS ON ANY FUCKING SERVER #
################################################

import os
import platform

# Verify if it's Windows 10
sysinfo = platform.platform()
win10 = sysinfo[0:10]

if win10 == "Windows-10":
    print("It's Windows 10")
    # Remove shared folder & disable network discovery
    os.system("wmic path Win32_Share delete")

    # Enable Windows Defender real-time protection
    os.system("PowerShell Set-MpPreference -DisableRealtimeMonitoring $false")

    # Enable Windows Defender cloud-delivered protection
    os.system("PowerShell Set-MpPreference -MAPSReporting Advanced")

    # Enable Windows Defender automatic submission
    os.system("powershell Set-MpPreference -SubmitSamplesConsent SendAllSamples")

    # Turn on firewall
    os.system("NetSh Advfirewall set allprofiles state on")

else:
    print("It's not a Windows 10, Please check the error logs")

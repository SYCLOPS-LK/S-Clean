import shutil, subprocess, os
from os import getenv

prefetch_folder_path = ('C:\\Windows\\Prefetch')
local_temp_folder_path = (getenv('LOCALAPPDATA') + '\\Temp')
windows_temp_folder_path = ('C:\\Windows\\temp')
softwaredistribution_folder_path = ("C:\\Windows\\SoftwareDistribution\\Download")

class OptimizeProcess():

    @staticmethod
    def clean_prefetch_folder():
        for filename in os.listdir(prefetch_folder_path):
            file_path = os.path.join(prefetch_folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except:
                continue

    @staticmethod
    def clean_local_temp_folder():
        for filename in os.listdir(local_temp_folder_path):
                    file_path = os.path.join(local_temp_folder_path, filename)
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                    except:
                        continue

    @staticmethod
    def clean_windows_temp_folder():
        for filename in os.listdir(windows_temp_folder_path):
            file_path = os.path.join(windows_temp_folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except:
                continue

    @staticmethod
    def clean_softwaredistribution_folder():
        for filename in os.listdir(softwaredistribution_folder_path):
            file_path = os.path.join(softwaredistribution_folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except:
                continue

    @staticmethod
    def refuce_system_latency():
        subprocess.check_output('bcdedit /set disabledynamictick yes', shell=True)
        subprocess.check_output('bcdedit /set useplatformtick yes', shell=True)
        subprocess.check_output('Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v "SystemResponsiveness" /t REG_DWORD /d "0" /f', shell=True)

    @staticmethod
    def flush_dns():
        subprocess.check_output('ipconfig /flushdns', shell=True)
from time import time
from turtle import update
import colorama
from colorama import Fore
colorama.init(autoreset=True)
import os , sys ,time

os.system('clear')
print(Fore.GREEN+'Updating InstaLoader please wait ...')
os.system('rm -rf InstaLoader')
os.system('git clone https://github.com/imraj569/InstaLoader.git')
os.system('clear')
print(Fore.GREEN+'InstaLoader updated successfully...')
time.sleep(1)
os.remove(sys.argv[0])


import banner
import requests
import re
import os
import sys
import colorama
from colorama import Fore
colorama.init(autoreset=True)

def get_response(url):
    try:
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"}
        r = requests.get(url,headers=header)
        while r.status_code != 200:
            r = requests.get(url,headers=header)
        return r.text
    except:
        print('somthing went wrong !')

def prepare_urls(matches):
    return list({match.replace("\\u0026", "&") for match in matches})

def l(): 
    url = input(Fore.BLUE+'Enter Instagram post URL: ')
    response = get_response(url)
    
    vid_matches = re.findall('"video_url":"([^"]+)"', response)
    pic_matches = re.findall('"display_url":"([^"]+)"', response)

    vid_urls = prepare_urls(vid_matches)
    pic_urls = prepare_urls(pic_matches)

    if vid_urls:
        print(Fore.CYAN+'\nDetected Videos:\n{0}'.format('\n'.join(vid_urls)))

    if pic_urls:
        print(Fore.LIGHTYELLOW_EX+'\nDetected Pictures:\n{0}'.format('\n'.join(pic_urls)))

    if not (vid_urls or pic_urls):
        print(Fore.RED+'Could not recognize the media in the provided URL.')

def ClearCon():
    try:
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
            os.system(command)
        else:
            os.system('clear')
    except:
        print('somthing want wrong')

def opt():
    print(Fore.LIGHTMAGENTA_EX+'Download all types of instagram posts,reels,videos and story etc. ≧◉◡◉≦')
    print(Fore.LIGHTYELLOW_EX+'''
-----------------------
    [1]change banner
    [2]clear screen
    [3]download post
    [4]Exit
-----------------------''')
    query = input('Enter any no you want: ')
    if '1' in query:
        ClearCon()
        banner.ban()
    elif '2' in query:
        ClearCon()
    elif '3' in query:
        l()
    elif '4' in query:
        ClearCon()
        print(Fore.BLUE+"Thanks for using Insta Loader  (•◡•) /")
        sys.exit()

if __name__ == '__main__':
    banner.ban()
    while True: 
        opt()
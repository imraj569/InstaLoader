from time import sleep
import requests
import re
import os
from tqdm import tqdm
import colorama
from colorama import Fore
colorama.init(autoreset=True)
from banner_2 import ban, bye
import sys

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
    if 'clear' in url:
        ClearCon()

    elif 'exit' in url or 'bye' in url:
        ClearCon()
        bye()
        sys.exit()

    elif 'banner' in url or 'bn' in url:
        ClearCon()
        ban()
    
    elif 'update' in url:
        ClearCon()
        print(Fore.GREEN+'please wait updating....')
        try:
            os.system('git clone https://github.com/imraj569/InstaLoader.git')
            print(Fore.GREEN+'successfully updated ....')
        except:
            print('''somthing went wrong please update manualy at
             : https://github.com/imraj569/InstaLoader.git ''')

    elif 'help' in url or '-h' in url:
        ClearCon()
        print(Fore.YELLOW+'''
     --------------------------------------------------------------- 
    | [+] for clear your screen type -clear.                        |
    | [+] for Exit type -exit/Exit.                                 |       
    | [+] for change banner type - banner/bn.                       |
    | [+] for help type - help/-h                                   |
    | [+] for Update Instaloader type - update                      |       
    | [+] for download instagram reels,images and more past url.    |
     ---------------------------------------------------------------
        ''')

    elif 'www.instagram.com' in url:
        print(Fore.YELLOW+'Please wait searching url content...')
        response = get_response(url)
        
        vid_matches = re.findall('"video_url":"([^"]+)"', response)
        pic_matches = re.findall('"display_url":"([^"]+)"', response)

        vid_urls = prepare_urls(vid_matches)
        pic_urls = prepare_urls(pic_matches)

        if vid_urls:
            # print(Fore.CYAN+'\nDetected Videos:\n{0}'.format('\n'.join(vid_urls)))
            a = (format('\n'.join(vid_urls)))
            try:
                chunk_size=256
                r=requests.get(url,stream=True)
                with open("reels.mp4","wb") as f:
                    for chunk in tqdm(r.iter_content(chunk_size=chunk_size)):
                        f.write(chunk)
                ClearCon()
                os.system('mv reels.mp4 /sdcard/Download/')       
                print(Fore.GREEN+'Video Downloaded successfully...')

            except:
                print('somthing went wrong please past url in browser and download')

        if pic_urls:
            print(Fore.LIGHTYELLOW_EX+'\nDetected Pictures:\n{0}'.format('\n'.join(pic_urls)))
           
        if not (vid_urls or pic_urls):
            print(Fore.RED+'Could not recognize the media in the provided URL.')

    else:
        print(Fore.RED+"sorry this command can't be Executed please type help for more.")

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

if __name__ == '__main__':
    ClearCon()
    ban()
    while True: 
        l()
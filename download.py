import requests
from tqdm import tqdm
import os
from colorama import Fore
import colorama
colorama.init(autoreset=True)

url = input(Fore.BLUE+'past result url: ')
try:
    chunk_size=256
    r=requests.get(url,stream=True)
    with open("reels.mp4","wb") as f:
        for chunk in tqdm(r.iter_content(chunk_size=chunk_size)):
            f.write(chunk)
        os.system('mv reels.mp4 /sdcard/Download/')    
        print('Video Downloaded successfully...')

except:
    print('somthing went wrong please past url in browser and download')


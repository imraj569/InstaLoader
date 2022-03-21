import requests
import re
import colorama
from colorama import Fore
colorama.init(autoreset=True)

def get_response(url):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"}
    r = requests.get(url,headers=header)
    while r.status_code != 200:
        r = requests.get(url,headers=header)
    return r.text

def prepare_urls(matches):
    return list({match.replace("\\u0026", "&") for match in matches})

print(Fore.CYAN+'''

───────╔╗───╔╗──────────╔╗
──────╔╝╚╗──║║──────────║║
╔╦═╗╔═╩╗╔╬══╣║──╔══╦══╦═╝╠══╦═╗
╠╣╔╗╣══╣║║╔╗║║─╔╣╔╗║╔╗║╔╗║║═╣╔╝
║║║║╠══║╚╣╔╗║╚═╝║╚╝║╔╗║╚╝║║═╣║
╚╩╝╚╩══╩═╩╝╚╩═══╩══╩╝╚╩══╩══╩╝
-----------------------------------------------------------------
                            v1
                            Author:https://github.com/imraj569
-----------------------------------------------------------------
Just past The instagram post link and Download
------------------------------------------------------------------                            
''')

url = input(Fore.BLUE+'Enter Instagram URL: ')
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

  
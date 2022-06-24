import requests
url = input('past result url: ')
try:
    chunk_size=256
    r=requests.get(url,stream=True)
    with open("reels.mp4","wb") as f:
        for chunk in r.iter_content(chunk_size=chunk_size):
            f.write(chunk)
            print('video downloaded successfully...')

except:
    print('somthing went wrong please past url in browser and download')


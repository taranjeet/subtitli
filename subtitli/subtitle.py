import os
import hashlib
import sys
import requests

__version__ = '0.0.1'

BASE_URL = 'http://api.thesubdb.com/?action=download&hash={hash}&language=en'


def get_hash(name):
    '''this hash function receives the name of the file and returns the hash code'''
    readsize = 64 * 1024
    with open(name, 'rb') as f:
        size = os.path.getsize(name)
        data = f.read(readsize)
        f.seek(-readsize, os.SEEK_END)
        data += f.read(readsize)
    return hashlib.md5(data).hexdigest()


def download_subtitle(path):

    filename, extension = os.path.splitext(path)
    headers = {'User-Agent': 'SubDB/1.0 (subtitle-cli/0.1; http://github.com/staranjeet/subtitli)'}
    url = BASE_URL.format(hash=get_hash(path))
    req = requests.get(url, headers=headers)
    if req.status_code == 200:
        with open(filename + '.srt', 'wb') as subtitle_file:
            subtitle_file.write(req.text)
        print("Subtitle successfully saved!")
    elif req.status_code == 404:
        print('Subtitle not found!')


def main():

    if len(sys.argv) == 1:
        print("Subtitle cli requires atleast one parameter")
        sys.exit(1)

    download_subtitle(sys.argv[1])

if __name__ == '__main__':
    main()

import requests
import validators
import os
import re
import configparser

def get_text(url):
    #TODO validate 
    r = requests.post(url)
    if r.status_code == 200:
        return r.text
    else:
        return None

def get_content(url):
    #TODO validate 
    r = requests.post(url)
    if r.status_code == 200:
        return r.content
    else:
        return None

def get_from_config():
    cfg = configparser.ConfigParser()
    cfg.read('config.ini')
    if cfg.sections() != None:
        for sec in cfg.sections():
            print("section: " + sec)
    try:
        print(cfg['crawler']['starturl'])
        return cfg['crawler']['starturl']
    except KeyError:
        print('KeyError')
        return None

def find(url):
    text = get_text(url)
    if text != None:
        founds = re.findall(r'(https?://\S+)', text)
        starturl = get_from_config()
        if starturl != None:
            for found in founds:
                if found.startswith(starturl):
                    filename_raw = found.rsplit('/', 1)[1]
                    filename = filename_raw[:len(filename_raw)-1]
                    dir = found.rsplit('/', 2)[1]
                    id = found.rsplit('/', 3)[1]
                    fullpath = os.path.join(id, dir, filename)
                    fulldir = os.path.join(id, dir)

                    content = get_content(found[:len(found)-1])
                    if content != None:
                        if not os.path.exists(fulldir):
                            print("create dir: " + fulldir)
                            os.makedirs(fulldir)
                        with open(fullpath, 'wb') as f:
                            print('save to file: ' + fullpath)
                            f.write(content)
            print('done...')
        else:
            print("check your config file...")


if __name__ == '__main__':
    url = input("please insert url: \n")
    find(url)


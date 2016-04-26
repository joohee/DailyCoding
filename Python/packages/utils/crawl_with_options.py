import requests
import validators
import os
import re
import configparser
from optparse import OptionParser
import validators

def validate_url(url):
	return validators.url(url)
		
def get_text(url):
	if validate_url(url):
		r = requests.post(url)
    	if r.status_code == 200:
        	return r.text
		else return None
    else:
		print ('url is invalid...')	
        return None

def get_content(url):
	if validate_url(url):
    	r = requests.post(url)
    	if r.status_code == 200:
        	return r.content
    	else:
        	return None
	else:
		print ('url is invalid...')	
		return None

def get_from_config(key):
    cfg = configparser.ConfigParser()
    cfg.read('config.ini')
    if cfg.sections() != None:
        for sec in cfg.sections():
            print("section: " + sec)
    try:
        print(cfg['crawler'][key])
        return cfg['crawler'][key]
    except KeyError:
        print('KeyError')
        return None

def find(url):
    text = get_text(url)
    if text != None:
        founds = re.findall(r'(https?://\S+)', text)
        starturl = get_from_config('starturl')
        if starturl != None:
            for found in founds:
                if found.startswith(starturl):
                    filename_raw = found.rsplit('/', 1)[1]
                    filename = filename_raw[:len(filename_raw)-1]
                    dir = found.rsplit('/', 2)[1]
                    id = found.rsplit('/', 3)[1]
                    parent_dir = found.rsplit('/', 4)[1]

                    fullpath = os.path.join(parent_dir, id, dir, filename)
                    fulldir = os.path.join(parent_dir, id, dir)

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

def save(number, start, end):
    '''입력받은 start num ~ end num까지의 회차에 대해 파일로 저장합니다.

        baseUrl은 ConfigParser를 통해 config.ini 파일에서 읽어옵니다. 
    '''
   baseurl = starturl = get_from_config('baseurl')
   print (baseurl)
   for no in range(start, end):
       url = baseurl.format(number, no)
       print(url)
       find(url)

if __name__ == '__main__':
    parser = OptionParser(usage='usage: %prog [options] arguments')
    parser.add_option('-n', '--number', dest='number', help='foo help')
    parser.add_option('-s', '--start', dest='start_no', default='1', help='foo help')
    parser.add_option('-e', '--end', dest='end_no', default='10', help='foo help')
    (options, args) = parser.parse_args()

    if not options.number:   # if filename is not given
            parser.error('number not given')
    else:
        print('number: ' + options.number)
        save(options.number, int(options.start_no), int(options.end_no))

    #find(url)


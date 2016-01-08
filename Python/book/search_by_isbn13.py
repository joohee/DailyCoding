#!/usr/bin/python

import requests
import json
import configparser

item_keys = {
        'title', 'link', 'cover_s_url', 'cover_l_url', 'description', 'author'
        , 'translator', 'pub_nm', 'pub_date', 'category', 'isbn'
        , 'isbn13', 'sale_yn', 'list_price', 'sale_price', 'status_des'
        , 'barcode', 'ebook_barcode'
        }

def search_from_api(isbn13_no):

    #search_url = 'https://apis.daum.net/search/book'
    #api_key = '980ffe4747d09f1c816073413df6991e'
    #output = 'json'

    search_url = get_from_config('firefriday', 'search_url')
    payload = {}
    payload['apikey'] = get_from_config('firefriday', 'api_key')
    payload['output'] = get_from_config('firefriday', 'output')
    payload['q'] = isbn13_no

    r = requests.get(search_url, payload)
    if r.status_code == 200:
        result = json.loads(r.text)

        totalCount = int(result['channel']['totalCount'])
        if totalCount > 0:
            item = result['channel']['item'][0]
            print (type(item))

            for key in item_keys:
                value = item[key]
                print ("item[", key, "] = ", value)

        else:
            print ('not found...')
    else:
        print ('error: ', r.status_code)

    print ('''''''''''''''''''''''''''''')

def get_from_config(section, key):
    config = configparser.ConfigParser()
    config.read('config.ini')

    if config.sections() != None:
        try:
            value = config[section][key] 
            return value
        except KeyError:
            return None
    else:
        print("config section not found: {}".format(section))
        return None
        

if __name__ == '__main__':
    isbn13_no = input("please valid isbn no: ")
    search_from_api(isbn13_no)
      

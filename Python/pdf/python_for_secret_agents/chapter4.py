
def example1():
    import urllib.request
    import urllib.parse
    import json
    import pprint

    # 1. Build the URL.
    form = {
        "address": "333 waterside drive, norfolk, va, 23510",
            #"address": "경기도 성남시 분당구 삼평동 642",
        "sensor": "false",
        #"key": Provide the API Key here if your're registered
    }
    query = urllib.parse.urlencode(form, safe=",")
    scheme_netloc_path = "https://maps.googleapis.com/maps/api/geocode/json"
    print(scheme_netloc_path+"?"+query)

    # 2. Send the request; get the response
    with urllib.request.urlopen(scheme_netloc_path+"?"+query) as geocode:
        print(geocode.info())
        response = json.loads(geocode.read().decode("UTF-8"))

    # 3. Process the response object.
    print(type(response))
    pprint.pprint(response)

def example2():
    import urllib.request
    import urllib.parse
    import json

    # 1. Build the URL.
    form = {
            "latlng": "36.844305, -76.29112",
            "sensor": "false",
            #"key": Provide the API Key here if you're registered,
    }
    query = urllib.parse.urlencode(form, safe=",")
    scheme_netloc_path = "https://maps.googleapis.com/maps/api/geocode/json"
    print(scheme_netloc_path + "?" + query)

    # 2. Send the request; get the response
    with urllib.request.urlopen(scheme_netloc_path+"?"+query) as geocode:
        print(geocode.info())
        response = json.loads(geocode.read().decode("UTF-8"))

    # 3. Process the response object.
    for alt in response['results']:
        print(alt['types'], alt['formatted_address'])


if __name__ == "__main__":
    #example1()
    example2()


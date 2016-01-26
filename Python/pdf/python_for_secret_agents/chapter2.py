import http.client
import contextlib
import ftplib

def example1():
    path_list = [
        "/wikipedia/commons/7/72/IPhone_Internals.jpg",
        "/wikipedia/en/c/c1/1drachmi_1973.jpg"
    ]
    host = "upload.wikimedia.org"

    with contextlib.closing(http.client.HTTPSConnection(host)) as connection:
        for path in path_list:
            connection.request("GET", path)
            response = connection.getresponse()
            print("Status: ", response.status)
            print("Header: ", response.getheaders())
            _, _, filename = path.rpartition("/")
            print("Writing: ", filename)
            with open (filename, "wb") as image:
                image.write(response.read())


# not working
def example2():
    host = "ftp.ibiblio.org"
    root = "/pub/docs/books/gutenberg/"

    def directory_list(path):
        with ftplib.FTP(host, user="anonymous") as connection:
            print("Welcome: ", connection.getwelcome())
            for name, details in connection.mlsd(path):
                print(name, details['type'], details.get("size"))

    directory_list(root)

# not working
def example3():
    import sys
    import urllib.request
    readme = "ftp://ftp.ibiblio.org/pub/docs/books/gutenberg/README"
    with urllib.request.urlopen(readme) as response:
        sys.stdout.write(response.read().decode("ascii"))

# not working
def example4():
    import urllib.request
    import json
    query_currencies = "http://www.coinbase.com/api/v1/currencies/"
    with urllib.request.urlopen(query_currencies) as document:
        print(document.info().items())
        currencies = json.loads(document.read().decode("utf-8"))
        print(currencies)

def example5():
    import urllib.parse, urllib.request
    import pprint
    import json

    currency = 'EUR'
    scheme_netloc_path = "https://coinbase.com/api/v1/prices/spot_rate"
    form = {"currency": currency}
    query = urllib.parse.urlencode(form) 
    print(query)

    with urllib.request.urlopen(scheme_netloc_path) as document:
        pprint.pprint(document.info().items())
        spot_rate = json.loads(document.read().decode("utf-8"))
        print(spot_rate)

def example6():
    import urllib.parse, urllib.request
    import json
    def get_spot_rate(currency):
        scheme_netloc_path = "https://coinbase.com/api/v1/prices/spot_rate"
        form = {"currency": currency}
        query = urllib.parse.urlencode(form)

        with urllib.request.urlopen(scheme_netloc_path+"?"+query) as document:
            spot_rate = json.loads(document.read().decode("utf-8"))

        print(type(spot_rate))
        return spot_rate

    rates = [ get_spot_rate("USD"), get_spot_rate("GBP"), get_spot_rate("EUR") ]
    with open("rate.json", "w") as save:
        json.dump(rates, save)
    
def example7():
    year_cheese = [(2000, 29.87), (2001, 30.12), (2002, 30.6), (2003, 30.66), 
                    (2004, 31.33), (2005, 32.62), (2006, 32.73), (2007, 33.5),
                    (2008, 32.84), (2009, 33.02), (2010, 32.92), (2011, 33.27),
                    (2012, 33.51)]

    print(max(year_cheese, key=lambda x: x[1]))
    print(min(year_cheese, key=lambda x: x[1]))

def example8():
    year_cheese = [(2000, 29.87), (2001, 30.12), (2002, 30.6), (2003, 30.66), 
                    (2004, 31.33), (2005, 32.62), (2006, 32.73), (2007, 33.5),
                    (2008, 32.84), (2009, 33.02), (2010, 32.92), (2011, 33.27),
                    (2012, 33.51)]

    def by_weight(yr_wt_tuple):

        year, weight = yr_wt_tuple
        return weight

    print(sorted(year_cheese, key=by_weight))

def example9():
    from collections import defaultdict
    corpus_file = "/usr/share/dict/words"
    digram_count = defaultdict(int)
    with open(corpus_file) as corpus:
        for line in corpus:
            word = line.lower().strip()
            for position in range(len(word)-1):
                digram = word[position:position+2]
                digram_count[digram] += 1

    print(digram_count)

def example10():
    from collections import Counter
    corpus_file = "/usr/share/dict/words"
    digram_count = Counter()
    with open(corpus_file) as corpus:
        for line in corpus:
            word = line.lower().strip()
            for position in range(len(word)-1):
                digram = word[position:position+2]
                digram_count[digram] += 1

    print(digram_count.most_common(10))

def example11():
    corpus_file = "/usr/share/dict/words"
    hyphenated = set()
    with open(corpus_file) as corpus:
        for line in corpus:
            word = line.lower().strip()
            if '-' in word:
                hyphenated.add(word)

    print(hyphenated)

if __name__ == "__main__":
    #example1()
    #example2()
    #example3()
    #example4()
    #example5()
    #example6()
    #example7()
    #example8()
    #example9()
    #example10()
    example11()

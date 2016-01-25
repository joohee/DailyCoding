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


def example2():
    host = "ftp.ibiblio.org"
    root = "/pub/docs/books/gutenberg/"

    def directory_list(path):
        with ftplib.FTP(host, user="anonymous") as connection:
            print("Welcome: ", connection.getwelcome())
            for name, details in connection.mlsd(path):
                print(name, details['type'], details.get("size"))

    directory_list(root)

if __name__ == "__main__":
    example1()
    example2()

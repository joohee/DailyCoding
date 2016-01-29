import glob
import os

def example1():
    pictures = glob.glob("*.jpg")
    print(pictures)

    for picture in pictures:
        print(os.path.splitext(picture))
    
def example2():
    with open("chapter2.py") as data:
        clean_lines = (raw.rstrip() for raw in data)
        for line in clean_lines:
            print(line)

        print("-----")

        non_blank_lines = (line for line in clean_lines if len(line) != 0)
        for line in non_blank_lines:
            print(line)

def example3():
    import zipfile
    with zipfile.ZipFile("demo.zip", "r") as archive:
        #archive.printdir()
            first = archive.infolist()[0]
            with archive.open(first) as member:
                text = member.read()
                print(text)

            for filename in archive.namelist():
                print(filename)
                archive.extract(filename)

def example4():
    from PIL import Image
    pix = Image.open("1drachmi_1973.jpg")
    print(pix.info.keys())
    exif = pix._getexif()
    print(exif.keys())

    import PIL.ExifTags
    for k, v in pix._getexif().items():
        print(PIL.ExifTags.TAGS[k], v)

def example5():
    from PIL import Image
    import glob
    import os

    for filename in glob.glob("*.jpg"):
        name, ext = os.path.splitext(filename)
        if name.endswith("_thumb"):
            continue
        img = Image.open(filename)
        thumb = img.copy()
        w, h  = img.size
        largest = max(w, h)
        w_n, h_n = w * 128//largest, h*128//largest
        print("Resize", filename, "from", w, h, "to", w_n, h_n)
        thumb.thumbnail((w_n, h_n), Image.ANTIALIAS)
        thumb.save(name+"_thumb"+ext)

if __name__ == "__main__":
    #example1()
    #example2()
    #example3()
    #example4()
    example5()
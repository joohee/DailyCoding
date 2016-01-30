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

def example6():
    from PIL import Image
    from fractions import Fraction
    ship = Image.open("IPhone_Internals.jpg")
    w, h = ship.size
    slices = 12 
    #print(range(slices+1))
    box = [ Fraction(i, slices) for i in range(slices+1)]
    #print(box)

    try:
        for i in range(slices):
            if i == slices:
                break
            for j in range(slices):
                if j == slices:
                    break
                bounds = int(w*box[i]), int(h*box[j]), int(w*box[i+1]), int(h*box[j+i])
                #print(bounds)
    except IndexError:
        pass
    
    logo = ship.crop(bounds)
    #logo.show()
    logo.save("IPhone_Internals_logo.jpg")
    
    # ImageEnhance, ImageFilter, ImageOps
    from PIL import ImageEnhance
    e = ImageEnhance.Contrast(logo)
    #e.enhance(2.0).show()
    #e.enhance(4.0).show()
    #e.enhance(8.0).show()

    e.enhance(8.0).save("LHD_Number_1.jpg")

    from PIL import ImageFilter
    #logo.filter(ImageFilter.EDGE_ENHANCE).show()

    e.enhance(8.0).filter(ImageFilter.EDGE_ENHANCE).save("LHD_Number_2.jpg")

    # combine
    p1 = e.enhance(8.0).filter(ImageFilter.ModeFilter(8))
    #p1.filter(ImageFilter.EDGE_ENHANCE).show()
    p1.filter(ImageFilter.EDGE_ENHANCE).save("LHD_Number_2_1.jpg")

    # ImageOps
    from PIL import ImageOps
    ImageOps.autocontrast(logo).show()
    logo.show()

    ac = ImageEnhance.Contrast(ImageOps.autocontrast(logo))
    ac.enhance(2.5).save("LHD_Number_3.jpg")

def example7():
    message = "http://www.kearsarge.navy.mil"
    message.encode("UTF-8")
    message.encode("UTF-16")
    array = [hex(c) for c in message.encode("UTF-8")]
    print(array)

    from bit_calculator import Calculator
    calc = Calculator()
    message_bytes = message.encode("UTF-8")
    print(list(calc.to_bits(c) for c in message_bytes))


if __name__ == "__main__":
    #example1()
    #example2()
    #example3()
    #example4()
    #example5()
    #example6()
    example7()

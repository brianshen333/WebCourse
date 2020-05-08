import zlib
import os
import re
import binascii
#this is the core
location = "C:/Users/Brian/OneDrive/Desktop/FavouriteGrep/favourites.fav"
data = open(location,"rb").read()

text = str(zlib.decompress(data))
with open("oldfavourite.xml","w+") as myfile:
        myfile.write(text)
email = "bshen@shoplogix.com"
pattern = r",*\s*{0}\s*,*".format(email)
if re.match(pattern,text):
    print("match found")
print("Match found, deleting")
result = re.sub(pattern,'',text)
with open("favourite.xml","w+") as myfile:
    myfile.write(result)

compresseddata = zlib.compress(bytes(result, 'utf-8'))

with open("newfavourite.fav","wb") as myfile:
    myfile.write(compresseddata)


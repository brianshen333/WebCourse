import zlib
import os
import re

#this is the core
class Grep:
    def __init__(self,location,gmail):
        self.email = gmail
        self.location = location
        
    def replace(self):
        data = open(self.location,"rb").read()

        text = str(zlib.decompress(data))

        
        pattern = "({0}[\W]*,)|({0})|(,[\W]*{0})".format(self.email)
        result = re.sub(pattern,' ',text)

        with open("favourite.xml","w+") as myfile:
            myfile.write(result)
        

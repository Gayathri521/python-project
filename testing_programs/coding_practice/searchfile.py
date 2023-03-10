import os
class Searchfiles():
    def __init__(self):
        self.files=[]
    def search(self,dir,filename):
        self.dir=dir
        self.filename=filename
        self.files=[]
        for root,dir,file in os.walk(self.dir):
            if self.filename in file:
                self.files.append(os.path.join(root,filename))
        return self.files

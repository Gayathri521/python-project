import os
class Countfiles():
    def __init__(self):
        self.count=0
    def count_files(self,dir):
        self.dirname=dir
        for file in os.listdir(self.dirname):
            if file.endswith(".py"):
                self.count+=1
        return self.count
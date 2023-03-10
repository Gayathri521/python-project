from testing_programs.coding_practice.searchfile import Searchfiles
dirname=input("enter the directory example :D:\\data  \n")
filename=input("enter the file name with extensions \n")
ob=Searchfiles()
print(ob.search(dirname,filename))
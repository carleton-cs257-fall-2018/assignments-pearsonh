'''
Paul Butterfield and Henry Pearson
9/18/18, CS 257
Books, Phase 1

''' 

import csv
import sys


def main ():
    if  4 < len(sys.argv) or 3 > len(sys.argv):
        print ("Usage: books1.py input-file action [sort-direction]")
        print("input-file should be a csv file. action should be 'books' or 'authors'. \
            sort-direction should be 'forward' or 'reverse'. ")
    elif len(sys.argv) == 3:
        display(sys.argv[1], sys.argv[2], False)
    elif len(sys.argv) == 4:
        if sys.argv[3] == "reverse":
            display(sys.argv[1], sys.argv[2], True)
        elif sys.argv[3] == "forward":
            display(sys.argv[1], sys.argv[2], False)
        else:
            print("Improper input for sort-direction")

'''
This wrapper function calls get(), reverse() if necessary, 
then prints output.  

@param: inputFile: the file to read
@param action: the data to be drawn from inputFile
@param backwards: if true, reverse output.
'''

def display (inputFile, action, backwards):
    list = get(inputFile, action)
    if backwards:
      list.reverse()
    for i in list:
        print(i)

'''
This function reads the specified data (book or author names) from the
csv file and sorts it alphabetically.

@param inputFile: the file to read
@param action: the data to be drawn
@return list of book or author names, alphabetical
'''
def get (inputFile, action):
    booklist = []
    try:
       with open(inputFile, newline='') as f:
           reader = csv.reader(f)
           if action == "books":
               for row in reader:
                   booklist.append(row[0])
               booklist.sort();
               return booklist
           elif action == "authors":
               for row in reader:
                   if row[2] not in booklist:
                       booklist.append(row[2])
               for i in range(len(booklist)):
                   booklist[i] = booklist[i].split(" ")
                   for item in booklist[i]:
                       if item[0] == "(":
                           booklist[i].remove(item)
                   booklist[i].reverse()
               booklist.sort(key=lambda x: x[0])
               for i in range(len(booklist)):
                   booklist[i].reverse()
                   temp = ""
                   for name in booklist[i]:
                       temp += name + " "
                   booklist[i] = temp
               return booklist
           else:
               print ("Improper input for action")
    except FileNotFoundError:
      print("The specified data file could not be found")
      exit()

        






main()

import csv
import sys


def main ():
    if  4 < len(sys.argv) or 3 > len(sys.argv):
        print ("Usage: blah blah blah")
    elif len(sys.argv) == 3:
        #print ("debug")
        forwards(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 4:
        if sys.argv[3] == "reverse":
            backwards(sys.argv[1], sys.argv[2])
        elif sys.argv[3] == "forwards":
            forwards(sys.argv[1], sys.argv[2])
        else:
            print("Improper input for sort-direction")


def get (inputFile, action):
    #print ("debug")
    booklist = []
    with open(inputFile, newline='') as f:
        reader = csv.reader(f)
        if action == "books":
            #print ("debug")
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
                #booklist[i].pop(len(booklist[i])-1)
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
                #print(booklist[i])
            return booklist
        else:
            print ("Improper input for action")

def backwards (inputFile, action):
    list = get(inputFile, action)
    list.reverse()
    for i in list:
        print(i)

def forwards (inputFile, action):
    list = get(inputFile, action)
    for i in list:
        print(i)





main()

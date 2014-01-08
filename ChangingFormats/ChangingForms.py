import string
import csv
#These are import-ant.... man that pun even hurt me

#global variables
alphabet = string.ascii_uppercase
allnodes = []
temp = -1

def makeName(counter):
    """A recursive method to give each node an origional name.
    If there are more than 26 nodes, we recycle over to AA, AB, AC and so on.
    this is used in both converting from a list to a matrix and from a matrix to a list.""""

    global temp
    if (temp> 25):
        temp = -1
    if (counter<=25):
        letter = alphabet[counter]
        return letter
    else:
        temp = temp + 1
        return alphabet[temp] + makeName(counter-26)

####################################################################################
#The following code is for converting a matrix to a list#

#  
def readinMATRIX(csvpath):
    """This reads in a csv (taking its path in as a parameter)
    and turns it into a list of lists* (G).  Returns that list.
    Each sublist is a row in the matrix.

    *Because when we have a hammer like a language based on lists...
    ...EVERYTHING IS A NAIL"""

    G = []
    with open (csvpath, 'rb') as csvfile:
        myreader = csv.reader(csvfile)
        for row in myreader:
            G.append(row)
    return G

#
def convertMATRIX (G):
    """Method to change an adjacency matrix to a list, takes in that list of lists created by readinMATRIX
    returns nothing, but prints out the adj list in the form of a string"""
    #The number of nodes is calculated, this gives us the range of letters we need to use.  A length of 3 would mean we're using the letters A,B,and C.
    num_nodes = len(G)
    #First, we make a list of the names of all nodes (abet). 
    abet = []
    for r in xrange (num_nodes+1):
        abet.append(makeName(r))
        
    #Then we go through that alphabet and see where nodes are connected in the matrix:
        
    #Going through each letter of the alphabet (equivalent to each row in adj. matrix)
    for i in xrange (len(abet)-1):
        
        #concatenating the string...
        toprint = abet[i] + "= {"
        #Going throuhg each item in a given row
        for j in range (len(abet)-1):
            #if there is a 1 in the matrix, it means that node abet[i] and node abet[j] share an edge and should be listed as such
            if (G[i][j]=='1'):
                toprint = toprint + str (abet[j] + ',')
        toprint = toprint[0:len(toprint)-1] + "}"
        if (toprint.find("{")==-1):
            #handling the case of lonely nodes
            print "This node has no neighbors"
        else: 
            print toprint
            
####################################################################################
####################################################################################
#The following code is for converting a list to a matrix.#


M = []

#Method to read in a list from the user line by line
#N is the number of nodes in the graph
def readinLIST(n):
    """Reads in an adj list from the user node by node.
    Takes in the number of nodes in the graph,
    converts that line into a line of a global matrix (M),
    and prints out the finished adj. matrix (M)

    Yes, this is a really odd thing to do, asking the user for a string and then stripping out most of what they give you.
    But we were told to expect things in the format of: A={B,C}
    when the user wanted to note that there were edges AB and AC"""
    global M
    abet = []
    #A reminder to all non comp sci types to close your brackets.  It's important.  
    print "Please remember to close your brackets.  It's important"
    counter = 0
    #creates names for all nodes
    for r in range (n):
        abet.append(makeName(r))
    #reads in one line of the list at a time (Ex. A={B,C})
    for i in range (n):
        if (i>25):
            l="A"+str(i-25)
        else:
            l=str(abet[i])

        line = raw_input(l + "= {")
        #Strips out the commas, 
        line = line.replace(",","")
        #Strips out the closed bracket.  It is merely there for decoration.  IMPORTANT DECORATION.   
        line = line.replace("}","")
        line = line.upper()
        #At this point, the input for A= {B,C} is now BC

        #Calls the method that converts where there ARE nodes, into a line of the matrix.  
        convertLIST(line,abet)

    #Once all the lines of the matrix have been created, it prints out.  
    for line in M:
        print line 


def convertLIST(line, abet):
    """Method to convert a String that holds the names of the nodes in N(i) into a line of a matrix.
    it takes in the line of the list as well as the list of names of each node
    it outputs a line (horizontal) of a matrix""" 
    global M
    x = []
    #Goes through the name of each node 
    for i in range (len(abet)):
        #if a name and a letter in the list match, add a 1.  
        if (abet[i]in line):
            x.append (1)
        #Otherwise, add a 0
        else:
            x.append(0)
    M.append(x)


def menu():
    """Menu and essentially main method of the code.
    Presents the user options via console for if they want to go from matrix --> list
    or list --> matrix"""
    
    #generic menu greeting 
    print "Greetings!  This here be Graph Theory"
    print ""
    print ""
    print "...Yay!"

    #You will either enter a matrix or a list.
    #if you don't have a list, you have a matrix.  Thus, you really only need to ask about one.   
    a1 = raw_input("Do you have an adjacency list? (y/n)  ")
    print ""

    
    if (a1=="y"):
        print "Adjacency List.  Got it!"
        print ""
        #Need to know how many nodes there are in your list before you start with a list.  Makes life easier.  
        p=int(raw_input("How many nodes are in your graph? "))
        readinLIST(p)
        
    elif (a1=="n"):
        print "Adjacency Matrix.  Got it!"
        print ""
        #writing out a matrix via console sounds difficult and easy to mess up.  Instead, read in a file path!   Yay! 
        path = raw_input ("Please enter a filepath for your CSV: ")
        convertMATRIX(readinMATRIX(str(path)))


    
    


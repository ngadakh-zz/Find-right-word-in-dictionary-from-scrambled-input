import itertools
class solve():
    'class variable for input word and real word'
    str=None
    realWord=None
    def __init__(self):
        self.str = raw_input("Enter String : ")        #'Taking user input'
        print "Your input is ,",self.str               #'Printing user input'

    def searchString(self):
        strings = itertools.permutations(self.str, r=len(self.str))    #Making permutations of input string 
        flag=0
        fo = open("dictionary.txt","r")                 #Read dictionary
        strs = fo.read()
        b = strs.split("\n")                            #Store dictionary contents to the list b 
              
        if self.str in b:                               #Find input string in list b
            flag=1
            self.realWord =self.str
        else:
            for str1 in strings:                        #Find each string from permutaions in list b
                tstr = ''.join(str1)
                count = strs.find(tstr)
                if tstr in b:
                    flag=1                              #id string found make flag 1
                    self.realWord =tstr
        if flag==1:
            print "Word exists in dictionary, The real word is",self.realWord      # prining real word from dictionary, if input is scrambled
        else:
            print "Word not found in dictionary"
solve1 = solve()                                        #Initialized constructor
solve1.searchString()                                   #Call search function to seach input string     

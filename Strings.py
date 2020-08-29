from navigation import continuation

# if __name__ == "__main__":
#   print("Hello,\nPlease run me from the menu\n(Type \"python Navigation.py\" into your terminal)\nBye bye.")
#   exit()

# if __name__ == "navigation.py":
#   def listofstrings():
#    strings = ["Print","search","characeter search","Capitalize","string enDING","casefold","center".center(7,"#"),"c0unt characters","/b encode string!","in string?","indeXing","is alphanum3ric","is @$sc11","is d3cima1","is \'digital\'","is __id__","is lowercase"]
#   exit()


def inputs():
  print("==inputs==")
  print("enter a string to test")
  teststring =  "test sTRINg\t now with a tab string"
  print("testing for:",teststring)
  print("enter a width of characters")


print("enter a character to check for")
character = "t"
print("character set to:",character)





#STRING OPERATIONS#
def capitalize_the_string(cap):
  op = "Capitalized:"
  print(op,cap.capitalize())

def string_ending(evalue):
  print("enter a value which the string might end:\n")
  if not evalue:
    print("enter a value with which the string might end, and we will check:")
    evalue = input()
  print("does the string end with", evalue,"?\n lets check with string.endswith(value)")
  if teststring.endswith(evalue):
    print("yes")
  else:
    print("no")

def stringcasefold(sring):
  print("casefolding can be described as an \"aggressive\" lower() method which conversts strings to a state called casefolded where they can be matched without regard to case\n enter a tring to casefold:")
  string = input()
  casefolded = string.casefold()
  print("casefolded", casefolded)

def centering(string):
  def width_check(trialwidth):
  if int(trialwidth) > len(teststring):
    print("width set to:", trialwidth)
    return trialwidth
  else:
    print("please select a number larger than:", len(teststring))
    trialwidth = input()
    return width_check(trialwidth)
  print("lets look at how to center a string.\n the center method takes your string and places it in the center of the number of characters you input, and uses the character you give it (as a second input) for padding\n for example how about you input a number of characters and pick a character for padding...")
  print("\nnumber of characters in which to center your string")
  trialwidth = input()
  width = int(width_check(trialwidth))
  print("good, now pick a character within which to center your string, in other words, the character that will be used for padding...\ncharacter:")
  padder = input()
  print("great now we are going to run string.center(width,padding)\n \n")
  print(string.center(width,padder))

def charcount():
  print("lets look at the method used to count characters in a string\n for this you will basically just run string.count(character)")
  print("like always lets start with your inputs, here we will need a string, and a character for the count method to look for and tally\n lets start with your string:\n")
  string = input()
  print("now which character should we count within that string?\n")
  char = input()
  print("now we're just going to run string.count(character) and it should tell you how many there are:\n",string.count(character))
  print("\n this means there are",string.count(character)," ",character,"'s in your string:",string)

def encoding():
  print("enter a string:")
  string = input()
  print(" now we'll run string.encode(encoding = \"utf-8\", errors=\"strict\"), on your string",string.encode(encoding = "utf-8", errors="strict"))

def capitalize(string)
  print("here is how to capitalize your string using string.capitalise()",string.capitalize())

def ending(string)
  ending = string_ending(string)
  

string_ending(teststring)
print("expand tabs:", teststring.expandtabs(tabsize=32))
print("but is",evalue,"in",teststring,"? the answer might suprise you...")

def infunct(evalue,teststring,):
  if evalue in teststring:
    print("yes, yes it is")
  else:
    print("no, no its not")

def indexfunct(string):
  print("lets use index to look for the letter a, where is the first one?")
  try:
    print("answer, character",string.index("a"))
  except ValueError:
    return print("there are none, this has been an example of handling something that throws a value error.")

def a(tempstring):
  if tempstring.isalnum() == True:
    aln = "is"
  else:
    aln = "is not"
  print("the string",aln,"alphanumeric characters ONLY")
a(teststring)

def alphatest(tempstring):
  if tempstring.isalpha() == True:
    alp = "is"
  else:
    alp = "is not"
  print("the string",alp,"comprised of only alphabetical characters")

def alphatest(tempstring):
  if tempstring.isascii() == True:
    asc = "is"
  else:
    asc = "is not"
  print("the string",asc,"comprised of only alphabetical characters")

def asciitest(tempstring):
  if tempstring.isascii() == True:
    asc = "is"
  else:
    asc = "is not"
  print("the string",asc,"comprised of only valid ascii characters or may be empty")

def decimaltest(tempstring):
  if tempstring.isdecimal() == True:
    dec = "is"
  else:
    dec = "is not"
  print("the string",dec,"made up of only decimal characters")


def digittest(tempstring):
  if tempstring.isdigit() == True:
    dig = "is"
  else:
    dig = "is not"
  print("the string",dig,"made up of a digit characters")


def isidtest(tempstring):
  print("some things like str and int may be identifiers, is the string an identifier?")
  if tempstring.isidentifier() == True:
    idtest = "you bet it is"
  else:
    idtest = "heck no, it isn't"
  print(idtest)


def lowertest(tempstring):
  print("can you let me know if all the letters are lowercase?")
  if tempstring.islower() == True:
    lowertest = "they are"
  else:
    lowertest = "I can, and they are not."
  print(lowertest)

def lowercheck(string):
  if string.islower() == True:
    print("the string is in lowercase")
  else:
    print("the string has an uppercase letter or no letters at all!")    

def prtcheck(string):
  if string.isprintable() == True:
    print("it can be printed")
  else:
    print("The string cannot be printed =\(") 

def spacecheck(string):
  if string.isspace() == True:
    print("you cant trick me, the whole thing is",string.count(" "),"spaces!")

def titlecheck(string):
  if string.istitle():
    print("This String Qualifies As A \"Title Card\" Meaning The First Letter In Each Word Is capitalised.")

def uppercheck(string):
  if string.isupper():
    print("your string has atleast one cased letter, and all of the cased letters are uppercase")




def joindynamics(string):
  print("play around with joining iterable strings! \n here enter the value for string1")
  string1 = input()
  print("okay now enter the value of string2")
  string2 = input()
  print("ok now we're going to run string1.join(string2)\n",string1.join(string2))
  print("now lets run the same thing on your string:")
  print(string.join(string1))
  print("when we join one string to another, string1.join(string2) puts all of string1 after each character of string2. Iterating over all of string2.\nmore eloquently put: 'the string whose method is called is inserted in between each character of the given string.'")
  print("so if you wanted to space a string out")
  string3 = "it's very easy"
  string4 = " "
  print(string3)
  print(string4.join(string3))
  print(string4.join(string4.join(string3)))


def just(string):
  print("Lets look at some JUSTIFICATION, python has two string methods: string.ljust and string.rjust, see what they do to your input string:")
  print(string.ljust(15,"="))
  print(string.rjust(15,"="))
  continuation()
  print("the ljust and rjust methods put the specified character to the right and left of your string respectively, but careful with the first argument! it is the total number of characters in the returned string, so if you provide less than your string length there will be no justification!")
  def example():

    print("\n\n now you try, make a new string:")
    string1 = str(input())
    print("select a number of characters for the line")
    num = int(input())
    print("and select a type of character to use to justify the string")
    char = str(input())
    print("now we'll run string.ljust(number, character) string.rjust(number character) ")
    print(string1.ljust(num,char),string1.rjust(num,char))  

def convlower(string):
  print("now we'll convert your string to lowercase using string.lower() this is relatively simple")
  print("\n",string.lower())
  print("\n\n apparently the lowercasing algorithm is described in 3.13 of the unicode standard you know....")
  a = input
  elipsis = [1,2,3]
  for i in elipsis:
    print(".")
  print("if youre into that kinda thing")

def testlstrip(string):
  print("lstrip removes the leading characters given, here provide a some characters to take off the front of your string:")
  def strip(string):
    strip = input()
    print(string.lstrip(strip))
  strip(string)

## DO GET TRANS AND STR.TRANSLATE


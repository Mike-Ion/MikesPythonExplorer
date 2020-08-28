

if __name__ == "__main__":
  print("Hello,\nPlease run me from the menu\n(Type \"python Navigation.py\" into your terminal)\nBye bye.")
  exit()

if __name__ == "navigation.py":
  def listofstrings():
   strings = ["Print","search","characeter search","Capitalize","string enDING","casefold","center".center(7,"#"),"c0unt characters","/b encode string!","in string?","indeXing","is alphanum3ric","is @$sc11","is d3cima1","is \'digital\'","is __id__","is lowercase"]
  exit()



def inputs():
  print("==inputs==")
  print("enter a string to test")
  teststring =  "test sTRINg\t now with a tab string"
  print("testing for:",teststring)
  print("enter a width of characters")

# trialwidth = input()
def width_check(trialwidth):
  if int(trialwidth) > len(teststring):
    print("width set to:", trialwidth)
    return trialwidth
  else:
    print("please select a number larger than:", len(teststring))
    trialwidth = input()
    return width_check(trialwidth)

width = int(width_check(trialwidth))
print("enter a value to search among the string")
evalue = "string"
print('value set to:',evalue)
print("enter a character to check for")
character = "t"
print("character set to:",character)

print("=====string operations=====")

def capitalize_the_string(cap):
  op = "Capitalized:"
  print(op,cap.capitalize())

def string_ending(evalue):
  print("does the string end with", evalue,"?")
  if teststring.endswith(evalue):
    print("yes")
  else:
    print("no")

casefolded = teststring.casefold()
centered = teststring.center(width,"#")
charactersforcount = teststring.count(character)
encodedstring = teststring.encode(encoding = "utf-8", errors="strict")

print("capitalized:",teststring.capitalize())
print("casefolded", casefolded)
print("centered at:", centered)
print("there are", charactersforcount, character, "'s' in", teststring)
print("an encoded version of the string is", encodedstring)
string_ending(teststring)
print("expand tabs:", teststring.expandtabs(tabsize=32))
print("but is",evalue,"in",teststring,"? the answer might suprise you...")

def infunct(evalue,teststring,):
  if evalue in teststring:
    print("yes, yes it is")
  else:
    print("no, no its not")
infunct(evalue,teststring)

def indexfunct(string):
  print("lets use index to look for the letter a, where is the first one?")
  try:
    print("answer, character",string.index("a"))
  except ValueError:
    return print("there are none, this has been an example of handling something that throws a value error.")

indexfunct(tempstring)

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
alphatest(teststring)

teststring = "teststringwith"

def alphatest(tempstring):
  if tempstring.isascii() == True:
    asc = "is"
  else:
    asc = "is not"
  print("the string",asc,"comprised of only alphabetical characters")
alphatest(teststring)

def asciitest(tempstring):
  if tempstring.isascii() == True:
    asc = "is"
  else:
    asc = "is not"
  print("the string",asc,"comprised of only valid ascii characters or may be empty")
asciitest(teststring)

def decimaltest(tempstring):
  if tempstring.isdecimal() == True:
    dec = "is"
  else:
    dec = "is not"
  print("the string",dec,"made up of only decimal characters")

decimaltest(teststring)

def digittest(tempstring):
  if tempstring.isdigit() == True:
    dig = "is"
  else:
    dig = "is not"
  print("the string",dig,"made up of a digit characters")

digittest(teststring)

def isidtest(tempstring):
  print("some things like str and int may be identifiers, is the string an identifier?")
  if tempstring.isidentifier() == True:
    idtest = "you bet it is"
  else:
    idtest = "heck no, it isn't"
  print(idtest)

isidtest(teststring)

def lowertest(tempstring):
  print("can you let me know if all the letters are lowercase?")
  if tempstring.islower() == True:
    lowertest = "they are"
  else:
    lowertest = "I can, and they are not."
  print(lowertest)

lowertest(teststring)

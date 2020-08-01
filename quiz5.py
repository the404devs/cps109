#Owen Goodwin
#CPS109 Quiz #5
#10/24/18
def asciiValueStuff(str):
  outStr = ""
  for char in str:
    val = ord(char)
    if val%2==0:
      outStr = outStr + "2 "
    elif val%3==0:
      outStr = outStr + "3 "
    else:
     outStr = outStr + "0 "
  print(outStr)

def area2D(w, h):
  return w*h
def area3D(w, h ,l):
  return w*h*l
  
def bootlegReplace(haystack, toReplace, replaceWith):  
  i = 0
  char = toReplace[i]
  chars = ""
  for needle in haystack: 
     if chars == toReplace:
       break;
     if needle == char:
       chars = chars+char
       i = i+1 #what kind of language doesn't support i++?
       if i < len(toReplace):
         char = toReplace[i]
  y = haystack.find(toReplace)
  z = haystack.find(toReplace)+len(toReplace)
  firstHalf = ""
  backHalf = ""    
  for x in range(y):
    firstHalf = firstHalf + haystack[x]
  for x in range(z,len(haystack)-len(firstHalf)+1):
    backHalf = backHalf + haystack[x]
  outStr = firstHalf+replaceWith+backHalf
  return outStr
  
       
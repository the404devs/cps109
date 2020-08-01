#Owen Goodwin
#CPS109 Quiz 6
#500909196
def bootlegSubStr(haystack,needle):
  i = 0
  j = 0
  while(true):
    charN = needle[i]
    charH = haystack[j]
    print("searching for: "+charN+" in: "+charH)
    if charN==charH:
      print("found: "+charN+" at:" +str(i))
      i = i+1
      if(i>=len(needle)):
        print("we found it! it looks like \""+needle+"\" is in \""+haystack+"\"!")
        break
    else:
      if i>0:
        print("not found, try again")
        i = 0
    j = j+1
    if j>=len(haystack):
      print("oh dear, it looks like \""+needle+"\" was not found in \""+haystack+"\"...")
      break

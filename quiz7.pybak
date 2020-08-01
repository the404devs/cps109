#Owen Goodwin
#CPS109 Quiz 7
#500909196
def bootlegSearchThatActuallyGivesTheIndexThisTime(haystack,needle):
  i = 0
  j = 0
  while(true):
    charN = needle[i]
    charH = haystack[j]
    print("searching for: "+charN+" in: "+charH)
    if charN==charH:
      print("found: "+charN+" at:" +str(i))
      if i==0: startPos=j
      i = i+1
      if(i>=len(needle)):
        print("we found it! it looks like \""+needle+"\" is in \""+haystack+"\" at index: "+str(startPos)+"!")
        print(str(startPos))
        break
    else:
      if i>0:
        print("not found, try again")
        i = 0
    j = j+1
    if j>=len(haystack):
      print("oh dear, it looks like \""+needle+"\" was not found in \""+haystack+"\"... \r\nA normal search function would return -1 in this instance, but this knockoff prefers to have a friendly conversation with you")
      break

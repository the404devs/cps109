tinyWaldo = makePicture("C:\\Users\\Owen\\Desktop\\a2\\tinyWaldo.jpg")
tinyScene = makePicture("C:\\Users\\Owen\\Desktop\\a2\\tinyScene.jpg")
arr = None
def greyscale(img):
  for px in getPixels(img):
    i = getRed(px) * 0.3 + getGreen(px) * 0.6 + getBlue(px) * 0.1
    setColor(px, makeColor(i, i, i))
    
def templateMatch(t,s):
  greyscale(t)
  greyscale(s)
  o = makeEmptyPicture(getWidth(s),getHeight(s))
  for yS in range(getHeight(s)-1):
    for xS in range(getWidth(s)-1):
      #print("searching at: "+str(xS)+","+str(yS))
      lumsum = 0
      for yT in range(getHeight(t)-1):
        
        for xT in range(getWidth(t)-1):
          #print(str(xS)+" and "+str(xT))
          if xT+xS<getWidth(s) and yT+yS<getHeight(s):
            pxT = getPixel(t,xT,yT)
            pxS = getPixel(s,xS+xT,yS+yT)
            lumT = (getRed(pxT)+getGreen(pxT)+getBlue(pxT))/3
            lumS = (getRed(pxS)+getGreen(pxS)+getBlue(pxS))/3
            lumO = abs(lumT-lumS)
            #print lumO
            lumsum = lumsum+lumO
      
      setColor(getPixel(o,xS,yS),makeColor(lumsum,lumsum,lumsum))
  explore(o)






def compareOne(t,s,x1,y1):
  lumsum=0
  greyscale(t)
  greyscale(s)
  #explore(t)
  o = makeEmptyPicture(getWidth(t),getHeight(t))
  for yT in range(getHeight(t)):        
    for xT in range(getWidth(t)):
      
      if xT+x1<getWidth(s) and yT+y1<getHeight(s):
        pxT = getPixel(t,xT,yT)
        pxS = getPixel(s,x1+xT,y1+yT)
        setColor(getPixel(o,xT,yT),getColor(pxS))
        lumT = (getRed(pxT)+getGreen(pxT)+getBlue(pxT))/3
        lumS = (getRed(pxS)+getGreen(pxS)+getBlue(pxS))/3
        lumO = lumT-lumS
        #print lumO
        lumsum = lumsum+lumO
  #explore(o)
  return abs(lumsum)
  
def compareAll(t,s):
  print("Searching...")
  arr = [[0 for y in range(getHeight(s))] for x in range(getWidth(s))]
  for y in range(getHeight(s)):
    for x in range(getWidth(s)):
      #print("Searching "+str(x)+", "+str(y))
      arr[x][y] = compareOne(t,s,x,y)
  return arr
  find2Dmin(arr)
      
def find2Dmin(arr):
  print("Finding minimum value...")
  min=2147483647
  minX=[]
  minY=[]
  print arr[0][0]
  for x in range(len(arr)-1):
    for y in range(len(arr[0])-1):    
      if arr[x][y]<min and arr[x][y]>50:
        min=arr[x][y]
        minX=x
        minY=y
        displayMatch(tinyScene,x,y,33,40,makeColor(0,255,0))
  print (minX,minY)
  return (minX,minY)
  
def displayMatch(s,x1,y1,w,h,col):
  print("Found Waldo at "+str(x1)+", "+str(y1))
  addRect(s,x1,y1,w,h,col)
  explore(s)
  
def findWaldo(t,s):
  arr = compareAll(t,s)
  pt = find2Dmin(arr)
  
  displayMatch(s,pt[0],pt[1],getWidth(t),getHeight(t),makeColor(0,255,0))
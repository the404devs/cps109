beach = makePicture("O:\\Courses\\cps109\\mediasources-4ed\\beach.jpg")

def blueAndGold(img):
  for x in range(10):
    for y in range(getHeight(img)-1):
      px1 = getPixelAt(img,x,y)
      px2 = getPixelAt(img,x+getWidth(img)-10,y)
      setColor(px1,makeColor(216,171,34))
      setColor(px2,makeColor(216,171,34))      
  for y in range(10):
    for x in range(getWidth(img)-1):
      px1 = getPixelAt(img,x,y)
      px2 = getPixelAt(img,x,y+getHeight(img)-10)
      setColor(px1,makeColor(0,0,255))
      setColor(px2,makeColor(0,0,255))
      
def purpleTeeth(img):
  print("y'all should see a dentist or some shit")
  
def checkLum(r,g,b):
  lum = r*0.3+g*0.6+b*0.1
  if lum<10:
    print("lookin pretty dark fam")
  elif 50<lum<200:
    print("pretty decent")
  else:
    print("too white, but don't tell the republicans")
    
def ckBlueAbove(img,back,skyY):
  
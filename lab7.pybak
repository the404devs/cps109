beach = makePicture("O:\\Courses\\cps109\\mediasources-4ed\\beach.jpg")

caterpillar = makePicture("O:\\Courses\\cps109\\mediasources-4ed\\caterpillar.jpg")

def sunset():
  addArcFilled(beach,215,165,60,50,-10,180,makeColor(255,195,0))
  writePictureTo(beach,"H:\\q1.png")
 
def bullseye(img,x,y,w):
  addArcFilled(img,x,y,w,w,0,360,makeColor(255,0,0))
  addArcFilled(img,x+w/4,y+w/4,w/2+1,w/2+1,0,360,makeColor(0,255,0))
  addArcFilled(img,x+w/3+1,y+w/3+1,w/3+1,w/3+1,0,360,makeColor(255,255,0))
  
def drawGrid(img,sp):
  x=y=0
  while(x<getWidth(img)-1):
    addLine(img,x,0,x,getHeight(img)-1)
    x=x+sp
  while(y<getHeight(img)-1):
    addLine(img,0,y,getWidth(img)-1,y)
    y=y+sp
    
def drawGrid2(img):
  sp=5
  x=y=0
  while(x<getWidth(img)-1):
    addLine(img,x,0,x,getHeight(img)-1)
    x=x+sp
    sp=sp+3
  sp=0
  while(y<getHeight(img)-1):
    addLine(img,0,y,getWidth(img)-1,y)
    y=y+sp
    sp=sp+3
    
#This one allows the user to specify a rectangle like the greyscale one from earlier, but now we're gonna fli the box's contents horizontally
def flip(img):
  imgOut = img#Copy of the original image to work with
  for px in getPixels(img):#Loop through each pixel
    if(getX(px) in range(0,getWidth(img)-1) and getY(px) in range(0,getHeight(img)-1)):#Check if the current pixel is within the box
      setColor(getPixelAt(imgOut,getWidth(img)-getX(px)-1+0,getY(px)),getColor(px))#Set the pixel (in the output image) at the opposite position of the current one (in the input image) to the color of the current one
      #|12345678|
      #Looking at the line above, we would take the color of pixel #1 in the original image and apply it to pixel #8 in the output image
      #Afterwards, we would repeat the process, applying the color of #2 to #7, and so forth
  return imgOut
    
#This one allows the user to specify a rectangle like the greyscale one from earlier, but now we're gonna fli the box's contents horizontally
def mirror20(img):
  imgOut = img#Copy of the original image to work with
  for px in getPixels(img):#Loop through each pixel
    if(getX(px) in range(0,20) and getY(px) in range(0,getHeight(img)-1)):#Check if the current pixel is within the box
      setColor(getPixelAt(imgOut,20-getX(px)+20,getY(px)),getColor(px))#Set the pixel (in the output image) at the opposite position of the current one (in the input image) to the color of the current one
      #|12345678|
      #Looking at the line above, we would take the color of pixel #1 in the original image and apply it to pixel #8 in the output image
      #Afterwards, we would repeat the process, applying the color of #2 to #7, and so forth
  return imgOut


#This function will reduce the size of an image by half
#Ex. If the input image is 128x128, the output image will be 64x64
def reduce(img):
  xOld = yOld = xNew = yNew = 0#These represent our current x-y coords in both the new and old images. We start them at 0
  newimg = makeEmptyPicture(getWidth(img)/2, getHeight(img)/2)#Create a new empty image, half the size of the old one
  while(true):#infinite loop
    px1 = getPixel(img, xOld,yOld)#Here we grab 4 pixels, like this....
    px2 = getPixel(img, xOld+1,yOld)#        px1|px2
    px3 = getPixel(img, xOld,yOld+1)#        ---|---
    px4 = getPixel(img, xOld+1,yOld+1)#      px3|px4
    r = (getRed(px1) + getRed(px2) + getRed(px3) + getRed(px4))/4#Take the average red value of the 4 pixels
    g = (getGreen(px1) + getGreen(px2) + getGreen(px3) + getGreen(px4))/4#Do the same with the green and blue values
    b = (getBlue(px1) + getBlue(px2) + getBlue(px3) + getBlue(px4))/4
    setColor(getPixel(newimg, xNew, yNew), makeColor(r,g,b))#Set the colour of the current pixel in the new image to a colour created from the average values just taken
    xOld = xOld+2#Increase our x-value for the old picture by 2, since we already took care of the pixel beside the old x-value
    if(xOld >= getWidth(img)-1):#If that new x-value is beyond the width of the old image...
      xOld = 1#Reset to 1. This is because if we reset to 0, our image will come out slanted, and while that may look cool it's not what we want.
      yOld = yOld+2#Increase current y-value by 2, for the same reason we do it for the x-value
    xNew = xNew+1#Add one to our x-value in the new image
    if(xNew >= getWidth(newimg)-1):#Again, if we've gone beyond the bounds of the image...
      xNew=0#reset to 0
      yNew=yNew+1#go to the next row
    if(yOld >= getHeight(img) or yNew >=getHeight(newimg)):#Check if we've gone beyond the height of either image, which would indicate that we're done here
      break#end the loop
  return newimg
  
  
#fuck just do this later
def grow(img):
  xOld = yOld = xNew = yNew = 0#These represent our current x-y coords in both the new and old images. We start them at 0
  newimg = makeEmptyPicture(getWidth(img)*2, getHeight(img)*2)#Create a new empty image, twice the size of the old one
  while(true):#infinite loop
    px0 = getPixel(img, xOld,yOld)
    px1 = getPixel(newimg, xNew,yNew)#Here we grab 4 pixels, like this....
    px2 = getPixel(newimg, xNew+1,yNew)#        px1|px2
    px3 = getPixel(newimg, xNew,yNew+1)#        ---|---
    px4 = getPixel(newimg, xNew+1,yNew+1)#      px3|px4
    r = getRed(px0)
    g = getGreen(px0)
    b = getBlue(px0)
    setColor(px1, makeColor(r,g,b))
    setColor(px2, makeColor(r,g,b))
    setColor(px3, makeColor(r,g,b))
    setColor(px4, makeColor(r,g,b))
    
    xNew = xNew+2#Increase our x-value for the old picture by 2, since we already took care of the pixel beside the old x-value
    if(xNew >= getWidth(newimg)-1):#If that new x-value is beyond the width of the old image...
      xNew = 1#Reset to 1. This is because if we reset to 0, our image will come out slanted, and while that may look cool it's not what we want.
      yNew = yNew+2#Increase current y-value by 2, for the same reason we do it for the x-value
    xOld = xOld+1#Add one to our x-value in the new image
    if(xOld >= getWidth(img)-1):#Again, if we've gone beyond the bounds of the image...
      xOld=0#reset to 0
      yOld=yOld+1#go to the next row
    if(yNew >= getHeight(newimg) or yOld >=getHeight(img)):#Check if we've gone beyond the height of either image, which would indicate that we're done here
      break#end the loop
  writePictureTo(newimg,"H:\\fuck.png")
  return newimg
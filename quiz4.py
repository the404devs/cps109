#Owen Goodwin
#CPS109 Lab #4
#10/03/18
def find_max(nums):
  max = 0
  for num in nums:
    if num > max:
      max = num
  return max
  
def pixel_offset(img, n):
  for px in getPixels(img):
    r = getRed(px) + n
    if r > 255:
      r =  r - 255
    g = getGreen(px) + n
    if g > 255:
      g =  g - 255
    b = getBlue(px) + n
    if b > 255:
      b =  b - 255
    col = makeColor(r, g, b)
    setColor(px, col)
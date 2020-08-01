#Owen Goodwin
#CPS109 Quiz #2
#09/19/18

def calculate_seq(digits, opr):
  total = 0
  for digit in digits:
    value = int(digit)
    total+=value
  if opr == "-":
    total = total*(-1)
  print total


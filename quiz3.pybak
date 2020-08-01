#Owen Goodwin
#CPS109 Quiz #3
#09/26/18
def cumulative_sum(nums):
  sums = [0] * (len(nums)+1)#Will store the sums. +1 because the first sum will be 0 and we don't want it
  result = [0] * len(nums)#transfer the sums here later
  for i in range(len(nums)):#loop through each number
    sums[i+1] = nums[i]+sums[i]#get the sum of the number, put it in our sums array. First element will be 0, then the rest will be all the sums
    result[i] = sums[i+1]#put that same element into the result array, to the left 1 position. this eliminates the first 0 and makes our final result the proper length.
  return result


def decode(message, key):
  alpha="abcdefghijklmnopqrstuvwxyz"
  rest = ""
  for letter in alpha:
    if not(letter in key):
      rest = rest + letter
  alpha2 = rest+key
  secret = ''
  message = message.lower()
  #basically the only change needed for this one was to swap 'alpha' and 'alpha2' in the for loop.
  for letter in message :
    if letter.lower() in alpha2:
      i = alpha2.find(letter)
      secret = secret + alpha[i]
  return secret
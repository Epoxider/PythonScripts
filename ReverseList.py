def reverseList(nums):
  temp = 0
  j = len(nums)-1
  for i in range(len(nums)-1):
    print("i = "+str(i) + " " + "j = " + str(j) + '\n')
    if len(nums)%2==0 and i == j+1:
      print('breaking')
      break
    elif len(nums)%2==1 and i==j:
      break
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
    j -= 1
    print(nums)
  return nums

print(reverseList([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))

def del_duplikat(arr):
   count = 0
   arr1 = []
   while arr:
       a = arr.pop()
       if a in arr:
           count+=1
       else:
           arr1.append(a)
   for i in range(count):
       arr1.append('_')
   return arr1

print(del_duplikat([4,1,5,1,8,5,4]))
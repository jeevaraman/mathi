n=5
sum=0
temp=num
while(temp>0):
  digit = temp % 10
  sum += digit ** 3
  temp //= 10
 if(num==sum):
    print("it is arm strong")
 else:
     print("not armstrong")

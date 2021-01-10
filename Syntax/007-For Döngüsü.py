
sehirler = ["İzmir","Ankara","Muş"]

for x in sehirler:
  print(x)
  
# Break kullanımı
for harf in 'İlkay Ergül':
  if harf == ' ':
    break
    
#List comprehension - square of even numbers
nums = [1,2,3,4,5,6,7]
numsqr = [x*x for x in nums if x%2==0]
print(numsqr)

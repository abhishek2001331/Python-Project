list1 = [1,2,3,4,5,6]
print(list1)
print(list1[3])
#traverse
for i in list1:
    print(i)

#even Odd    
count = 0
for i in list1:
    if(i % 2 == 0):
        count = count+1
        print(count)
    print(len(list1) - count)
      
#average
n = len(list1)
#for i in list1:
avg = sum(list1) / n
print(avg)


#append(),insert() , remove() , pop() , len() ,extend() , reverse(), sort(), clear(),copy() ,count() , del keyword
l1 = ["apple" , "mango", "banana","orange"]
l1.append("greps")
print(l1)
l1.remove("orange")
print(l1)
l1.insert(2,"gwava")
print(l1)

print(len(l1))

l1.pop(2)
print(l1)

l1.reverse()
print(l1)

l1.sort()
print(l1)

l2 = l1.copy()
print(l2)

l1.clear()
print(l1)




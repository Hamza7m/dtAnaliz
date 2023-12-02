import numpy as np 
print("Hello world from main ")
list = [1,2,3,4,4,7,4]

array = np.array(list)
print(array)

for i in range(len(array)):
    print(str(i) + ".iter : " + str(array[i]))
    
maxsimum = np.max(list)

print(maxsimum)
minimum = np.min(list)
print(minimum)
num = np.random.randint(maxsimum)

newList = np.add(array,num)
for x in range(len(array)):
    print(str(i) + ".iter" + str(newList[x]))
    

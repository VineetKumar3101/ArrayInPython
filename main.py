import numpy as np
print("\n-----------------------------------------------------")

#list
arr=[23,4,25,6,8]
for i in range(5):
    print(arr[i])

print("\n-----------------------------------------------------")


#2d Array(list)
arr2= [[23, 4, 25],[5,1,3],[61,6, 8]]
print(arr2)

print("\n-----------------------------------------------------")

#in matrix
arr3= [[23, 4, 25],[5,1,3],[61,6, 8]]
for j in range(3):
    for k in range(3):
        print(arr3[j][k],end=" ")
    print()

print("\n-----------------------------------------------------")

arr4= [[23, 4, "Anshu"],[5,1.0,"Aryan"],["Vineet",6+6j, 8]]
for m in range(3):
    for n in range(3):
        print(arr4[m][n],end=" ")
    print()

print("\n-----------------------------------------------------")

#using numpy class (1d array)
z=np.array([1,2,3,6,58,9,3,4,3])
print(z)
print(z.shape)

print("\n-----------------------------------------------------")

#using numpy class (2d array)
y=np.array([[23, 4, 25],[5,1,3],[61,6, 8]])
print(y)
print(y.shape)

print("\n-----------------------------------------------------")

w=np.array([[23, 4, 25],[5,1,3],[61,6, 8],[2,6,8]])
print(w)

print(w.shape)

print(w.reshape(3,4))

print(w.reshape(2,3,2))


print("\n-----------------------------------------------------")

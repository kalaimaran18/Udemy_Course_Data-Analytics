import numpy as np
arr1=np.array([1,2,3,4,5])
print(arr1)
print(type(arr1))

# Identity matrix method
arr1=np.eye(3)
print(arr1)

#Array Vectorized Operation
ar1=([2,4,5,6,7,8])
ar2=([1,3,6,5,9,7])
print("Addition",ar1+ar2)
##Square Root
print(np.sqrt(ar1))
## Exponential
print(np.exp(ar2))
## Sine
print(np.sin(ar2))
## Natural Log
print(np.log(ar2))

## Array Slicing and Indexing

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[0][0])
print(arr[0:1,2:])

## Modify Array Element
arr[0][0]=20
print(arr)

## Statistical Concepts
data=np.array([1,2,3,7,8,9])
mean=np.mean(data)
std_dev=np.std(data)
normalize_data=(data-mean)/std_dev
print(normalize_data)
print(np.var(data))
print(std_dev)
print(mean)


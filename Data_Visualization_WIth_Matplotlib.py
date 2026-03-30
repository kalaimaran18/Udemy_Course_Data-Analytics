## Data Visualization with Matplotlib

import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1,4,9,16,15]

# Create a Line Plot
plt.plot(x,y)
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title("Basic Line Plot")


## Create a Customized Line Plot
plt.plot(x,y,color='RED',linestyle='--')
plt.grid(True)
plt.show()

## Multiple Plots 
c=[3,2,7,6,8,4]
b=[9,12,15,18,21,24]
d=[10,20,30,40,50,60]
plt.figure(figsize=(9,5))
plt.subplot(1,2,1)
plt.plot(c,b,color='green')
plt.title("Plot1")
plt.show()


## Bar Plot
categories=['A','B','C','D','E','F']
Values=[5,7,3,8,6,1]
plt.bar(categories,Values,color='yellow')
plt.show()
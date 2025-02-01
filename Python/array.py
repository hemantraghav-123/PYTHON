# import numpy as np
# a= np.array([range( i , i+4)for i in[1,3,5]])
# print(a)


# import numpy as np
# a= np.array([[1,2],[3,4]])
# b= np.array([[5,6], [7,8]])
# c= np.dot(a,b)
# print(c)


import numpy as np
a= np.arange(10)
b= a[1:5]
b[0]=10
print(a)
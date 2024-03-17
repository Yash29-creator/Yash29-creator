# Guide for NumPy
<pre>
import numpy as np</br>
a = np.array([1,2,3])</br>
b = np.array([(1.5,2,3), (4,5,6)], dtype = float)</br>
c = np.array([[(1.5,2,3), (4,5,6)],[(3,2,1), (4,5,6)]], dtype = float)</br>

np.zeros((3,4)) #Create an array of zeros</br>
np.ones((2,3,4),dtype=np.int16) #Create an array of ones</br>
d = np.arange(10,25,5)#Create an array of evenly spaced values (step value)</br>
np.linspace(0,2,9) #Create an array of evenlyspaced values (number of samples)</br>
e = np.full((2,2),7)#Create a constant array</br>
f = np.eye(2) #Create a 2X2 identity matrix</br>
np.random.random((2,2)) #Create an array with random values</br>
np.empty((3,2)) #Create an empty array</br>
</br>
np.save('my_array' , a)</br>
np.savez( 'array.npz', a, b)</br>
np.load( 'my_array.npy')</br>
np.loadtxt("myfile.txt")</br>
np.genfromtxt("my_file.csv", delimiter= ',')</br>
np.savetxt( "myarray.txt", a, delimiter= " ")</br>
np.info(np.ndarray.dtype)</br>
</br>
a.shape #Array dimensions</br>
len(a)#Length of array</br>
b.ndim #Number of array dimensions</br>
e.size #Number of array elements</br>
b.dtype  #Data type of array elements</br>
b.dtype.name  #Name of data type</br>
b.astype(int). #Convert an array to a different type</br>
</br>
np.int64 #Signed 64-bit integer types</br>
np.float32. #Standard double-precision floating point</br>
np.complex. #Complex numbers represented by 128 floats</br>
np.bool  #Boolean type storing TRUE and FALSE values</br>
np.object #Python object type</br>
np.string_ #Fixed-length string type</br>
np.unicode_ #Fixed-length unicode type</br>
</br>
g = a - b. #Subtraction</br>
np.subtract(a,b) #Subtraction</br>
  array([[-0.5,0. ,0.], [-3. , -3. , -3. ]])</br>
b + a #Addition </br>
np.add(b,a) #Addition</br> 
  array([[ 2.5, 4. , 6.],[5. ,7. ,9. ]])</br>
a/b #Division </br>
np.divide(a,b) #Division </br>
 array([[0.66666667,1. ,1.],[0.25 ,0.4 ,0.5 ]])</br>
a * b #Multiplication </br>
np.multiply(a,b) #Multiplication </br>
  array([[1.5, 4. ,9.],[ 4. , 10. , 18. ]])</br>
np.exp(b) #Exponentiation</br>
np.sqrt(b) #Square root</br>
np.sin(a)  #Print sines of an array</br>
np.cos(b) #Elementwise cosine</br>
np.log(a)#Elementwise natural logarithm</br>
e.dot(f) #Dot product </br>
 array([[7.,7.],[7.,7.]])</br>
</br>
a == b #Elementwise comparison</br>
 array([[False , True, True],</br>
             [ False,False ,False ]], dtype=bool)</br>
a< 2 #Elementwise comparison</br>
   array([True, False, False], dtype=bool)</br>
np.array_equal(a, b) #Arraywise comparison</br>
</br>
h = a.view()#Create a view of the array with the same data</br>
np.copy(a) #Create a copy of the array</br>
h = a.copy() #Create a deep copy of the array</br>
</br>
a.sort() #Sort an array</br>
c.sort(axis=0) #Sort the elements of an array's axis</br>
</br>
a[2] #Select the element at the 2nd index</br>
  3</br>
b[1,2] #Select the element at row 1 column 2(equivalent to b[1][2])</br>
  6.0</br>
a[0:2]#Select items at index 0 and 1</br>
 array([1, 2])</br>
b[0:2,1] #Select items at rows 0 and 1 in column 1</br>
  array([ 2.,5.])</br>
b[:1] #Select all items at row0(equivalent to b[0:1, :])</br>
  array([[1.5, 2., 3.]])</br>
c[1,...] #Same as [1,:,:]</br>
 array([[[ 3., 2.,1.],[ 4.,5., 6.]]])</br>
a[ : : -1] #Reversed array a array([3, 2, 1])</br>
</br>
a[a<2] #Select elements from a less than 2</br>
 array([1])</br>
</br>
b[[1,0,1, 0],[0,1, 2, 0]] #Select elements(1,0),(0,1),(1,2) and(0,0)</br>
  array([ 4. , 2. , 6. ,1.5])</br>
b[[1,0,1, 0]][:,[0,1,2,0]] #Select a subset of the matrix’s rows and columns</br>
 array([[ 4. ,5. , 6. , 4.],[1.5, 2. , 3. ,1.5],[ 4. ,5. , 6. , 4.],[1.5, 2. , 3. ,1.5]])</br>
</br>
i = np.transpose(b) #Permute array dimensions</br>
i.T #Permute array dimensions</br>
</br>
b.ravel() #Flatten the array</br>
g.reshape(3, -2) #Reshape, but don’t change data</br>
</br>
h.resize((2,6)) #Return a new arraywith shape(2,6)</br>
np.append(h,g) #Append items to an array</br>
np.insert(a,1,5)  #Insert items in an array</br>
np.delete(a,[1])  #Delete items from an array</br>
</br>
np.concatenate((a,d),axis=0) #Concatenate arrays</br>
 array([1, 2, 3, 10, 15, 20])</br>
np.vstack((a,b) #Stack arrays vertically(row wise)</br>
 array([[1. , 2. , 3.],[1.5, 2. , 3.],[ 4. ,5. , 6. ]])</br>
np.r_[e,f] #Stack arrays vertically(row wise)</br>
np.hstack((e,f)) #Stack arrays horizontally(column wise)</br>
 array([[7.,7.,1.,0.],[7.,7.,0.,1.]])</br>
np.column_stack((a,d)) #Create stacked column wise arrays</br>
 array([[1, 10],[ 2, 15],[ 3, 20]])</br>
np.c_[a,d] #Create stacked column wise arrays</br>
</br>
np.hsplit(a,3) #Split the array horizontally at the 3rd index</br>
  [array([1]),array([2]),array([3])]</br>
np.vsplit(c,2) #Split the array vertically at the 2nd index</br>
  [array([[[ 1.5, 2. ,1.],[ 4. ,5. , 6. ]]]),</br>
   array([[[ 3., 2., 3.],[ 4.,5., 6.]]])]</br>
</pre>

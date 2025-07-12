[identity](http://docs.scipy.org/doc/numpy/reference/generated/numpy.identity.html#numpy.identity)
The identity tool returns an identity array. An identity array is a square matrix with all the main diagonal elements as  and the rest as . The default type of elements is float.
```py
import numpy
print numpy.identity(3) #3 is for  dimension 3 X 3

#Output
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
```
[eye](http://docs.scipy.org/doc/numpy/reference/generated/numpy.eye.html#numpy-eye)
The eye tool returns a 2-D array with 's as the diagonal and 's elsewhere. The diagonal can be main, upper or lower depending on the optional parameter . A positive  is for the upper diagonal, a negative  is for the lower, and a   (default) is for the main diagonal.
```py
import numpy
print numpy.eye(8, 7, k = 1)    # 8 X 7 Dimensional array with first upper diagonal 1.

#Output
[[ 0.  1.  0.  0.  0.  0.  0.]
 [ 0.  0.  1.  0.  0.  0.  0.]
 [ 0.  0.  0.  1.  0.  0.  0.]
 [ 0.  0.  0.  0.  1.  0.  0.]
 [ 0.  0.  0.  0.  0.  1.  0.]
 [ 0.  0.  0.  0.  0.  0.  1.]
 [ 0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.]]

print numpy.eye(8, 7, k = -2)   # 8 X 7 Dimensional array with second lower diagonal 1.
```

### Task
Your task is to print an array of size $N$X$M$ with its main diagonal elements as $1$'s and $0$'s everywhere else.

### Note
In order to get alignment correct, please insert the line $numpy.set_printoptions(legacy='1.13')$ below the numpy import.

### Input Format
A single line containing the space separated values of $N$ and $M$.
$N$ denotes the rows.
$M$ denotes the columns.

### Output Format
Print the desired $N$X$M$ array.

### Sample Input
```py
3 3
```
### Sample Output
```py
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
```
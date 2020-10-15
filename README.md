# linear_algebra
a module for using linear algebraic mathematical objects on python. a personal exercise.

# class: matrix

instance attributes : 

>itself:   an array in the form [[row], [row], ..., [row]] 

>rowcount:  number of rows

>colcount:  number of columns

>rows:   same as itself

>columns:  an array in the form [[column], [column], ..., [column]]

instance methods:

>show():   shows the matrix in a way that looks similar to notation in mathematics.

>scalar_multiple(scalar):  takes the scalar multiple of the matrix with the given scalar and returns another matrix.

# class: vector

instance attributes : 

> same except:

> colcount is always 1, no rows or columns attributes.

> additional norm attribute, with the value of the vector's norm (or magnitude)

instance methods:

> show():  same as matrix

> scalar_multiple(scalar):   same as matrix

> isparallel(vector):    returns True if given vector is parallel to the vector in the argument, false otherwise.

> isorthogonal(vector):    returns True if given vector is orthogonal (perpendicular) to the vector in the argument, false otherwise.

> projection(vector, rnd=16):    returns the projection vector of the given vector in respect to the vector in the argument. ( rnd = round)

> anglebetween(vector, rnd=16):    returns the angle (in radians) between the given vector and the vector in the argument. (rnd = round)

# objects:

 x_hat, y_hat and z_hat unit vectors in R3, x_hat2 and y_hat2 unit vectors in R2.

# functions:

addition(a, b):   returns a matrix (vector) formed by the addition of matrices(vectors) a and b.

multiplication(a, b):   returns a matrix (vector) formed by the multiplication of matrices(vectors) a and b.

power(a, pow):   returns a matrix(vector) formed by taking the 'pow'th power of the matrix(vector) a.

dot_product(v1, v2):    returns the dot product of vectors v1 and v2.

complex_length(cmplx):    returns the length (magnitude) of the complex number cmplx.

polar_form(cmplx, rnd=16):    returns a tuple (length, theta) as in the polar form (length).(cos(theta) + isin(theta))

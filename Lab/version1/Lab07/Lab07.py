import numpy

# Exercise 1
A = numpy.array([[3, 1], [2, 3]])
B = numpy.array([[1, 2, 3], [4, 2, 1], [2, 4, 4]])

# a) Print the 2nd row of A


def exercise1_a():
    print(A[-1])

# exercise1_a()

# b) Print the 3rd row of B


def exercise1_b():
    print(B[-1])

# exercise1_b()

# c) The first element of the 2nd row of B


def exercise1_c():
    print(B[1][0])

# exercise1_c()

# d) The 3rd element of the 1st row of B


def exercise1_d():
    print(B[0][-1])

# exercise1_d()

# e) The 3rd column of B


def exercise1_e():
    for i in range(len(B)):
        print(B[i, -1])

# exercise1_e()

# f) The 2nd column of B


def exercise1_f():
    for i in range(len(B)):
        print(B[i, 1])

# exercise1_f()

# g) The 1st column of A


def exercise1_g():
    for i in range(len(A)):
        print(A[i, 0])

# exercise1_g()


# Exercise 2
A = numpy.array([[12, 3], [2, 7]])
B = numpy.array([[3, -1], [1, 2]])


def exercise2_a():
    print(numpy.add(A, B))

# exercise2_a()


def exercise2_b():
    print(numpy.subtract(A, B))

# exercise2_b()


def exercise2_c():
    print(numpy.add(2 * A, 3 * B))

# exercise2_c()


def exercise2_d():
    print(numpy.dot(A, B))

# exercise2_d()


def exercise2_e():
    print(numpy.dot(B, A))

# exercise2_e()


def exercise2_f():
    print(numpy.linalg.matrix_power(A, 2))

# exercise2_f()


def exercise2_g():
    print(numpy.subtract(numpy.linalg.matrix_power(
        A, 2), 2 * numpy.linalg.matrix_power(B, 2)))

# exercise2_g()

# Exercise 3


def exercise3_a():
    A = numpy.array([[4, 5], [3, 4]])
    print(numpy.linalg.inv(A))


# exercise3_a()


def exercise3_b():
    A = numpy.array([[-1, 0], [1, 1]])
    print(numpy.linalg.inv(A))


# exercise3_b()


def exercise3_c():
    A = numpy.array([[1, 2, 1], [3, 2, 1], [1, 2, 1]])
    try:
        print(numpy.linalg.inv(A))
    except:
        print("Matrix is not invertible")


# exercise3_c()


def exercise3_d():
    A = numpy.array([[1, 2, 1], [3, 2, 1], [1, 2, 1]])
    try:
        print(numpy.linalg.inv(A))
    except:
        print("Matrix is not invertible")


# exercise3_d()

#  Exercise 4
A = numpy.array([[1/2, 2, 0], [2, 4, 4], [2, 3, 4/9]])
B = numpy.array([[-3/4, 2, 1], [2, 4, 3], [3, 4, 2]])


def exercise4_a():
    print(numpy.dot(numpy.linalg.inv(A), B))

# exercise4_a()


def exercise4_b():
    print(numpy.dot(2 * A.T, B))

# exercise4_b()


def exercise4_c():
    print(numpy.linalg.inv(numpy.add(A.T, numpy.linalg.inv(B))))

# exercise4_c()


def exercise4_d():
    print(numpy.dot(numpy.subtract(A, B), numpy.add(A, B)).T)

# exercise4_d()

import numpy


lis1 = numpy.array([[1,2], [1,2], [1,2], [1,2]])
lis2 = numpy.array([[3,4], [3,4], [3,4]])
#
# print(numpy.concatenate(([[1,2], [1,2], [1,2], [1,2]], [[3,4], [3,4], [3,4]]), axis=0))

# array_1 = numpy.array([[1,2,3],[0,0,0], [2,2,2]])
# array_2 = numpy.array([[0,0,0],[7,8,9], [3,3,3]])
# print(numpy.concatenate((array_1, array_2), axis = 0))

print(numpy.zeros((3,3,3), dtype=int))
import math
from math import sqrt
import numbers


'''if self.h != other.w or self.w != other.h:
            raise(ValueError, "Dimension error")''' 

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
    
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1:
            det = self.g[0][0]
            
        elif self.h == 2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]

            det = 1/(a*d-b*c)
        return det

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        
        t_ele = 0
        for i in range(self.h):
            for j in range(self.w):
                ele = self.g[i][j]
                if i == j:
                    t_ele = t_ele + self.g[i][j]
        return t_ele

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        

        if self.h == 1:
            inv = []
            inv.append([1/self.g[0][0]])
            
        else:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            factor = 1 / (a * d - b * c)
            
            inv = [[d, -b],[-c, a]]
            
            for i in range(len(inv)):
                for j in range(len(inv[0])):
                    inv[i][j] = factor * inv[i][j]
                    
        return Matrix(inv)

    
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        matrix_transpose = []
        for i in range(self.w):
            new_row = []
            for j in range(self.h):
                new_row.append(self.g[j][i])
            matrix_transpose.append(new_row)
        return Matrix(matrix_transpose)

    
    def is_square(self):
        return self.h == self.w

    
    
    
    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self, other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        matrixSum = []
    
        # matrix to hold a row for appending sums of each element
        row = []
        sumAB = 0
        
        for i in range(self.h):
            row = []
            for j in range(self.w):
                sumA = self.g[i][j]
                sumB = other.g[i][j]
                sumAB = sumA + sumB
                row.append(sumAB)
            matrixSum.append(row)
       
        return Matrix(matrixSum)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        matrixNeg = []
        row = []
        neg_A = 0
        
        for i in range(self.h):
            row = []
            for j in range(self.w):
                neg_A = -self.g[i][j]
                row.append(neg_A)
            matrixNeg.append(row)
       
        return Matrix(matrixNeg)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        matrixSub = []
        row = []
        subAB = 0
        
        for i in range(self.h):
            row = []
            for j in range(self.w):
                subA = self.g[i][j]
                subB = other.g[i][j]
                subAB = subA - subB
                row.append(subAB)
            matrixSub.append(row)
       
        return Matrix(matrixSub)
    
    def __mul__(self, other):
        
        matrixMul = []
        
        
        for i in range(self.h):
            row = []
            for j in range(other.w):
                mulRes = 0
                for k in range(other.h):
                    mulRes += self.g[i][k] * other.g[k][j]
                row.append(mulRes)
            matrixMul.append(row)
        return Matrix(matrixMul)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        
        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        matrixSS = []
    
        # matrix to hold a row for appending sums of each element
        row = []
        ScaMul = 0
        
        for i in range(self.h):
            row = []
            for j in range(self.w):
                ScaMul = other * self.g[i][j]
                row.append(ScaMul)
            matrixSS.append(row)
       
        return Matrix(matrixSS)
    
        '''if isinstance(other, numbers.Number):
            pass'''
            
import math

from ._global import EPSILON


class Vector:
    def __init__(self, lst):
        
        self._values = list(lst)
        
    def __getitem__(self, index):
        return self._values[index]
    
    def __repr__(self):
        return 'Vector({})'.format(self._values)
    
    def __len__(self):
        return len(self._values)
    
    def __add__(self, another):
        assert len(self) == len(another), \
        "Error in adding. Length of vectors must be same. "
        return Vector([a + b for a, b in zip(self, another)])
    
    def underlying_list(self):
        return self._values
    
    def __sub__(self, another):
        assert len(self) == len(another), \
        "Error in subing. Length of vectors must be same. "
        return Vector([a - b for a, b in zip(self, another)])
    
    def __mul__(self, k):
        return Vector([k*e for e in self])
    
    def __rmul__(self, k):
        return self * k
    
    def __truediv__(self, k):
        return (1/k)*self 
    
    def __pos__(self):
        return 1 * self
        
    def __neg__(self):
        return -1 * self
    
    def __iter__(self):
        return self._values.__iter__()
    
    def __str__(self):
        return '({})'.format(', '.join(str(e) for e in self._values))
    
    @classmethod
    def zero(cls, dim):
        return cls([0] * dim)
    
    def norm(self):
        return math.sqrt(sum(e**2 for e in self))
    
    def dot(self, another):
        """向量的点乘"""
        assert len(self) == len(another), \
        "Error in subing. Length of vectors must be same. "
        return sum(a * b for a, b in zip(self, another))
    
    def normalize(self):
        if self.norm() -0.0 < EPSILON:
            raise ZeroDivisionError("Normalize error! norm is zero vector {} .".format(self._values))
        return Vector(self._values) / self.norm() 
    

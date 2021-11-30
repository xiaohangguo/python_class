import math


class Triangle:
    def __init__(self,a,b,c,shape='Triangle'):
        if a+b <= c or a+c <=b or b+c<=a :
                raise Exception('ParamsError')
        self.__a = a
        self.__b = b
        self.__c = c
        self.__P = a+b+c
        p = self.__P/2
        self.__S = math.sqrt(p *(p-a)*(p-b)*(p-c))
        self.__shape=shape
    def __repr__(self):
        return '形状为%s三边为(a=%r,b=%r,c=%r)'%(self.__shape,self.__a,self.__b,self.__c)
    def __show__(self):
        print('周长为',self.__P)
        print('面积为',self.__S)
        #return '周长为%r'%(self.__P)
s1 = Triangle(6,8,10)
print(s1)
s1.__show__()

class RightTrangle(Triangle):
    def __init__(self,a,b,c,shape='RightTrangle'):
        def eq(x,y):
            e = 0.00000001
            if abs(x-y):
                return True
            else:
                return False
        x,y,z = a*a,b*b,c*c
        if eq(x,y+z) or eq(y,x+z) or eq(z,x+y):
           # Triangle.__init__(self,a,b,c,'RightTriangle')
            super().__init__(a,b,c,shape)
            m = max(a,b,c)
            if a ==m:
                self.__right='angle_A'
            elif b ==m:
                self.__right='angle_B'
            else:
                self.__right='angle_C'
        else:
            raise Exception('ParmsError')
    def show(self):
        super().__show__()
        print('right angle=',self.__right)
s3 =RightTrangle(3,4,5)
print(s3)
s3.show()
class IsoTrangle(Triangle):
    def __init__(self,a,b,c,shape='IsoTrangle'):
        def eq(x,y):
            e = 0.00000001
            if abs(x-y)<e:
                return True
            else:
                return False
        if eq(a,b) or eq(b,c) or eq(a,c):
            super().__init__(a,b,c,shape)
            if eq(a,b):
                self.__iso=['a','b',a]
            elif eq(a,c):
                self.__iso=['a','c',b]
            else:
                self.__iso=['b','c',c]
        else:
             raise Exception('ParamsError')
    def show(self):
        print('Isosides:',self.__iso)

        super().__show__()

s4 = IsoTrangle(3,3,5)
s4.show()
print(s4)

class IsoRightTriangle(IsoTrangle,RightTrangle):
    def __init__(self,a,b,c,shape='IsoRightTriangle'):
        # IsoTrangle.__init__(self,a,b,c)
        # RightTrangle.__init__(self,a,b,c)
        super().__init__(a,b,c,shape)
    def show(self):
       # IsoTrangle.show(self,False)
        super().show()
s5  = IsoRightTriangle(3,3,math.sqrt(18))
print(s5)
s5.show()
s6 = IsoRightTriangle(4,4,math.sqrt(32))
print(s6)
s6.show()

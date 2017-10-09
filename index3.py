#coding=utf-8
class Vecter3:
    def __init__(self, x=0, y=0, z=0):
        self.X = x
        self.Y = y
        self.Z = z
    def __add__(self, n):
        r = Vecter3()
        r.X = self.X + n.X
        r.Y = self.Y + n.Y
        r.Z = self.Z + n.Z
        return r
    def __sub__(self, n):
        r = Vecter3()
        r.X = self.X - n.X
        r.Y = self.Y - n.Y
        r.Z = self.Z - n.Z
        return r
    def __mul__(self, n):
        r = Vecter3()
        r.X = self.X * n
        r.Y = self.Y * n
        r.Z = self.Z * n
        return r
    def __truediv__(self, n):
        r = Vecter3()
        r.X = self.X / n
        r.Y = self.Y / n
        r.Z = self.Z / n
        return r
    def __floordiv__(self, n):
        r = Vecter3()
        r.X = self.X // n
        r.Y = self.Y // n
        r.Z = self.Z // n
        return r
    def show(self):
        print((self.X,self.Y,self.Z))
v1 = Vecter3(1,2,3)
v2 = Vecter3(4,5,6)
v3 = v1+v2
v3.show()
v4 = v1-v2
v4.show()
v5 = v1*3
v5.show()
v6 = v1 // 2
v6.show()




'''#coding=utf-8
import types
class Person(object): #基类必须继承于object，否则在派生类中将无法使用super()函数
    def __init__(self, name = '', age = 20, sex = 'man'):
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)
    def setName(self, name):
        if not isinstance(name,str):
            print('name must be string.')
            return
        self.__name = name
    def setAge(self, age):
        if not isinstance(age,int):
            print('age must be integer.')
            return
        self.__age = age
    def setSex(self, sex):
        if sex != 'man' and sex != 'woman':
            print('sex must be "man" or "woman"')
            return
        self.__sex = sex
    def show(self):
        print(self.__name)
        print(self.__age)
        print(self.__sex)
class Student(Person):
    def __init__(self, name='', age = 30, sex = 'man', major = 'Computer'):
        #调用基类构造方法初始化基类的私有数据成员
        super(Student, self).__init__(name, age, sex)
        self.setMajor(major) #初始化派生类的数据成员
    def setMajor(self, major):
        if not isinstance(major, str):
            print('major must be a string.')
            return
        self.__major = major
    def show(self):
        super(Student, self).show()
        print(self.__major)
if __name__ =='__main__':
    zhangsan = Person('Zhang San', 19, 'man')
    zhangsan.show()
    lisi = Student('Li Si',32, 'man', 'Math')
    lisi.show()
'''

'''
	_xxx：这样的对象叫做保护变量，不能用'from module import *'导入，只有类对象和子类对象能访问这些变量；
	__xxx__：系统定义的特殊成员名字；
	__xxx：类中的私有成员，只有类对象自己能访问，子类对象也不能访问到这个成员，但在对象外部可以通过“对象名._类名__xxx”这样的特殊方式来访问。Python中没有纯粹的C++意义上的私有成员。

'''
#!/usr/bin/python3

def _people():
	print('what???')

class apeople():
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。体重是%s" %(self.name,self.age,self.__weight))

if __name__ == '__main__':
	a=people('wang',29,50)
	a.speak()
class Demo:
    def add(self,a,b,c=5):
        return a+b
    
obj=Demo()
# obj.add(5,7)    
print(obj.add(5,7))
print(obj.add(5,7,5))


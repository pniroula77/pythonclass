from multipledispatch import dispatch

class Addition:
    @dispatch(int,int) #decorater
    def Add(self,a,b):
        print("Interger addition")
        return a + b 

    @dispatch(int,int,int)
    def Add(self,a,b,c):
        return a + b + c

    @dispatch(float,int)
    def Add(self,a,b):
        print("float addition")
        return a + b

    @dispatch(str,str)
    def Add(self,a,b):
        return a + " " + b
    

obj = Addition()

result = obj.Add("Ram","Thapa")
print(result)
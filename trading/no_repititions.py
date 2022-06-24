
#for i in len(x):


class Onlyone:
    def __init__(self,lists,x ):
        self.arr = lists
        self.name = x
    def no_repeat(self):
        z = []
        for i in range(len(self.arr)):
            y =self.arr[i][self.name]
            z.append(y)
        return set(z)  


    # def __str__(self, lists,x):
    #     self.arr = lists

    # def no_repitions(self):
    #     for i in self.arr:

    #         x,v= x+1,self.arr[i]

    #         while x < len(self.arr):
    #             s = self.arr[x]
    #             if v == s:
    #                 self.arr.pop(x)
    #             x= x+1 

    #     return self.arr
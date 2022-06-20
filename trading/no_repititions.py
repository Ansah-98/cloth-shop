class Onlyone:
    def __str__(self, lists):
        self.arr = lists

    def no_repitions(self):
        for i in self.arr:

            x,v= x+1,self.arr[i]

            while x < len(self.arr):
                s = self.arr[x]
                if v == s:
                    self.arr.pop(x)
                x= x+1 
                
        return self.arr
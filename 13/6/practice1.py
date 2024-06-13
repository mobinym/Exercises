class Numbers:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        self.start+=3
        if self.start>self.end:
            raise StopIteration
        return self.start   

t1 = Numbers(10,100)
for item in t1:
    print (item)
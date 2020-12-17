class RightLeftCentre:

    def __init__(self,mainstring):
        self.mainstr = mainstring

    def rights(self,string,n):
        for i in range(n):
            self.mainstr = self.mainstr+string
        return self.mainstr

    def lefts(self,string,n):
        for i in range(n):
            self.mainstr =  string+self.mainstr
        return self.mainstr

    def centres(self,string,n):
        for i in range(n):
            self.mainstr = string+self.mainstr+string
        return self.mainstr

if __name__ == "__main__":
    str = 'Keshav'
    a = RightLeftCentre(str)
    print(a.centres('+-*/',5))
    print(a.lefts('=',5))
    print(a.rights('=',5))
class RightLeftCentre:

    def __init__(self,mainstring):
        self.mainstr = mainstring

    def lefts(self,string,n):
        string*=n
        return string+self.mainstr

    def rights(self,string,n):
        string*=n
        return self.mainstr+string

    def centres(self,string,n):
        string*=n
        return string+self.mainstr+string

if __name__ == "__main__":
    str = 'Keshav'
    a = RightLeftCentre(str)
    print(a.centres('+-*/',5))
    print(a.lefts('=',5))
    print(a.rights('=',5))
    print(a.centres('=',2))
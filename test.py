def baz(a):
    def biz(i):
        def buz(u):
            return a+i-u
        return buz(i/2)
    return biz(a*3)

print(baz(4))
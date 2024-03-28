class StudentsClass:
    def __init__(self, fname, lname, age) -> None:
        self.fname = fname,
        self.llname = lname,
        self.age  = age

    def __init__(self) -> None:
        pass


    def test_fun(self):
        print("this is test fun")

def greet(fn):
    def mfn():
        print("gud morning")
        fn()
        print("Thanks")
    return mfn

@greet
def hello():
    print("Hello world")

hello()

greet(hello)


class staticvar:
    static_variable = 0
    def __init__(self, name) -> str:
        self.static_variable = name

    def fun(self, sname) -> str:
        return 20

a = staticvar("nnnn")
print(a.static_variable)
b = staticvar("mmmmm")

print(a.static_variable)
print(b.static_variable)
print(staticvar.static_variable)

print(a.fun("yyyyy"))

#print(dir(str))
#print(help(staticvar))

print(a.__dict__)

#print(staticvar)
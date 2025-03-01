def greet():
    print("hello")
def foo():
    print("foo foo")
def bar (f):
    f()

bar(greet)
bar(foo)
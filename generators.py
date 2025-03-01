#nestedfunctions
#def foo():
 #   def bar():
  #      print("bar bar")
   # return bar

#f=foo()
#f()
#or foo()()


def makeadder(a):
    def add(b):
        nonlocal a
        a+=1
        return a+b

    return add

#f=makeadder(5)
#print(f(4))
#print(f(5))
#print(f(6))
#print(f(10))
print(makeadder(10)(2))
num=[1,2,3,4]
def inc(num):
    num+=[10] 
    print(f"inside{num}")
inc(num)
print(f"outside{num}")
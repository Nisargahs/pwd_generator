digits=[294304,34324,32442,234,435]
largest_so_far= 10000000
print('before',largest_so_far)
for num in digits:
    if num < largest_so_far:
        largest_so_far = num
    
print ('after',largest_so_far)
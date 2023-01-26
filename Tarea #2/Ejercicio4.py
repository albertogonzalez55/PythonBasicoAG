from random import randint
nums_random=[randint(1,10)for _ in range(10)]

print (nums_random)

nums_alcubo = [n**3 for n in nums_random]
print (nums_alcubo)

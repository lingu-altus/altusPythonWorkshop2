
ten = 10


# 1. Pure Functions 
def addTen(input):
	return input + 10

print(addTen(10))
print(addTen(10))
print(addTen(10))
print(addTen(10))

# 2. Immutability

original_list = [1,2,3]
# .map() .filter() .reduce() 

def increment_items(items, increment):
	return [item + increment for item in items]

new_list = increment_items(original_list, 5)

print(original_list)
print(new_list)

# 3. First class functions

def declareAndUseFunction(func, input):
	print("I'm going to invoke your function now!")
	print(func(input))

declareAndUseFunction(addTen, 9)

add10 = addTen

print(add10(4))

add5 = lambda x: x + 5


# Benefits
# 1. Easy to reason
# 2. More predictable - easier to test
# 3. Concurrency-friendly
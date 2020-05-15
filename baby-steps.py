print('Hello World!')


print() # print a break line

data_to_print = input('Insert data: ')
print(data_to_print)


print() # print a break line

name = 'John'
surname = 'Doe'
full_name = name + ' ' + surname # concat strings!
print(full_name)

print() # print a break line


number = 18
if (number >= 18):
	print('The number is equal or greater than 18')
	print('🙂')
else:
	print('You are a child')

print() # print a break line


def sum(n, m):
	"This is the documentation of the function"
	return n + m

print(sum(3,4))


print() # print a break line

# Function definition is here
def printinfo(name, age = 35):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age ", age)
   return

# Now you can call printinfo function
printinfo(age = 42, name = "Lola")

print() # print a break line

paco = 'paco'
printinfo(paco)


print() # print a break line

def iterate(*data_list):
	for data in data_list:
		print(data.upper()) # print to uppercase
	return

iterate('apple', 'banana', 'watermelon')

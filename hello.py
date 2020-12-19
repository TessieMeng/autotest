print(1)

a1 = 3
a2 = "hello world"
a3 = 100+34
print(a3)

print("hello world")
print("good \n evening")
print('''hello

world''')
print("123"+"456")
print("o"*6)

str1 = "a b c d e"
print(str1[0])
print(str1[-1])

str2 = "my name is mts"
print(str2[-3:0])   # string[first:last+1]
print(str2[:0])

len(str2)

# list
a = [1,"a","1.2",["12","13"]]
print(a[3][0])

a[3][0] = "new"  # element can be changed
print(a)

# tuple：similar to list，but cannot change the element
b = ("t","u","p","l","e")

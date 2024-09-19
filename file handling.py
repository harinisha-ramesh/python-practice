# file opening  
file = open('sample.txt','r') 

# READ
# read()---> to read the entire file
file = open("sample.txt", "r")
content = file.read()  # Read entire file
print(content)
file.close()  

# readline() ----> to read the file line by line
file = open("sample.txt", "r")
print(file.readline())
print(file.readline())

# readlines() ----> to read all lines in a file
file = open("sample.txt", "r")
print(file.readlines())


#WRITE
file = open("sample.txt",'w')
file.write("This is the starting.\n")
file.close()

#APPEND
file = open("sample.txt", "a")
file.write("This is an appended line.\n")  # Append a line to the file
file.close()
  
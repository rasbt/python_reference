# Different methods to read from text files
# sr 11/18/2013
# Python 3.x

# Note: rb opens file in binary mode to avoid issues with Windows systems
# where '\r\n' is used instead of '\n' as newline character(s).


# A) Reading in Byte chunks
reader_a = open("file.txt", "rb")
chunks = []
data = reader_a.read(64)  # reads first 64 bytes
while data != "":
    chunks.append(data)
    data = reader_a.read(64)
if data:
    chunks.append(data)
print (len(chunks))
reader_a.close()


# B) Reading whole file at once into a list of lines
with open("file.txt", "rb") as reader_b:   # recommended syntax, auto closes
    data = reader_b.readlines() # data is assigned a list of lines
print (len(data))


# C) Reading whole file at once into a string
with open("file.txt", "rb") as reader_c:
    data = reader_c.read() # data is assigned a list of lines
print (len(data))


# D) Reading line by line into a list
data = []
with open("file.txt", "rb") as reader_d:
    for line in reader_d:
        data.append(line)
print (len(data))






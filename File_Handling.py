f=open('Index.txt')
print(f.read())

f=open('Index.txt','w')
f.write('I am a Coder Pro Max')
f.close

f=open('Index.txt')
print(f.read())

f=open('Index.txt','a')
f.write(' But weak in DSA')
f.close

f=open('Index.txt')
print(f.read())

f=open('Index.txt')
print(f.read(5))
print(f.read(5))
print(f.tell())
print(f.seek(0))
print(f.seek(15))
print(f.read(5))

f.seek(0)
for line in f:
 print(line)


f=open('Index.txt')
f.readline()

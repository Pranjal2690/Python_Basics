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
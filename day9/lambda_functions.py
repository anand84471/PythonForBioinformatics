x=lambda a:a+5

y=lambda a,b:a+b

print(x(5))
print(y(3,4))


get_length=lambda seq:len(seq)
print(get_length("ATGCTGATAGAATG"))


z=lambda a,b,c:a+b+c+4
print(z(1,2,3))


z=lambda a,b=5:a+b

print(z(1,2))
print(z(1))



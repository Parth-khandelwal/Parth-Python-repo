a=int(input('enter amount:'))
b=int(input('enter tax perecentage'))
c=int(input('enter tenure(in years)'))
tax=(a*b)/100
total=tax*c
net=a+total
print(total,'- this amount includes total tax till the tenure ')
print(net,'-This includes total amount including taxesa')

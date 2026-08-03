#str list tuple set dict range()
'''
for var in seq:
    print(var)

'''
'''
s='Codegnan'
for ch in s:
    if ch in 'aeiouAEIOU':
        print(ch)
'''

'''
l = [10,23,30,45,1,3,15,16,18,19,21]
for i in l:
    if i%2==0:
        print(i,"Even")
    else:
        print(i,"Odd")
'''

'''
marks = (90,20,35,46,78,92,87,48)
for mark in marks:
    if mark>35:
        print(mark,"pass")
    else:
        print(mark,"fail")
'''
'''
followers = {'dhana','dimple','subb','charan'}
for i in followers:
    print(i)
'''
'''
bus = {'s1':'Booked','s2':'Available','s3':'Availbale','s4':'Booked','s5':'Available'}
for seat in bus:
    if bus.get(seat) == 'Available':
        print(seat,bus.get(seat))
        '''
#range(start,enf+1,step) => (0,nodef,1)
for i in range(1,11):
    print(i)
for i in range(2,51,2):
    print(i,end=' ')
for i in range(1,100,2):
    print(i,end='')
for i in range(5,51,5):
    print(i)
n = int(input("Enter the table no: "))
for i in range(1,11):
    print(f'{n}*{i}={n*i}')



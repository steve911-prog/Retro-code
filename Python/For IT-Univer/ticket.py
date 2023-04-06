''''123456' - '123'      '456'
                    list('123') = ['1', '2', '3']
                    [int(i) for i in list('123')] = ['1', '2', '3']
                    '''

e = int(input( 'Entry num of first ticket '))
b = int(input('Entry num of last ticket '))
count = 0

def chek(ij):
    global count
    ij = str(ij).zfill(6)
    b1 = ij[:3]
    b2 = ij[3:]
    b1 = [int(i) for i in list(b1)]
    b2 = [int(i) for i in list(b2)]
    if sum(b1) == sum(b2):
        print(ij)
for i in range(e,b):
    check(i)      
count += 1
#print('lucky tickets - ' , str(count))

#print(i)
for i in range(e,b):
    check(i)


#begin = '123456'
#



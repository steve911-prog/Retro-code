begin = input("Введите номер первого билетика ") #006789
end = input("Введите номер последнего билетика ")#123789 
count = 0

def check(bil):
    global count                #"006789" -> 6789 -> "006789"
    bil = str(bil).zfill(6)      
    b1 = bil[:3]                # "006"
    b2 = bil[3:]                # "789"
    b1 = [int(i) for i in list(b1)]
    b2 = [int(i) for i in list(b2)]
    if sum(b1) == sum(b2) :
        print(bil)
        count += 1
        
for bilet in range(int(begin), int(end) + 1):
    check(bilet)

print("счастливых билетиков - ", count)

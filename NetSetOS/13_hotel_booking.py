# Hotel bookings Possible

arrival = [1, 3, 5]
depart = [2, 6, 8]

final = [(i, 'RED') for i in arrival] + [(j, "BLUE") for j in depart]
final.sort()
print(final)

rooms = 1
guest = 0
flag = True
for i in final:
    if i[1] == 'RED':
        guest += 1
        if guest > rooms:
            flag = False
            break
    elif i[1] == 'BLUE':
        guest -= 1

if flag:
    print("Success")
else:
    print("Error!!!")

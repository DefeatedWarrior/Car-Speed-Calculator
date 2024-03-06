nr = 0
dist = 30

with open('data.csv', 'w') as file:
    file.write("#,Time,Speed (KM/H),Speed (M/S),Distance,Type")
    file.close()

def Ask_Questions(nr):
    times = input("Time: ")
    if times == "exit":
        file.close()
        exit()
    else:
        times = int(times)

    car_type = input("Car Type: ")
    nr = nr + 1
    CSV_Add_Line(times, car_type, nr, dist)

def CSV_Add_Line(t, name, nr, dist):
    s = dist/t
    km = str(s * 3.6)
    with open('data.csv', 'a') as file:
        file.write("\n"+ str(nr) + "," + str(t) + "," + km + "," + str(s) + "," + str(dist) + "," + name + ",")
        Ask_Questions(nr)

Ask_Questions(nr)
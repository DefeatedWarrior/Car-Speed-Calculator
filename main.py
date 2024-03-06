
with open('data.csv', 'w') as file:
    file.write("#,Time,Speed,Distance,Type")
    file.close()

def Ask_Questions():
    times = input("Time: ")
    car_type = input("Car Type: ")
    CSV_Add_Line(times, car_type)

def CSV_Add_Line(t, name):
    with open('data.csv', 'a') as file:
        file.write()

Ask_Questions()
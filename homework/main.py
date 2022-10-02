from models.models import Toyota

while True:
    print("0. Exit\n" +
          "1. Add new car\n" +
          "2. Get all cars\n" +
          "3. Get car from id\n" +
          "4. Change color\n" +
          "5. Shift gears"
        )

    flag = int(input('Choose menu item: '))

    if flag == 1:
        name = input("Car name: ")
        engine = input("Type engine: ")
        color = input("Color: ")
        gear = input("Num of gears: ")
        car = Toyota(name, engine, color, gear)
        car.save()
    elif flag == 2:
        Toyota.get_all_cars()
    elif flag == 3:
        id = int(input("Type id to search: "))
        Toyota.get_by_id(id)
    elif flag == 4:
        id = int(input("Type id to search and change color: "))
        Toyota.new_color(id)
    elif flag == 5:
        id = int(input('Type id to search and to drive car: '))
        Toyota.shift_gear(id)
    elif flag == 0:
        print("Exit the app")
        break
    

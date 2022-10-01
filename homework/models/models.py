from hashlib import new
import json

class Toyota:
    file = 'cars.json'

    def __init__(self, name, engine, color, gear):
        self.name = name
        self.engine = engine
        self.color = color
        self.gear = gear

    

    @classmethod
    def get_data(cls):
        file = open('databases/' + cls.file, 'r')
        data_in_json = file.read()
        data = json.loads(data_in_json)
        file.close()
        return data

    @classmethod
    def get_all_cars(cls):
        data = cls.get_data()
        for car in data:
            print('Name:', car["name"])
            print('Engine:', car["engine"])
            print('Color:', car["color"])
            print('Gear:', car["gear"])

    @classmethod
    def get_by_id(cls, id):
        data = cls.get_data()
        counter = 0
        for car in data:
            if id == car['id']:
                print(car["name"])
                print(car["engine"])
                print(car["color"])
                print(car["gear"])
                break
            counter += 1
            if counter == len(data):
                print('Not found car with this id')

    @classmethod
    def new_color(cls, id):
        count = 0
        newcols = cls.get_data()
        for newcol in newcols:
            if id == newcol['id']:
                print(newcol["color"])
                new_obj = input("New color: ")
                newcol["color"] = new_obj
                print('new color: ', newcol["color"])
                break
            count+=1
            if count == len(newcols):
                print('Not found car with this id')
        file = open("databases/" + cls.file, "w")
        data_in_json = json.dumps(newcols)
        file.write(data_in_json)

    @classmethod
    def shift_gear(cls, id):
        data = cls.get_data()
        count = 0
        for car in data:
            if id == car['id']:
                gear = 0
                while gear == 0 or gear > int(car['gear']):
                    gear = int(input('Choose gear:'))
                    if gear > int(car['gear']):
                        print('Car has no gear ' + str(gear) + ' gears')
                    elif gear == 0:
                        print('you`re not moving anywhere')
                print('Start drive!')
                while 0 < gear and gear <= int(car['gear']):
                    print('You enter ' + str(gear) + ' gear')
                    gear = int(input('Next your gear '))
                if gear == 0:
                    print('car stopped.')
                else:
                    print('accident')
                break
            count += 1
            if count == len(data):
                print('Not found car with this id')



    def save(self):
        data = self.get_data()
        new_car = {'name': self.name, 'engine': self.engine, 'color': self.color, 'gear': self.gear}
        if len(data) == 0:
            new_car['id'] = data[-1]['id'] + 1
        else:
            new_car['id'] = 1
        data.append(new_car)
        file = open('databases/' + self.file, 'w')
        data_in_json = json.dumps(data)
        file.write(data_in_json)
        file.close()
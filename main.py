class Car:
    def __init__(self, brend, model, production_year, color, horse_power, is_sport_car=False):
        self.__brand = brend
        self.__model = model
        self.__production_year = production_year
        self.__color = color
        self.__horse_power = horse_power
        self.__is_sport_car = is_sport_car


    def get_brand(self):
        return self.__brand
    
    def get_model(self):
        return self.__model
    
    def get_production_year(self):
        return self.__production_year
    
    def get_color(self):
        return self.__color
    
    def get_horse_power(self):
        return self.__horse_power
    
    def get_is_sport_car(self):
        return self.__is_sport_car
    

    def change_color(self, new_color):
        if self.__color != new_color:
            self.__color = new_color
            return True
        return False
    
    def increase_horse_power(self, hp):
        if hp > 0:
            self.__horse_power +=hp
            return True
        return False
    

toyota_car = Car(brend='Toyota', model='corolla', production_year=2022, color='white', horse_power=139)   

# print(f"Toyota_car - brand:{toyota_car.get_brand()}")
# print(f"Toyota_car - model:{toyota_car.get_model()}")
# print(f"Toyota_car - production_year:{toyota_car.get_production_year()}")
# print(f"Toyota_car - color:{toyota_car.get_color()}")
# print(f"Toyota_car - horse_power:{toyota_car.get_horse_power()}")
# print(f"Toyota car - is_sport_car:{toyota_car.get_is_sport_car()}")


toyota_car_change_color = toyota_car.change_color("red")
# print(toyota_car_change_color)
# print(toyota_car.get_color())

# toyota_car_change_color = toyota_car.change_color("red")
# print(toyota_car_change_color)

toyota_car_increase_hp = toyota_car.increase_horse_power(65)
print(toyota_car_increase_hp)
print(toyota_car.get_horse_power())

# toyota_car_increase_hp = toyota_car.increase_horse_power(-40)
# print(toyota_car_increase_hp)
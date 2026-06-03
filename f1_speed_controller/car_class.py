class Car:
    def __init__(self, year_model, make, top_speed):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
        self.__top_speed = top_speed
    def accelerate(self):
        self.__speed += 5
    def brake(self):
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0
    def get_speed(self):
        return self.__speed
    
    if __name__ == "__main__":
        my_car = Car("2026", "Red Bull Racing RB20")
        my_car.brake()
        print(f"Speed after braking: {my_car.get_speed()}") # This will print -5!
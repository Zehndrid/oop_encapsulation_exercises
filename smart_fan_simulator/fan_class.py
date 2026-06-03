class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        self.__speed = speed
        self.__radius = float(radius)
        self.__color = color
        self.__on = on

    def get_speed(self): return self.__speed
    def set_speed(self, speed): self.__speed = speed
    def get_on(self): return self.__on
    def set_on(self, on): self.__on = on
    def get_color(self): return self.__color
    def set_color(self, color): self.__color = color
    def get_radius(self): return self.__radius

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = float(radius)
        else:
            self.__radius = 5.0 # Fallback to default

if __name__ == "__main__":
    fan1 =Fan(speed=Fan.FAST, radius=10.0, color="yellow", on=True)
    fan2 = Fan(speed=Fan.MEDIUM, radius=5.0, color="blue", on=False)
   
    print(f"Fan 1 -> Speed: {fan1.get_speed()}, Color: {fan1.get_color()}, On: {fan1.get_on()}")
    print(f"Fan 2 -> Speed: {fan2.get_speed()}, Color: {fan2.get_color()}, On: {fan2.get_on()}")
class Pet:
    def __init__(self, name="", animal_type="", age=0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name): self.__name = name
    def set_animal_type(self, animal_type): self.__animal_type = animal_type

    def get_name(self): return self.__name
    def get_animal_type(self): return self.__animal_type
    def get_age(self): return self.__age

if __name__ == "__main__":
    print("--- Pet Registration ---")
    user_name = input("Enter name: ")
    user_type = input("Enter type: ")
    user_age = int(input("Enter age: "))

    my_pet = Pet()
    my_pet.set_name(user_name)
    my_pet.set_animal_type(user_type)
    my_pet.set_age(user_age)

    print(f"Name: {my_pet.get_name()}")
    print(f"Type: {my_pet.get_animal_type()}")
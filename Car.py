# Program # 2: Car Class
# Write a class named Car that has the following data attributes:

# __year_model (for the car's year model)
# __make (for the make of the car)
# __speed (for the car's current speed)
# The Car class should have an __init__ method that accepts the car's year model and make as arguments.  These values should be assigned to the object's __year_model and __make data attributes.  It should also assign 0 to the __speed data attribute.

# The class should also have the following methods:

# The accelerate method should add 5 to the speed data attribute each time it it called.
# The brake method should subtract 5 from the speed data attribute each time it is called.
# The get_speed method should return the current speed.
# Next, design a program that creates a Car object then calls the accelerate method five times.  After each call to the accelerate method, get the current speed of the car and display it.  The call the brake method.  After each call to the brake method, get the current speed of the car and display it.

class Car:
    def __init__(self, year_model, make):
        # Initializing the data attributes
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0  # Initial speed is 0

    def accelerate(self):
        # Increase speed by 5 each time this method is called
        self.__speed += 5

    def brake(self):
        # Decrease speed by 5 each time this method is called
        self.__speed -= 5

    def get_speed(self):
        # Return the current speed
        return self.__speed


# Main program to create a Car object and test the methods
def main():
    # Create a Car object
    car = Car(2023, "Toyota")

    # Accelerate the car 5 times
    print("Accelerating the car:")
    for _ in range(5):
        car.accelerate()
        print(f"Current speed: {car.get_speed()} mph")

    # Brake the car 5 times
    print("\nBraking the car:")
    for _ in range(5):
        car.brake()
        print(f"Current speed: {car.get_speed()} mph")

# Call the main function to run the program
if __name__ == "__main__":
    main()

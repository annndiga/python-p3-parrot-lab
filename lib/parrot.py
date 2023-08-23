def parrot(argument=None):
    if argument is not None:
        print(argument)
        return argument
    else:
        print("Squawk!")
        return "Squawk!"

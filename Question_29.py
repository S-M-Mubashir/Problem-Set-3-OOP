def makeFancy(func):
    def wrapper():
        print("*"*20)
        func()
        print("*"*20)
        print("*"*15)
        print("*"*10)
    return wrapper

class FancyPrint:
    message = " "

    def set_message(self, value):
        FancyPrint.message = value

    @makeFancy
    def fancyprint():
        print(FancyPrint.message.upper())


F = FancyPrint()
F.set_message("Congratulations!")
FancyPrint.fancyprint()

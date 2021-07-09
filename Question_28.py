class FancyPrint:
    message = " "

    def set_message(self, value):
        FancyPrint.message = value

    @staticmethod
    def fancyprint():
        print(FancyPrint.message.upper())


F = FancyPrint()
F.set_message("Congratulations!")
FancyPrint.fancyprint()

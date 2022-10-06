# from ctypes import addressof
from turtle import Turtle

# ALIGNMENT = "left"
FONT = ("Arial", 50, "bold")


class Wallet(Turtle):
    def __init__(self, address, balance):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write(f"")
        self.address = address
        self.balance = balance

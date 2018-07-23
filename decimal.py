from decimal import Decimal

def generator_liczb_decimal():
   a = 2.0
   while a <= 5.5:
       print(Decimal(a))
       a = a + 0.5

generator_liczb_decimal()
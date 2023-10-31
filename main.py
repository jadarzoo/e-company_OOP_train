from foydalanuvchilar import *
from maxsulotlar import *
from buyurtmalar import *


# E-commerce platformasini sinovdan o'tkazish
mijoz = Mijoz(1, "Ahmadullo Jo'rayev", "ahmadulloj@elektron.pochta", "parol123", "123 Asosiy ko'cha")
sotuvchi = Sotuvchi(2, "Eng sotuvchi", "sotuvchi@elektron.pochta", "sotuvchiparol", "XYZ Bank")
maxsulot = Maxsulot(101, "Ajoyib Maxsulot", 49.99)

savatcha = mijoz._savatcha
savatcha.maxsulot_qoshish(maxsulot, 2)

buyurtma = Buyurtma(1, mijoz, KreditKartaTolov("1234 5678 9012 3456", "12/25", "123"), StandartYetkazibBerish())
buyurtma.element_qoshish(maxsulot, 2)

mijoz.buyurtma_qilish(buyurtma)
sotuvchi.buyurtma_qilish(buyurtma)

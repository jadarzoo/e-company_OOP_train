from abc import ABC, abstractmethod


class Buyurtma:
    def __init__(self, buyurtma_id, mijoz, tolov_metodi, yetkazib_berish_metodi):
        self._buyurtma_id = buyurtma_id
        self._mijoz = mijoz
        self._tolov_metodi = tolov_metodi
        self._yetkazib_berish_metodi = yetkazib_berish_metodi
        self._elementlar = []

    def element_qoshish(self, maxsulot, miqdori):
        self._elementlar.append((maxsulot, miqdori))

    def umumiy_summa(self):
        umumiy_summa = 0
        for maxsulot, miqdori in self._elementlar:
            umumiy_summa += maxsulot.narxni_olish() * miqdori
        return umumiy_summa

    def tolov_metodi(self):
        return self._tolov_metodi

    def yetkazib_berish_metodi(self):
        return self._yetkazib_berish_metodi


class Tolov(ABC):

    @abstractmethod
    def tolov_qilish(self, summa):
        pass


class KreditKartaTolov(Tolov):
    def __init__(self, karta_raqami, amal_qilish_muddati, cvv):
        self._karta_raqami = karta_raqami
        self._amal_qilish_muddati = amal_qilish_muddati
        self._cvv = cvv

    def tolov_qilish(self, summa):
        print(f"{summa} dollarni kredit kartasi bilan to'lov qilindi.")


class PayPalTolov(Tolov):
    def __init__(self, email, parol):
        self._email = email
        self._parol = parol

    def tolov_qilish(self, summa):
        print(f"{summa} dollarni PayPal orqali to'lov qilindi.")


class YetkazibBerish(ABC):
    @abstractmethod
    def yetkazib_berish(self, buyurtma, manzil):
        pass


class StandartYetkazibBerish(YetkazibBerish):
    def yetkazib_berish(self, buyurtma, manzil):
        print(f"{manzil} manziliga standart yetkazib berish amalga oshirildi.")


class ExpressYetkazibBerish(YetkazibBerish):
    def yetkazib_berish(self, buyurtma, manzil):
        print(f"{manzil} manziliga express yetkazib berish amalga oshirildi.")

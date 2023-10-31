from abc import ABC, abstractmethod
from maxsulotlar import Savatcha

class Foydalanuvchi(ABC):
    def __init__(self, user_id, ism, email, parol):
        self._user_id = user_id
        self._ism = ism
        self._email = email
        self._parol = parol

    @abstractmethod
    def buyurtma_qilish(self, buyurtma):
        pass

class Mijoz(Foydalanuvchi):
    def __init__(self, user_id, ism, email, parol, manzil):
        super().__init__(user_id, ism, email, parol)
        self._manzil = manzil
        self._savatcha = Savatcha()

    def buyurtma_qilish(self, buyurtma):
        tolov = buyurtma.tolov_metodi()
        yetkazib_berish = buyurtma.yetkazib_berish_metodi()

        tolov.tolov_qilish(buyurtma.umumiy_summa())
        yetkazib_berish.yetkazib_berish(buyurtma, self._manzil)

class Sotuvchi(Foydalanuvchi):
    def __init__(self, user_id, ism, email, parol, bank_hisobi):
        super().__init__(user_id, ism, email, parol)
        self._bank_hisobi = bank_hisobi
        self._maxsulotlar = []

    def buyurtma_qilish(self, buyurtma):
        try:
            tolov = buyurtma.tolov_metodi()
            umumiy_summa = buyurtma.umumiy_summa()
            self._bank_hisobi.tolov_qabul(umumiy_summa)
        except AttributeError:
            pass


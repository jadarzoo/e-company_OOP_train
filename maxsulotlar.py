class Maxsulot:
    def __init__(self, maxsulot_id, nom, narx):
        self._maxsulot_id = maxsulot_id
        self._nom = nom
        self._narx = narx

    def narxni_olish(self):
        return self._narx

class Savatcha:
    def __init__(self):
        self._elementlar = []

    def maxsulot_qoshish(self, maxsulot, miqdori):
        self._elementlar.append((maxsulot, miqdori))

    def umumiy_summa_hisoblash(self):
        umumiy_summa = 0
        for maxsulot, miqdori in self._elementlar:
            umumiy_summa += maxsulot.narxni_olish() * miqdori
        return umumiy_summa
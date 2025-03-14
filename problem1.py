import os

class WorkWithFiles:
    def __init__(self, katalog):
        self.katalog = katalog
        self.files = os.listdir(katalog)

    def __str__(self):
        papkalar = []
        for i in self.files:
            if os.path.isdir(os.path.join(self.katalog, i)):
                papkalar.append(i)
                
        fayllar = []
        for i in self.files:
            if os.path.isfile(os.path.join(self.katalog, i)):
                fayllar.append(i)

        natija = f"Katalogda {len(papkalar)} ta papka va {len(fayllar)} ta fayl bor.\n"
        natija += f"Papkalar: {', '.join(papkalar)}\n"
        natija += f"Fayllar: {', '.join(fayllar)}"
        
        return natija

    def count_papka(self):
        count = 0
        for i in self.files:
            if os.path.isdir(os.path.join(self.katalog, i)):
                count += 1
        return count
    
    def count_file(self):
        count = 0
        for i in self.files:
            if os.path.isfile(os.path.join(self.katalog, i)):
                count += 1
        return count

    def fayl_qidirish(self, fayl_nomi):
        for fayl in self.files:
            if fayl == fayl_nomi:
                return f"Bu txt fayl mavjud: {fayl}"
        return "Fayl topilmadi."


class ChildClass(WorkWithFiles):
    def __init__(self, katalog):
        super().__init__(katalog)
        self.fayllar = self.matn_file()

    def matn_file(self):
        natija = []
        for fayl in self.files:
            if fayl.endswith('.txt'):
                natija.append(fayl)
        return natija
    


txt_file = ChildClass("D:\\python najot talim\\fayllar bilan i shlash\\uyga vazifa")
print(txt_file)
print(txt_file.fayl_qidirish("result.txt"))

#6-misol
class Ishchi:
    def __init__(self, ism, maosh):
        self.ism = ism
        self.maosh = maosh

    def ishlash(self):
        print("Ishlamoqda")


class Dasturchi(Ishchi):
    def ishlash(self):
        print("Kod yozmoqda")


# 1 obyekt
d1 = Dasturchi("Ali", 5000)
d1.ishlash()

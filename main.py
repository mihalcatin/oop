# class MojaKalkulacka:
#     @staticmethod
#     def sucet (a, b):
#         return a + b
#
#     @staticmethod
#     def sucin(a, b):
#         return a*b
#
#
# print(MojaKalkulacka.sucet(2, 2))
# print(MojaKalkulacka.sucin(2, 3))
#
#
# class Zviera:
#     def hlas(self):
#         raise NotImplementedError("Podtrieda musí implementovať metódu")
#
# class Pes(Zviera):
#     def hlas(self):
#         return "HAF"
#
# class Kohut(Zviera):
#     def hlas(self):
#         return "KODKODAK"
#
#
# class Macka(Zviera):
#     def hlas(self):
#         return "MNAU"
#
# def vydaj_zvuk(Zviera):
#     return Zviera.hlas()

#
# class Zviera:
#     def hlas(self):
#         raise NotImplementedError("Podtrieda musí implementovať metódu")
#
#
# class Kohut(Zviera):
#     def nohy(self):
#         return "2"
#
# class Pes(Zviera):
#     def nohy(self):
#         return "4"
#
# class Macka(Zviera):
#     def nohy(self):
#         return "4"
#
# pes = Pes()
# macka = Macka()
# kohut = Kohut()
#
# for zviera in [pes, macka, kohut]:
#     print(zviera.nohy())
#
# class Pes():
#     def hlas(self):
#         return "haf"
#
# class Kohut():
#     def hlas(self):
#         return "KODKODAK"
#
# class Macka():
#     def hlas(self):
#         return "MNAu"
#
# def vydaj_zvuk(zviera):
#     return zviera.hlas()
#
# pes = Pes()
# macka = Macka()
# kohut = Kohut()
#
#
# for zviera in [pes, macka, kohut]:
#     print(zviera.hlas())



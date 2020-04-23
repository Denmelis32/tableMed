class TabletMed:

    def __init__(self):
        pass

    def initialization(self, tableDate, tabletWeight, numberPills, nameMed):
        self.tabletDate = tableDate
        self.tabletWeight = tabletWeight
        self.numberPills = numberPills
        self.nameMed = nameMed

    def read(self):
        self.tabletDate = int(input("Срок годности таблетки "))
        self.tabletWeight = int(input("Вес одной таблетки "))
        self.numberPills = int(input("Количество таблеток в упаковке "))
        self.nameMed = input("Наименования лекарства ")

    def display(self):
        print(self.nameMed + " Название таблетки, " + str(self.numberPills) +
              " Количество таблеток, " + str(self.tabletWeight) + " Вес одной таблетки, " +
              str(self.tabletDate) + " Срок годности ")


class Med:

    def add(self, arg1, arg2):
        F = TabletMed()
        number = (arg1.numberPills + arg2.numberPills) / 2
        if arg1.tabletWeight < arg2.tabletWeight:
            weight = arg1.tabletWeight
        else:
            weight = arg2.tabletWeight

        F.initialization(arg2.tabletDate, weight, number, arg1.nameMed)
        return F


C = TabletMed()
C.read()
C.display()
D = TabletMed()
D.read()
D.display()
apteka = Med()
apteka.add(C, D)
itemsMed = []
itemsMed.append(C)
itemsMed.append(D)
weight = int(input("Заданное значение, с которым будете сравнивать "))
counts = int(input("Количество лекарств "))
for i in range(counts):
    itemsMed.append(apteka.add(itemsMed[(len(itemsMed) - 1)], itemsMed[len(itemsMed) - 2]))

for f in range(len(itemsMed)):
    sum = itemsMed[f].numberPills * itemsMed[f].tabletWeight

if sum > weight:
    print(round(sum, 1))

#x = (input("Wie ist dein Name?:"))
#print("Hallo", x)
euro = float(input("Wieviel € sollen umgerechnet werden?:"))
dollar = round(euro*1.09, 2)
print("Der Wechselkurs beträgt", dollar, "$")

def doppel():
    x=int(input("Bitte geben Sie eine Zahl ein: "))
    y=2*x
    print("Das Doppelte Ihrer Zahl ist:",y)
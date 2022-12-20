import calc


nr1 = int(input("Geef een eerste nummer: "))
nr2 = int(input("Geef een tweede nummer: "))
methode = input("Wil je + of -? (+/-) ")

if methode == "-":
    print(calc.subtract(nr1, nr2))
elif methode == "+":
    print(calc.add(nr1, nr2))
else:
    print("Dat kan ik niet, ", methode)
1
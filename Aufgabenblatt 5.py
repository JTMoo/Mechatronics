# 1 Schreibe ein Programm, das alle Zahlen zwischen 1 und der einer vom Benutzer definierten Zahl (input) ausgibt.
#   Achtung: Fehlerfaelle beruecksichtigen (Bedingungen)

# 2 Schreibe ein Programm, das alle Primzahlen zwischen 1 und 1000 ausgibt.
#   Primzahlen sind so definiert, dass sie nur durch sich selbst und 1 teilbar sind. Beispiel: 1, 2, 3, 5, 7 ....

# 3 Schreibe ein Programm, das alle Zeichen eines Benutzer-definierten (input) strings (Bedingung) in jeweils einer Zeile ausgibt.




#aufg.1
Zahl = input("Gebe eine Zahl aus. \n")

if Zahl == 0:
    print ("Das sollte eine Zahl sein.")
else:
    print("Gut.")


zahlen = range(1,(int(Zahl)))

for numbers in zahlen:
    print(int(numbers))

pause = "     "
print(pause)

#aufg.2
primzahlen = [1,2, 3, 5 ,7 ,11 ,13 ,17 ,19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157 ,163 ,167, 173, 179, 181, 191, 193, 197 ,199 ,211 ,223 ,227, 229 ,233 ,239 ,241, 251 ,257 ,263 ,269, 271, 277 ,281 ,283 ,293 ,307 ,311 ,313, 317 ,331 ,337, 347 ,349 ,353 ,359 ,367 ,373 ,379 ,383 ,389 ,397 ,401 ,409 ,419 ,421 ,431 ,433 ,439 ,443 ,449 ,457 ,461 ,463, 467 ,479 ,487 ,491 ,499 ,503 ,509 ,521 ,523 ,541, 547 ,557 ,563, 569, 571, 577, 587, 593, 599, 601, 607, 613 ,617, 619 ,631 ,641 ,643, 647 ,653, 659 ,661 ,673 ,677 ,683 ,691, 701, 709 ,719 ,727 ,733 ,739 ,743, 751 ,757, 761, 769 ,773 ,787 ,797, 809 ,811 ,821 ,823, 827, 829, 839 ,853, 857, 859 ,863, 877 ,881, 883, 887, 907, 911 ,919, 929 ,937 ,941, 947, 953, 967, 971, 977, 983, 991, 997]

for dieobenda in primzahlen:
    print(dieobenda)


#aufg.3
Benutzer_Eingabe = input("Gebe irgend welche Charaktere ein: \n") #???????????????????????????????????????????????????????????????

for irgendwas in Benutzer_Eingabe:
    print(irgendwas)


 

numberToCheck = 15

if numberToCheck > 1:
	for i in range(2, int(numberToCheck / 2) + 1):
		if (numberToCheck % i) == 0:
			print(numberToCheck, "ist keine Primzahl")
			break
	else:
		print(numberToCheck, "ist eine Primzahl")
else:
	print(numberToCheck, "ist keine Primzahl")
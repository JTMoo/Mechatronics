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

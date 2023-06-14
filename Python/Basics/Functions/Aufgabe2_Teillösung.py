# Prinzipiell soll eine Funktion erstellt werden, die eine Überprüfung macht.
# Überprüfung bedeutet if/else und ein return (Rückgabeparameter) eines bools.
# Beispiel mit dem Operator Modulo (%)
def Ist_Restlos_Durch_2_Teilbar(numberToCheck):
  if numberToCheck % 2 == 0:
    return True
  else:
    return False
  
num1 = 1
num2 = 2
num3 = 20
num4 = 21

print(Ist_Restlos_Durch_2_Teilbar(num1))
print(Ist_Restlos_Durch_2_Teilbar(num2))
print(Ist_Restlos_Durch_2_Teilbar(num3))
print(Ist_Restlos_Durch_2_Teilbar(num4))

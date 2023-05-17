def function1(var1):
  if var1 == 99:
    return
  
  function1(var1+1)
  print(var1)
  
var2 = 0
function1(var2)

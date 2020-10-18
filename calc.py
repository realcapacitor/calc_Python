#CALCULATOR USING def_function
import time
while 'a'=='a':
   print("▂▃▄▅▆▇█▓▒░-WELCOME-░▒▓█▇▆▅▄▃▂")
   time.sleep(1)
   print("LOADING" , end=" ")
   print(".", end=" ")
   time.sleep(0.2)
   print(".", end=" ")
   time.sleep(0.2)
   print(".", )
   time.sleep(0.2)
   time.sleep(0.2)
   for i in range(50):
      print("=", end=" ")
      while i==49:
          print("=")
          break
      time.sleep(0.1)
  
   print("PLEASE WAIT...",)
  
     
  
   a=int(input(" Enter first no : "))           #THE INPUT PART
   print(" _________________________________________________ ")
   op=input(" Enter Operation  :")
   time.sleep(1)
   print(" _________________________________________________ ")
   b=int(input(" Enter second no : "))
   print(" _________________________________________________ ")
   time.sleep(2)
   print(" ♥ ´¨`•.¸¸.♫│▌▌▌│▌▌│▌CALCULATING...▌│▌▌│▌▌▌♫´¨`*•.¸¸♥ ")
   time.sleep(2)

                                                               #THE def PART
   def add():
      return(a+b)
     
   def sub():
      return(a-b)

   def Mult():
     return(a*b)

   def Div():
      return(a/b)

   def Mod():
     return(a%b)

   
                                                         #THE if...else PART
   if(op=='+'):
      print("The Addition is ",add())
   elif(op=='-'):
      print("The subtraction is ",sub())
   elif(op=='*'):
      print("The multiplication is ",Mult())
   elif(op=='/'):
      print("The division is ",Div())
   elif(op=='%'):
      print("The modulus is ",Mod())
   else:
      print("INVALID OPERATION")
   for i in range(5):
      print(".")

   print(" ★ ☆ ✰ ✯ ✡ ✪ ✶ ✱ ✲ ✴ ✼ ✻ ✵ ❇ ❈ ❊ ❖ ❄ ❆ ❋ ❂ ⁂")
   for i in range(5):
      print(".")



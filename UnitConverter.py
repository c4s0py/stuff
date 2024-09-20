def MassUp():
     print("""
           Converting mass up

           1. MG > G
           2. G > KG
           3. KG > T
           """)
     inp = input("Please make a selection: ")
     inp2 = input("Please Input a number ")
     answer = []
     if inp == "1":
          answer.append(int(inp2)/1000)
          print(str(answer) + " Gramms")
     elif inp == "2":
          answer.append(int(inp2)/1000)
          print(str(answer)+ " Kilograms")
     elif inp == "3":
          answer.append(int(inp2)/1000)
          print(str(answer)+ " Tonnes")

def MassDown():
     print("""
           Converting mass down

           1. T > KG
           2. KG > G
           3. G > MG
           """)
     inp = input("Please make a selection: ")
     inp2 = input("Please Input a number ")
     answer = []
     if inp == "1":
          answer.append(int(inp2)*1000)
          print(str(answer) + " Kilograms")
     elif inp == "2":
          answer.append(int(inp2)*1000)
          print(str(answer)+ " Gramms")
     elif inp == "3":
          answer.append(int(inp2)*1000)
          print(str(answer)+ " Miligrams")

def Mass():
     print("Would you like to convert up or down?")
     inp = input("Please make a selection - U/D: ")
     if inp == "U":
          MassUp()
     if inp == "D":
          MassDown()

def length():
     print("Would you like to convert up or down?")
     inp = input("Please make a selection - U/D: ")
     if inp == "U":
          LengthUp()     
     if inp == "D":
          LengthDown()

def LengthUp():
     print("""
           Converting length up

           1. MM > CM
           2. CM > M
           3. M > KM
           """)
     inp = input("Please make a selection: ")
     inp2 = input("Please input a number:")
     answer = []
     if inp == "1":
          answer.append(int(inp2)/10)
          print(str(answer) + " Centimetres")
     elif inp == "2":
          answer.append(int(inp2)/100)
          print(str(answer) + " Metre")
     elif inp == "3":
          answer.append(int(inp2)/1000)
          print(str(answer) + " Kilometre")

def LengthDown():
     print("""
           Converting length down

           1.KM > M
           2.M > CM
           3.CM > MM
           """)
     inp = input("Please make a selection: ")
     inp2 = input("Please input a number:")
     answer = []
     if inp == "1":
          answer.append(int(inp2)*1000)
          print(str(answer) + " Metre")
     elif inp == "2":
          answer.append(int(inp2)*100)
          print(str(answer) + " Centimetre")
     elif inp == "3":
          answer.append(int(inp2)*10)
          print(str(answer) + " Millimetre")

def Capacity():
     print("Would you like to convert up or down?")
     inp = input("Please make a selection - U/D: ")
     if inp == "U":
          CapacityUp()
     if inp == "D":
          CapacityDown()

def CapacityDown():
     print("""
           1. L > Ml
           """)
     inp = input("Please make a selection: ")
     inp2 = input("Please input a number: ")
     answer = []
     if inp == "1":
          answer.append(int(inp2)*1000)
          print(str(answer)+ " Millilitres")

def CapacityUp():
     print("""
           1. Ml > L
           """)
     inp = input("Please make a selection: ")
     inp2 = input("Please input a number: ")
     answer = []
     if inp == "1":
          answer.append(int(inp2)/1000)
          print(str(answer)+ " Litres")

def Main_Menu():
        print("""
              Welcome to my unit of measure converter.


              1. Mass
              2. Length
              3. Capacity
              4. Info

              """)
        inp = input("Please make a selection: ")
        if inp == "1":
            Mass()
        elif inp == "2":
            length()
        elif inp == "3":
             Capacity()
        elif inp == "4":
             print("Scripted by C4S0, finished on 20/09/2024 ")
Main_Menu()
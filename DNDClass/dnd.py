import random
import tkinter 


frame = tkinter.Tk()
frame.resizable(False,False)
frame.geometry("650x500")
frame.title("DnD Random Character Generator")
frame.config(bg="Gray6")

randomclass = random.choice(open("Classes.txt").read().split())
randomrace = random.choice(open("Races.txt").read().split())
randomdwarfname = random.choice(open("RaceNames/DwarfNames.txt").read().split())
randomdtieflingname = random.choice(open("RaceNames/TieflingNames.txt").read().split())
randomhalforcname = random.choice(open("RaceNames/HalfOrcNames.txt").read().split())
randomelfname = random.choice(open("RaceNames/ElfNames.txt").read().split())
randomhumanname = random.choice(open("RaceNames/Human.txt").read().split())
randomhalflingname = random.choice(open("RaceNames/Halfling.txt").read().split())
randomgnomename = random.choice(open("RaceNames/Gnome.txt").read().split())
randomdragonbornname = random.choice(open("RaceNames/Dragonborn.txt").read().split())
randomhalfelfname = random.choice(open("RaceNames/Halfelf.txt").read().split())


HumanPic = tkinter.PhotoImage(file="RacePictures/Human.png")
HalfOrcPic = tkinter.PhotoImage(file="RacePictures/HalfOrc.png")
ElfPic = tkinter.PhotoImage(file="RacePictures/Elf.png")
HalfElfPic = tkinter.PhotoImage(file="RacePictures/HalfElf.png")
DragonbornPic = tkinter.PhotoImage(file="RacePictures/Dragonborn.png")
DwarfPic = tkinter.PhotoImage(file="RacePictures/Dwarf.png")
GnomePic = tkinter.PhotoImage(file="RacePictures/Gnome.png")
TiefligPic = tkinter.PhotoImage(file="RacePictures/Tiefling.png")
HalflingPic = tkinter.PhotoImage(file="RacePictures/Halfling.png")


pic1 = tkinter.Label(image=None,
                     bg="Gray13",
                     borderwidth=2,
                     relief="solid")
pic1.place(x=400,y=120)

if randomrace == "Halfling":
    pic1.config(image=HalflingPic)

if randomrace == "Tiefling":
    pic1.config(image=TiefligPic)

if randomrace == "Gnome":
    pic1.config(image=GnomePic)

if randomrace == "Dwarf":
    pic1.config(image=DwarfPic)

if randomrace == "Human":
    pic1.config(image=HumanPic)

if randomrace == "Half-orc":
    pic1.config(image=HalfOrcPic)

if randomrace == "Elf":
    pic1.config(image=ElfPic)

if randomrace == "Half-elf":
    pic1.config(image=HalfElfPic)


if randomrace == "Dragonborn":
    pic1.config(image=DragonbornPic)

print(randomdwarfname)

Strength = []
Dexterity = []
Constitution = []
Intelligence = []
Wisdom = []
Charisma = []
dicerolls = []
allignment = ['Lawful Good' , 'Neutral Good', 'Chaotic Good',
              'Lawful Neutral', 'Neutral' , 'Neutral Evil',
              'Lawful Evil', 'Neutral Evil', 'Chaotic Evil']

Allignment = random.choice(allignment)

for i in range(6):
    dicerolls.append(random.randint(8,18))

print(dicerolls)

Title = tkinter.Label(text="Random DND Character Generator",
                      font=("Ariel", 25),
                      background="Gray13",
                      fg="White",
                      border=2,
                      relief="solid")
Title.place(x=110, y=5)

Name = tkinter.Label(text="Name: ",
                      font=("Ariel", 17),
                      background="Gray13",
                      fg="White",
                      border=2,
                      padx=5,
                      pady=5,
                      relief="solid")
Name.place(x=110, y=53)


cred = tkinter.Label(text="Made by C4 ",
                      font=("Ariel", 10),
                      background="Gray13",
                      fg="Red",
                      border=2,
                      relief="solid")
cred.place(x=20, y=20)

Race = tkinter.Label(text="Race: " + "\n" + randomrace +
                     "\n" + "\n" + "Class: " + "\n" + randomclass + 
                     "\n" + "\n" + "Allignment: "+  "\n" + Allignment,
                      font=("Ariel", 17),
                      background="Gray13",
                      fg="White",
                      border=2,
                      padx=5,
                      pady=5,
                      relief="solid")
Race.place(x=110, y=105)

info = tkinter.Label(text="Thank you for looking at my random DnD Character Creator" +
                     "\n" + "It's been quite fun to work on " +
                      "somethings I'd like to work on for this project" + 
                     "\n" + "Is to be able to consistently randomise your character within the GUI"+
                      "\n" + "as opposed to opening and closing the .py file."+ 
                      "\n" + "Another thing is to be able to apply racial bonuses to your pre-existing stats.",
                      font=("Ariel", 10),
                      background="Gray13",
                      fg="White",
                      border=2,
                      relief="solid",
                      padx=5,
                      pady=5,
                      justify="left")
info.place(x=110, y=345)

if randomrace == "Dwarf":
    Name.config(text="Name: " + randomdwarfname)

if randomrace == "Tiefling":
    Name.config(text="Name: " + randomdtieflingname) 

if randomrace == "Elf":
    Name.config(text="Name: " + randomelfname) 

if randomrace == "Half-orc":
    Name.config(text="Name: " + randomhalforcname)

if randomrace == "Human":
    Name.config(text="Name: " + randomhumanname)

if randomrace == "Dragonborn":
    Name.config(text="Name: " + randomdragonbornname)

if randomrace == "Halfling":
    Name.config(text="Name: " + randomhalflingname)

if randomrace == "Gnome":
    Name.config(text="Name: " + randomgnomename)

if randomrace == "Half-elf":
    Name.config(text="Name: " + randomhalfelfname)


if randomclass == "Barbarian":
    Strength.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Constitution.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Dexterity.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Wisdom.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Charisma.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Intelligence.append(max(dicerolls))
    
if randomclass == "Artificer":
    Intelligence.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Constitution.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Dexterity.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Wisdom.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Charisma.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Strength.append(max(dicerolls))

if randomclass == "Bard":
    Charisma.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Dexterity.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Constitution.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Wisdom.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Intelligence.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Strength.append(max(dicerolls))

if randomclass == "Cleric":
    Wisdom.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Constitution.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Strength.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Dexterity.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Charisma.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Intelligence.append(max(dicerolls))

if randomclass == "Druid":
    Wisdom.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Constitution.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Intelligence.append(max(dicerolls))
    dicerolls.append(max(dicerolls))
    Dexterity.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Strength.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Charisma.append(max(dicerolls))

if randomclass == "Fighter":
    Strength.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Constitution.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Dexterity.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Wisdom.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Charisma.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Intelligence.append(dicerolls)

if randomclass == "Monk":
    Dexterity.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Wisdom.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Constitution.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Strength.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Intelligence.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Charisma.append(max(dicerolls))

if randomclass == "Paladin":
    Strength.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Charisma.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Constitution.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Wisdom.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Dexterity.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Intelligence.append(max(dicerolls))

if randomclass == "Ranger":
    Dexterity.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Wisdom.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Constitution.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Strength.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Intelligence.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Charisma.append(max(dicerolls))

if randomclass == "Rogue":
    Dexterity.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Constitution.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Intelligence.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Charisma.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Wisdom.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Strength.append(max(dicerolls))

if randomclass == "Sorcerer":
    Charisma.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Constitution.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Wisdom.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Dexterity.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Intelligence.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Strength.append(max(dicerolls))

if randomclass == "Warlock":
    Charisma.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Dexterity.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Constitution.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Wisdom.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Intelligence.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Strength.append(max(dicerolls))

if randomclass == "Wizard":
    Intelligence.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Constitution.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Wisdom.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Dexterity.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Charisma.append(max(dicerolls))
    dicerolls.remove(max(dicerolls))
    Strength.append(max(dicerolls))
    
highestroll = max(dicerolls)

Str = tkinter.Label(text="STR: " +"\n" +  str(Strength) + 
                    "\n" + "DEX: " +"\n" + str(Dexterity) +
                    "\n" + "CON: " +"\n" + str(Constitution) +
                    "\n" + "INT: " +"\n" + str(Intelligence) +
                    "\n" + "WIS: " +"\n" + str(Wisdom) +
                    "\n" + "CHR: " + "\n" +str(Charisma),
                      font=("Ariel", 20),
                      background="Gray13",
                      borderwidth=2,
                      relief="solid",
                      fg="White")
Str.place(x= 20, y= 50)    

frame.mainloop()
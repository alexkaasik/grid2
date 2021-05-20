from tkinter import *
ColorL = ["red","orange","yellow","green","indigo","indigo","violet","white","black","ultraviolet","phantom"]
Lantern = ["red corps.gif","orange corps.gif","yellow corps.gif","green corps.gif","blue corps.gif","indigo corps.gif","violet corps.gif","white corps.gif","black corps.gif","ultraviolet corps.gif","phantom.gif"]
global can, PI
def list_to_txt(event):
    global can, PI
    txt.delete(0.0,END)
    valik=lbox.curselection()
    txt.insert(END,lbox.get(valik[0]))
    print(lbox.get(valik[0]))
    can.delete(ALL)
    PI = PhotoImage(file=Lantern[valik[0]])
    print(Lantern[valik[0]])
    can.create_image(0,0,image=PI,anchor=NW)
    
def txt_to_list(event):
    text=text.get(0.0,END)
    text=text[-2:-1]
    if text--"/n":
        pass
    else:
        ColorL.append(text)
        lbox.config(height=len(Lantern))
        lbox.insert(END,text)
        txt.delete(0.0,END)
        text-""

def color_change():
    text = txt.get(0.0, END)
    print(list(text))
    if text=="red corps.gif\n":
        ttt="Powered by Rage:\nOATH OF THE RED LANTERNS.\nWith blood and rage of crimson red,\nWe fill men's' souls with darkest dread,\nAnd twist your minds to pain and hate.\nWe'll burn you all—that is your fate!\n\nRed Lanterns puck their own blood like weapon,\nTheir is a curse of Red lantern, if user put on the ring\nit switches their hearts with a energy heart\nif try to remove the ring without\nblue lanterns they will die."
    elif text=="orange corps.gif\n":
        ttt="Powered by Greed:\nOATH OF THE ORANGE LANTERNS.\n What's mine is mine.\nAnd mine and mine.\nAnd mine and mine and mine.\nNot yours!"
    elif text=="yellow corps.gif\n":
        ttt="Powered by Fear:\nOATH OF THE YELLOW LANTERNS.\nIn blackest day, in brightest night,\nBeware your fears made into light\nLet those who try to stop what's right,\nBurn like my power... Sinestro's might!"
    elif text=="green corps.gif\n":
        ttt="Powered by Will:\nOATH OF THE GREEN LANTERNS.\nIn brightest day, in blackest night,\nNo evil shall escape my sight!\nLet those who worship evil's might\nBeware my power, Green Lantern's light!\n\nGreen Lantern are\nspace police force keep peace in the universe\nthere weakness is yellow, color of fear "
    elif text=="blue corps.gif\n":
        ttt="Powered by Hope:\nOATH OF THE BLUE LANTERNS.\nIn fearful day, in raging night,\nwith strong hearts full, our souls ignite,\nwhen all seems lost in the War of Light,\nlook to the stars-- For hope burns bright!\n\nBlue Lanterns can keep Orange lanterns calm,\ndeactivating red lanterns\nand cure their curse,and boost green lanterns"
    elif text=="indigo corps.gif\n":
        ttt="Powered by Compassion:\nOATH OF THE INDIGO LANTERNS.\nTor lorek san, bor nakka mur,\nNatromo faan tornek wot ur.\nTer Lantern ker lo Abin Sur,\nTaan lek lek nok--Formorrow Sur!\n\nIndigo lanterns or indigo tribe\nonly few can change the mental state of\nthe user, their dont have to be Compassion"
    elif text=="violet corps.gif\n":
        ttt="Powered by Love:\nOATH OF THE VIOLET LANTERNS.\nFor hearts long lost and full of fright,\nFor those alone in Blackest Night.\nAccept our ring and join our fight\n Love conquers all with violet light!\n\nviolet lanterns or Star Sapphires are mostly females"
    elif text=="white corps.gif\n":
        ttt="Powered powered by Life\nWHITE LANTERNS\nEmotional Spectrum:\nRage,Greed,Fear,Will,Hope,Compassion,Love.\n\nWhite Lanterns can use whole\nEmotional Spectrum and use their powers"
    elif text=="black corps.gif\n":
        ttt="Powered by Death:\nOATH OF THE BLACK LANTERNS.\nThe Blackest Night falls from the skies,\nThe darkness grows as all light dies.\nWe crave your hearts and your demise,\nBy my black hand, the dead shall rise!\n\nMost black lanterns are dead and was in\nBlackest Night Prophecy\nand end all light in the universe"
    elif text=="ultraviolet corps.gif\n":
        ttt="Powered by Negative Emotional:\nOATH OF THE ULTRAVIOLET LANTERNS.\nBy shield of day, and shield of night,\nWe feed and grow, beyond all sight\n Your darkest self shall be our knight,\nWield the sword of unseen light!"
    elif text=="phantom.gif\n":
        ttt="Powered by Emotional Spectrum:\nRage,Greed,Fear,Will,Hope,Compassion,Love.\nIn Desperate Day, In Hopeless Night,\nThe Phantom Ring is our last light.\nWe yearn for power, strength and might\nI seize the ring, that is my right!"

    opis.config(text=ttt)

lan=Tk()
lan.title("Lanterns")
lan.iconbitmap('0001.ico')
lbox=Listbox(lan,width=20,height=len(Lantern),selectmode=SINGLE)
for element in Lantern:
    lbox.insert(END,element)

lbox.bind("<<ListboxSelect>>",list_to_txt)
lbox.grid(column = 0, row = 0)

txt=Text(lan,height = 4,width = 20,wrap=WORD)
txt.grid(column = 0, row = 2)
txt.bind("<Return>",txt_to_list)

can=Canvas(lan)
can.grid(column = 0, row = 1)

PI = PhotoImage(file="")

panel = Label(lan, image = PI)
panel.grid(column = 0, row = 1)

ColorL=PhotoImage(file="red corps.gif")

btn=Button(text='Info', command=color_change)
btn.grid(column = 2, row = 0)

opis=Label(lan, text="DESCRIPTION", width=40, height=20)
opis.grid(column = 2, row = 1)

lan.mainloop()
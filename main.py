from tkinter import *
from tkinter.ttk import *
from PIL import Image
from PIL import ImageTk

# Creting gui
root = Tk()
var1 = StringVar()
var2 = StringVar()
root.configure(background='darkslategray')
root.geometry("850x680")
root.title("CIPHERWARE")
# main pic
my_pic = Image.open("3928920_850x680.png")

new_pic = ImageTk.PhotoImage(my_pic)
my_label = Label(root, image=new_pic)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

# style the icons
style = Style()  # This will create style object
# This will be adding style, and
# naming that style variable as
# W.Tbutton (TButton is used for ttk.Button).

style.configure('T.TButton', background='black', foreground='white', font='bold')
style.configure('C.TButton', background='gold')
style.configure('C1.TButton', background='lightgreen')
style.configure('L1.TButton',background='firebrick',foreground='white',font=('bold'))
style.configure('E.TButton', background='green', foreground='black', font='bold')
style.configure('D.TButton', background='red', foreground='black', font='bold')

# labels and entry required
head_label = Label(root,text="WELCOME TO CIPHERWARE")
head_label.grid(row=0,column=1)

text_label = Label(root, text="TEXT",style='T.TButton')
text_label.grid(row=1, column=0, padx=10, pady=20,sticky='W')

## key labels and entry required
key_label = Label(root, text="KEY",style='T.TButton')
key_label.grid(row=2, column=0, padx=10, pady=20,sticky='W')

scr = Scrollbar(root)
xscrollbar = Scrollbar(root, orient='horizontal')
xscrollbar.grid(row=1, column=1, sticky=E + W)
text_entry = Entry(root,width=70,xscrollcommand=xscrollbar.set)
text_entry.grid(row=1,column=1,padx=10,pady=20)
xscrollbar.config(command=text_entry.xview)

#key entry required
#scrollbar
key1_entry = Entry(root,width =32)
key1_entry.insert(0,"Key-1")
key1_entry.grid(row=2, column=1,padx=10, pady=20,sticky='W')


key2_entry = Entry(root, text="key-2",width =32)
key2_entry.insert(0,"Key-2")
key2_entry.grid(row=2, column=1,padx=10, pady=20,sticky='E')


#combobox........................................................
encode_cipher = Combobox(root, textvariable=var1)
# Combo Box for length of your password
encode_cipher['values'] = ('Atbash','ROT13'
                           ,'Caesar','Affine','Rail-fence',
                           'Baconian','Polybius_Square','Simple_Substitution'
                           ,'Codes_and_Nomenclators','Columnar_Transpositions',
                           'Autokey','Beaufort','Porta','Running_Key'
                           ,'Vigenere_Gronsfeld','HomoPhonic_Substitutuion'
                           ,'Four_Square','Hill','Playfair','ADFGVX','ADFGX','Bifid'
                           ,'Straddle_Checkerboard','Trifid','Base64','Fractioned_Morse')
encode_cipher.current(0)
encode_cipher.bind('<<ComboboxSelected>>')
encode_cipher.grid(column=1, row=3,sticky='W',padx=10,pady=20)

encode_selection_label = Label(root,text="CIPHER TO ENCODE",style='L1.TButton')
encode_selection_label.grid(row=3,column=0,padx=10,pady=20,sticky='W')

##Instructions for key
inst_entry = Entry(root,width=40)
inst_entry.grid(row=3,column=1,padx=10,pady=20,sticky='E')

#encoded data entry box
encode_label = Label(root,text="ENCODED TEXT",style='T.TButton')
encode_label.grid(row=4,column=0,padx=10,pady=20,sticky='W')
xscrollbar1 = Scrollbar(root, orient='horizontal')
xscrollbar1.grid(row=4, column=1, sticky=E + W)
encode_entry = Entry(root,width=70,xscrollcommand=xscrollbar1.set)
encode_entry.grid(row=4,column=1,padx=10,pady=20)
xscrollbar1.config(command=encode_entry.xview)

#Button for encoding
encode_button = Button(root,text="ENCODE",style='E.TButton')
encode_button.grid(row=5,column=1,padx=10,pady=20)

#Decode part.....................................................

decode_cipher = Combobox(root, textvariable=var1)
# Combo Box for length of your password
decode_cipher['values'] = ('Atbash','ROT13'
                           ,'Caesar','Affine','Rail-fence',
                           'Baconian','Polybius_Square','Simple_Substitution'
                           ,'Codes_and_Nomenclators','Columnar_Transpositions',
                           'Autokey','Beaufort','Porta','Running_Key'
                           ,'Vigenere_Gronsfeld','HomoPhonic_Substitutuion'
                           ,'Four_Square','Hill','Playfair','ADFGVX','ADFGX','Bifid'
                           ,'Straddle_Checkerboard','Trifid','Base64','Fractioned_Morse')
decode_cipher.current(0)
decode_cipher.bind('<<ComboboxSelected>>')
decode_cipher.grid(column=1, row=6,sticky='W',padx=10,pady=20)

decode_selection_label = Label(root,text="CIPHER TO DECODE",style='L1.TButton')
decode_selection_label.grid(row=6,column=0,padx=10,pady=20,sticky='W')

###Instructions for key


inst1_entry = Entry(root,width=40)
inst1_entry.grid(row=6,column=1,padx=10,pady=20,sticky='E')


#decoded data entry box
decode_label = Label(root,text="DECODED TEXT",style='T.TButton')
decode_label.grid(row=7,column=0,padx=10,pady=20,sticky='W')
xscrollbar2 = Scrollbar(root, orient='horizontal')
xscrollbar2.grid(row=7, column=1, sticky=E + W)
decode_entry = Entry(root,width=70,xscrollcommand=xscrollbar2.set)
decode_entry.grid(row=7,column=1,padx=10,pady=20)
xscrollbar2.config(command=decode_entry.xview)

###Button for decodings
decode_button = Button(root,text="DECODE",style='D.TButton')
decode_button.grid(row=8,column=1,padx=10,pady=20)

# BUTTONS required
my_pic1 = Image.open("icons8-copy-30.png")
resize1 = my_pic1.resize((15,15),Image.ANTIALIAS)
new_pic1 = ImageTk.PhotoImage(resize1)
copy = Button(root,image=new_pic1,style='C.TButton')
copy.grid(row=4,column=2,padx=10,pady=20)
copy1 = Button(root,image=new_pic1,style='C.TButton')
copy1.grid(row=7,column=2,padx=10,pady=20)
#................
my_pic2 = Image.open("icons8-broom-90.png")
resize2 = my_pic2.resize((40,40),Image.ANTIALIAS)
new_pic2 = ImageTk.PhotoImage(resize2)
clear = Button(root,image=new_pic2,style='C1.TButton')
clear.grid(row=9,column=1,pady=20)




mainloop()

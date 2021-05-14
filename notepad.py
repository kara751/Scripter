import datetime
import os.path
import time
from tkinter import *
import speech_recognition as sr
import pyttsx3 as pyttsx3
from tkinter.ttk import Combobox
import pyautogui
import pyaudio
import win32api
import tkinter.messagebox as tmsg
from tkinter import filedialog, font
from tkinter.filedialog import askopenfilename,asksaveasfilename

import win32con
import win32gui

root=Tk()
root.geometry("980x687")
root.title("Untitled - Scriptpad")
root.wm_iconbitmap("note.ico")
def new(event=""):
    global file
    root.title("Untitled - Scriptpad")
    file=None
    area.delete(1.0,END)

def openf(event=""):
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),
                         ("Text Document","*.txt")])
    if file =="":
        file =None
    else:
        root.title(os.path.basename(file)+ "- Scriptpad")
        area.delete(1.0,END)
        f=open(file,"r")
        area.insert(1.0,f.read())
        f.close()

def save(event=""):
    global file
    if file== None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),
                         ("Text Document","*.txt")])

        if file == "":
            file=None
        else:
           f =open(file,"w")
           f.write(area.get(1.0,END))
           f.close()
           root.title(os.path.basename(file) + "- Scriptpad")
    else:
        f = open(file, "w")
        f.write(area.get(1.0, END))
        f.close()

def exit():
        root.destroy()

def cut(event=""):
    pyautogui.hotkey('delete')
def copy(event=""):
    area.clipboard_clear()
    area.clipboard_append(area.selection_get())

def paste(event=""):
    area.insert(INSERT,area.clipboard_get())
def select(event=""):
    pyautogui.hotkey('ctrl', 'a')
def notepad():
    tmsg.showinfo("Scriptpad","This is a simple Scriptpad developed by Karan")
def zoomin():
     for i in range(1,50):
      area.config(font=f"Helvetica {15+i}")

def zoomout():
    for i in range(1, 2):
        area.config(font=f"Helvetica {15 - i}")
def dark():
   area.config(bg="black",fg="white",selectbackground="blue")
def white():
   area.config(bg="white",fg="black",selectbackground="blue")
def red():
   area.config(bg="red",fg="black",selectbackground="black")
def blue():
   area.config(bg="blue",fg="white",selectbackground="black")
def green():
   area.config(bg="green",fg="black",selectbackground="black")
def orange():
   area.config(bg="orange",fg="white",selectbackground="black")
def yellow():
   area.config(bg="yellow",fg="black",selectbackground="black")
def print():
    pass
def maximize():
    time.sleep(2)
    root = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(root, win32con.SW_MAXIMIZE)
def minimize():
    time.sleep(2)
    root = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(root, win32con.SW_MINIMIZE)
def clear(event=""):
    area.delete(1.0, END)
def timed(event=""):
    x=datetime.datetime.now()
    area.insert(1.0,x)
def bold():
   area.config(font="Helvetica 19 bold")
def italic():
    area.config(font="Helvetica 19 italic")
def underline():
    area.config(font="Helvetica 19 underline")
def overstrike():
    area.config(font="Helvetica 19 overstrike")
def replace():
    global replacevalue
    global replacevalue2
    window2=Toplevel(root)
    window2.title("Replace")
    window2.wm_iconbitmap("note.ico")
    window2.geometry("300x200")
    lbl2=Label(window2,text="Replace",font="Helvetica 9")
    lbl2.place(x=20,y=30)

    replacevalue = StringVar()
    replacevalue2 =StringVar()

    replaceentry = Entry(window2, textvariable=replacevalue)
    replaceentry.place(x=20,y=60)
    replaceentry2 =Entry(window2,textvariable=replacevalue2)
    replaceentry2.place(x=20,y=100)
    Button(window2,text='Replace',command=replacee).place(x=50,y=140)
    window2.mainloop()
def replacee():
    q=replacevalue.get()
    w=replacevalue2.get()
    area.replace(f'{q},{w}')


def fonts():
       global lab
       global fon
       global window
       global sty
       global color
       window=Toplevel(root)
       window.title("Font")
       window.geometry("510x410")
       window.wm_iconbitmap("note.ico")
       Label(window,text="Size:",font="TimesNewRoman 9").place(x=30,y=20)
       n=StringVar()
       fon=Combobox(window,width=7,textvariable=n,state="readonly",font="Helvetica 9")
       fon['values'] =('8',
                       '10',
                       '12',
                       '14',
                       '16',
                       '18',
                       '20',
                       '22',
                       '24',
                       '26',
                       '28',
                       '30',
                       '32',
                       '34','36','38','40','42','44','46','48','50','52','54','56','58','60','62','64','66','68','70','72','74','76','78','80','82','84','86','88','90','92','94','96','98','100'

                       )
       fon.current(4)
       fon.place(x=30,y=60)
       z = StringVar()
       color = Combobox(window, width=10, textvariable=z, state="readonly", font="Helvetica 9")
       color['values'] = ('snow', 'ghost white','white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99')
       color.current(2)
       color.place(x=120, y=60)
       Label(window, text="Font Color:", font="TimesNewRoman 9").place(x=120, y=20)
       Label(window, text="Font:",font="TimesNewRoman 9").place(x=230, y=20)
       r=StringVar()
       sty=Combobox(window,width=25,textvariable=r,state="readonly",font="Helvetica 9")
       sty['values']=('8514oem',
'Fixedsys',
'Terminal',
'Modern',
'Roman',
'Script',
'Courier',
'MS Serif',
'MS Sans Serif',
'Small Fonts',
'Marlett',
'Arial',
'Arabic Transparent',
'Arial Baltic',
'Arial CE',
'Arial CYR',
'Arial Greek',
'Arial TUR',
'Arial Black',
'Bahnschrift Light',
'Bahnschrift SemiLight',
'Bahnschrift',
'Bahnschrift SemiBold',
'Bahnschrift Light SemiCondensed',
'Bahnschrift SemiLight SemiConde',
'Bahnschrift SemiCondensed',
'Bahnschrift SemiBold SemiConden',
'Bahnschrift Light Condensed',
'Bahnschrift SemiLight Condensed',
'Bahnschrift Condensed',
'Bahnschrift SemiBold Condensed',
'Calibri',
'Calibri Light',
'Cambria',
'Cambria Math',
'Candara',
'Candara Light',
'Comic Sans MS',
'Consolas',
'Constantia',
'Corbel',
'Corbel Light',
'Courier New',
'Courier New Baltic',
'Courier New CE',
'Courier New CYR',
'Courier New Greek',
'Courier New TUR',
'Ebrima',
'Franklin Gothic Medium',
'Gabriola',
'Gadugi',
'Georgia',
'Impact',
'Ink Free',
'Javanese Text',
'Leelawadee UI',
'Leelawadee UI Semilight',
'Lucida Console',
'Lucida Sans Unicode',
'Malgun Gothic',
'@Malgun Gothic',
'Malgun Gothic Semilight',
'@Malgun Gothic Semilight',
'Microsoft Himalaya',
'Microsoft JhengHei',
'@Microsoft JhengHei',
'Microsoft JhengHei UI',
'@Microsoft JhengHei UI',
'Microsoft JhengHei Light',
'@Microsoft JhengHei Light',
'Microsoft JhengHei UI Light',
'@Microsoft JhengHei UI Light',
'Microsoft New Tai Lue',
'Microsoft PhagsPa',
'Microsoft Sans Serif',
'Microsoft Tai Le',
'Microsoft YaHei',
'@Microsoft YaHei',
'Microsoft YaHei UI',
'@Microsoft YaHei UI',
'Microsoft YaHei Light',
'@Microsoft YaHei Light',
'Microsoft YaHei UI Light',
'@Microsoft YaHei UI Light',
'Microsoft Yi Baiti',
'MingLiU-ExtB',
'@MingLiU-ExtB',
'PMingLiU-ExtB',
'@PMingLiU-ExtB',
'MingLiU_HKSCS-ExtB',
'@MingLiU_HKSCS-ExtB',
'Mongolian Baiti',
'MS Gothic',
'@MS Gothic',
'MS UI Gothic',
'@MS UI Gothic',
'MS PGothic',
'@MS PGothic',
'MV Boli',
'Myanmar Text',
'Nirmala UI',
'Nirmala UI Semilight',
'Palatino Linotype',
'Segoe MDL2 Assets',
'Segoe Print',
'Segoe Script',
'Segoe UI',
'Segoe UI Black',
'Segoe UI Emoji',
'Segoe UI Historic',
'Segoe UI Light',
'Segoe UI Semibold',
'Segoe UI Semilight',
'Segoe UI Symbol',
'SimSun',
'@SimSun',
'NSimSun',
'@NSimSun',
'SimSun-ExtB',
'@SimSun-ExtB',
'Sitka Small',
'Sitka Text',
'Sitka Subheading',
'Sitka Heading',
'Sitka Display',
'Sitka Banner',
'Sylfaen',
'Symbol',
'Tahoma',
'Times New Roman',
'Times New Roman Baltic',
'Times New Roman CE',
'Times New Roman CYR',
'Times New Roman Greek',
'Times New Roman TUR',
'Trebuchet MS',
'Verdana',
'Webdings',
'Wingdings',
'Yu Gothic',
'@Yu Gothic',
'Yu Gothic UI',
'@Yu Gothic UI',
'Yu Gothic UI Semibold',
'@Yu Gothic UI Semibold',
'Yu Gothic Light',
'@Yu Gothic Light',
'Yu Gothic UI Light',
'@Yu Gothic UI Light',
'Yu Gothic Medium',
'@Yu Gothic Medium',
'Yu Gothic UI Semilight',
'@Yu Gothic UI Semilight',
'HoloLens MDL2 Assets',
'Open Sans',
'Open Sans Semibold',
'Arial Unicode MS',
'@Arial Unicode MS',
'Century',
'Wingdings 2',
'Wingdings 3',
'Book Antiqua',
'Century Gothic',
'Haettenschweiler',
'MS Outlook',
'Tempus Sans ITC',
'Pristina',
'Papyrus',
'Mistral',
'Lucida Handwriting',
'Kristen ITC',
'Juice ITC',
'French Script MT',
'Freestyle Script',
'Bradley Hand ITC',
'Garamond',
'Monotype Corsiva',
'Algerian',
'Baskerville Old Face',
'Bauhaus 93',
'Bell MT',
'Berlin Sans FB',
'Bernard MT Condensed',
'Bodoni MT Poster Compressed',
'Britannic Bold',
'Broadway',
'Brush Script MT',
'Californian FB',
'Centaur',
'Chiller',
'Colonna MT',
'Cooper Black',
'Footlight MT Light',
'Harlow Solid Italic',
'Harrington',
'High Tower Text',
'Jokerman',
'Kunstler Script',
'Lucida Bright',
'Lucida Calligraphy',
'Lucida Fax',
'Magneto',
'Matura MT Script Capitals',
'Modern No. 20',
'Niagara Engraved',
'Niagara Solid',
'Old English Text MT',
'Onyx',
'Parchment',
'Playbill',
'Poor Richard',
'Ravie',
'Informal Roman',
'Showcard Gothic',
'Snap ITC',
'Stencil',
'Viner Hand ITC',
'Vivaldi',
'Vladimir Script',
'Wide Latin',
'Tw Cen MT',
'Tw Cen MT Condensed',
'Script MT Bold',
'Rockwell Extra Bold',
'Rockwell Condensed',
'Rockwell',
'Rage Italic',
'Perpetua Titling MT',
'Perpetua',
'Palace Script MT',
'OCR A Extended',
'Maiandra GD',
'Lucida Sans Typewriter',
'Lucida Sans',
'Imprint MT Shadow',
'Goudy Stout',
'Goudy Old Style',
'Gloucester MT Extra Condensed',
'Gill Sans Ultra Bold Condensed',
'Gill Sans Ultra Bold',
'Gill Sans MT Condensed',
'Gill Sans MT',
'Gill Sans MT Ext Condensed Bold',
'Gigi',
'Franklin Gothic Medium Cond',
'Franklin Gothic Heavy',
'Franklin Gothic Demi Cond',
'Franklin Gothic Demi',
'Franklin Gothic Book',
'Forte',
'Felix Titling',
'Eras Medium ITC',
'Eras Light ITC',
'Eras Demi ITC',
'Eras Bold ITC',
'Engravers MT',
'Elephant',
'Edwardian Script ITC',
'Curlz MT',
'Copperplate Gothic Light',
'Copperplate Gothic Bold',
'Century Schoolbook',
'Castellar',
'Calisto MT',
'Bookman Old Style',
'Bodoni MT Condensed',
'Bodoni MT Black',
'Bodoni MT',
'Blackadder ITC',
'Arial Rounded MT Bold',
'Agency FB',
'Bookshelf Symbol 7',
'MS Reference Sans Serif',
'MS Reference Specialty',
'Berlin Sans FB Demi',
'Tw Cen MT Condensed Extra Bold',
'Arial Narrow',
'MT Extra',
'PosterBodoni WGL4 BT',
'ZapfHumnst Ult BT',
'Futura Md BT',
'Futura XBlkIt BT',
'Geometr212 Bk BT',
'Stencil BT',
'Futura LtCn BT',
'FuturaBlack WGL4 BT',
'Vineta BT',
'ShotgunBlanks BT',
'FrankGoth BT',
'Square721 Ex BT',
'Humanst521 XBd BT',
'Swis721 Ex BT',
'OCR-A BT',
'Incised901 Nd BT',
'Incised901 NdIt BT',
'CaslonOpnface BT',
'BankGothic Md BT',
'Decorated035 BT',
'Carmina Blk BT',
'Kaufmann BT',
'VAGRounded BT',
'HandelGothic BT',
'DomBold BT',
'BroadwayEngraved BT',
'Swis721 BlkRnd BT',
'Folio Lt BT',
'Schneidler Blk BT',
'Zurich XBlk BT',
'Fraktur BT',
'WeddingText BT',
'BernhardTango BT',
'Brush455 BT',
'Normande BT',
'Cooper BlkOul BT',
'Amazone BT',
'Freehand591 BT',
'Century725 Blk BT',
'Parisian BT',
'AdLib WGL4 BT',
'Chianti XBd BT',
'Sonic XBd BT',
'AlphabetSoup Tilt BT',
'CandyBits BT',
'Eyeballs BT',
'PrimaSans BT',
'NewspaperPi BT')
       sty.current(130)
       sty.place(x=230, y=60)
       Button(window,text="Ok",command=ok,padx=10,bg="black",fg="white",font="TimesNewRoman 13 bold").place(x=170,y=350)
       Button(window,text="Apply",command=fo,padx=10,bg="black",fg="white",font="TimesNewRoman 13 bold").place(x=280,y=350)
       Label(window, text="Sample:", fg="black", font="TimesNewRoman 9").place(x=145,y=130)
       lab=Label(window,relief=SUNKEN,cursor='tcross',text="CoDe",bg="#856ff8",fg="white",font="TimesNewRoman 10")
       lab.place(x=145,y=170)
       window.resizable(0, 0)
       window.mainloop()

def fo():
    x=fon.get()
    y=sty.get()
    z=color.get()
    tuple=(f"{y}",x)
    #area.insert(1.0,z)
    area.config(font=tuple,foreground=z)
    lab.config(font=(tuple))
    lab.config(fg=f'{z}')
def left():
    area.tag_configure("left",justify='left')
    area.tag_add("left",1.0,"end")
def right():
    area.tag_configure("right", justify='right')
    area.tag_add("right", 1.0, "end")
def center():
    area.tag_configure("center", justify='center')
    area.tag_add("center", 1.0, "end")
def ok():
    window.destroy()
def takeCommand():
     engine=pyttsx3.init('sapi5')
     rate=engine.getProperty('rate')
     #volume=engine.getProperty('volume')
     voices =engine.getProperty('voices')
     engine.setProperty('voice',voices[1].id)
     engine.setProperty('rate',rate-20)
     #engine.setProperty('volume',volume+0.25)
     engine.say(area.get(1.0,END))
     engine.runAndWait()
def callback(event):
    root.after(1, _callback)
def _callback():
 abc=area.get(1.0,END)
 count = 0;
 for i in range(0, len(abc)):
     if (abc[i] != ' '):
         count = count + 1;
 statusbar.set(f"Characters:{count - int(1)} Words:{len(abc.split())}")
 lbl=Label(root,textvariable=statusbar)
 lbl.pack(side=BOTTOM,anchor="sw")

check=IntVar()
statusbar = StringVar()
statusbar.set("UTF-8")

sbar = Label(root, textvariable=statusbar, relief=SUNKEN, bg="white", fg="black", anchor="center",font='Helvetica 10')
sbar.pack(side=BOTTOM, fill=X)
scrollbar =Scrollbar(root)
hscrollbar =Scrollbar(root,orient=HORIZONTAL)
scrollbar.pack(side=RIGHT,fill=Y)
hscrollbar.pack(side=BOTTOM,fill=X)
global area
area = Text(root,yscrollcommand = scrollbar.set,xscrollcommand=hscrollbar.set,bg="#856ff8",fg="white",font="TimesNewRoman 16",undo=True,wrap=WORD,selectbackground="black")

area.pack(fill="both",ipady=1000000)


scrollbar.config(command=area.yview)
hscrollbar.config(command=area.xview)


file =None
Menubar =Menu(root)
filemenu =Menu(Menubar,tearoff=0)
filemenu.add_command(label="New",command=new,accelerator="Ctrl+N")
filemenu.add_separator()
filemenu.add_command(label="Open",command=openf,accelerator="Ctrl+O")
filemenu.add_separator()
filemenu.add_command(label="Save",command=save,accelerator="Ctrl+S")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=exit)
Menubar.add_cascade(label="File",menu=filemenu)
root.config(menu=Menubar)

editmenu =Menu(Menubar,tearoff=0)
editmenu.add_command(label="Undo",command=area.edit_undo,accelerator="Ctrl+Z")
editmenu.add_command(label="Redo",command=area.edit_redo,accelerator="Ctrl+Y")
editmenu.add_separator()
editmenu.add_command(label="Cut",command=cut,accelerator="Ctrl+X")
editmenu.add_command(label="Copy",command=copy,accelerator="Ctrl+C")
editmenu.add_command(label="Paste",command=paste,accelerator="Ctrl+V")
editmenu.add_separator()
editmenu.add_command(label="Select all",command=select,accelerator="Ctrl+A")
editmenu.add_command(label="Clear all",command=clear,accelerator="Del")
editmenu.add_separator()
editmenu.add_command(label="Time/Date",command=timed,accelerator="F5")
Menubar.add_cascade(label="Edit",menu=editmenu)

format=Menu(Menubar,tearoff=0)
format.add_checkbutton(label="Word Wrap",variable=check)
format.add_separator()
format.add_command(label="Font...",command=fonts)
format.add_separator()
format.add_command(label="Bold",command=bold,font='Helvetica 9 bold')
format.add_command(label="Italic",command=italic,font='Helvetica 9 italic')
format.add_separator()
format.add_command(label="Underline",command=underline)
format.add_command(label="Overstrike",command=overstrike)
format.add_separator()
Menubar.add_cascade(label="Format",menu=format)
align=Menu(format,tearoff=0)

align.add_command(label="Left",command=left)
align.add_separator()
align.add_command(label="Right",command=right)
align.add_separator()
align.add_command(label="Center",command=center)
format.add_cascade(label="Alignment",menu=align)





view=Menu(Menubar,tearoff=0)
view.add_checkbutton(label="Status Bar",variable=check)
view.add_separator()
Menubar.add_cascade(label="View",menu=view)

zom=Menu(view,tearoff=0)
zom.add_command(label="Zoom In",command=zoomin)
zom.add_command(label="Zoom Out",command=zoomout)
zom.add_separator()
zom.add_command(label="Maximize",command=maximize)
zom.add_command(label="Minimize",command=minimize)
view.add_cascade(label="Appearance",menu=zom)

set=Menu(Menubar,tearoff=0)
Menubar.add_cascade(label="Settings...",menu=set)

theme =Menu(set,tearoff=0)
theme.add_command(label="Dark mode",command=dark,background="black",foreground="white")
theme.add_separator()
theme.add_command(label="Notepad mode",command=white)
theme.add_separator()
theme.add_command(label="Red mode",command=red,background="red",foreground="black")
theme.add_separator()
theme.add_command(label="Blue mode",command=blue,background="blue",foreground="white")
theme.add_separator()
theme.add_command(label="Green mode",command=green,background="green",foreground="black")
theme.add_separator()
theme.add_command(label="Orange mode",command=orange,background="orange",foreground="white")
theme.add_separator()
theme.add_command(label="Yellow mode",command=yellow,background="yellow",foreground="black")
set.add_cascade(label="Theme",menu=theme)

loud=Menu(Menubar,tearoff=0)
loud.add_command(label="Read aloud",command=takeCommand)
Menubar.add_cascade(label="Speech",menu=loud)


help=Menu(Menubar,tearoff=0)
help.add_command(label="About Scriptpad",command=notepad)
Menubar.add_cascade(label="Help",menu=help)
root.bind("<Control-n>",new)
root.bind("<Control-o>",openf)
root.bind("<Control-s>",save)
root.bind("<Control-x>",cut)
root.bind("<Control-c>",copy)
root.bind("<Control-v>",paste)
root.bind("<Control-a>",select)
root.bind("<Delete>",clear)
root.bind("<F5>",timed)
root.bind("<Control-z>",lambda e:area.edit_undo())
root.bind("<Control-y>",lambda e:area.edit_redo())
root.bind("<Key>",callback)
fonts=font.families()
for i in fonts:
    print()
root.mainloop()

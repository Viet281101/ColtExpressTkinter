
# !/usr/bin/python3
import sys
import pygame
from tkinter import ttk
import tkinter as tk
from tkinter import *
from settings import *
from PIL import ImageTk, Image
from itertools import count, cycle
from tkinter import messagebox


class Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.resizable(False, False)
        self['bg'] = 'black'
        self._frame = None
        self.switch_frame(MenuStartWindow)

    def switch_frame(self, frame_class) -> None:
        if unmute: clickSound()
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self.geometry('1194x576+'+self.screen()+'+20')
        self._frame.pack()

    def screen(self) -> str:
        screen_width = self.winfo_screenwidth()
        posX = (screen_width //2) - (1194//2) 
        return str(posX)


class MenuStartWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.background()
        self.buttonGame(master)

    def background(self) -> None:
        self.lbl = ImageLabel(self)
        self.lbl['bd'] = 0
        self.lbl['cursor'] = 'X_cursor'
        self.lbl.grid(row = 0, column = 0)
        self.lbl.load('./assets/Images/pixel_train_city.gif')
        if unmute: playMusic()
    
    def buttonGame(self, master) -> None:
        frameBtn = tk.Frame(self,width = 170, height = 576, bg=TEXT_PURPLE)
        frameBtn.grid(row = 0, column = 1)

        self.btn_start = tk.Button(frameBtn, fg = 'purple', 
            font=FONT_HELV, command=lambda: master.switch_frame(Game), 
            width= 10, highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, 
            bd = 0, activebackground=TEXT_BLACK, cursor='target')
        self.btn_start.place(x = 18 , y=150)

        self.btn_ruler = tk.Button(frameBtn, fg = 'purple', 
            font=FONT_HELV, command=lambda: master.switch_frame(Rule), 
            width= 10, highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, 
            bd = 0, activebackground=TEXT_BLACK, cursor='target')
        self.btn_ruler.place(x = 18 , y=200)

        self.btn_setting = tk.Button(frameBtn, fg = 'purple', 
            font=FONT_HELV, command=lambda: master.switch_frame(Setting), 
            width= 10, highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, 
            bd = 0, activebackground=TEXT_BLACK, cursor='target')
        self.btn_setting.place(x = 18 , y=250)
        
        self.btn_credit = tk.Button(frameBtn, fg = 'purple', 
            font=FONT_HELV, command=lambda: master.switch_frame(Credit), 
            width= 10, highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, 
            bd = 0, activebackground=TEXT_BLACK, cursor='target')
        self.btn_credit.place(x = 18 , y=300)

        self.btn_quit = tk.Button(frameBtn, fg = 'purple', 
            font=FONT_HELV, command=self.confirmBox, 
            width= 10, highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, 
            bd = 0, activebackground=TEXT_BLACK, cursor='target')
        self.btn_quit.place(x = 18 , y=350)

        self.loadTextLang()

    def loadTextLang(self) -> None:
        if langEn and not langFr:
            self.btn_start.config(text=english_text['start'])
            self.btn_ruler.config(text=english_text['rule'])
            self.btn_setting.config(text=english_text['setting'])
            self.btn_credit.config(text=english_text['credit'])
            self.btn_quit.config(text=english_text['quit'])
        
        elif not langEn and langFr:
            self.btn_start.config(text=francais_texte['start'])
            self.btn_ruler.config(text=francais_texte['rule'])
            self.btn_setting.config(text=francais_texte['setting'])
            self.btn_credit.config(text=francais_texte['credit'])
            self.btn_quit.config(text=francais_texte['quit'])
    
    def confirmBox(self) -> None:
        if unmute: clickSound()
        if langEn and not langFr:
            confirm = messagebox.askquestion('Confirm Box', 
            "Are you sure to quit the game ? \nYour data will not be saved !", 
            icon='warning')
            if confirm == 'yes':
                self.quit()

        elif not langEn and langFr:
            confirm = messagebox.askquestion('Confirm Box', 
            "Etes-vous sûr de quitter le jeu ? \nVos données ne seront pas enregistrées !", 
            icon='warning')
            if confirm == 'yes':
                self.quit()
        

class ImageLabel(tk.Label):
    def load(self, im) -> None:
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self) -> None:
        self.config(image=None)
        self.frames = None

    def next_frame(self) -> None:
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)


class Game(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        stopMusic()

        ''' Start to build the game in here '''
        ##### Set canvas 
        self.tkraise()
        # self.pack_propagate(False)
        self.canvas = tk.Canvas(self, 
            height = 576, width = 1194, 
            bd = 0, bg = "#000000",
            highlightthickness = 0)
        self.canvas.pack(side=TOP,padx=0,pady=0)
        self.canvas.focus_set()

        ##### Set background
        self.backgroundImg = PhotoImage(file='./assets/Images/BackgroundCity.png')


        self.returnBtn = tk.Button(self.canvas, text="",
            fg = 'purple', font=FONT_HELV,
            command=lambda: master.switch_frame(MenuStartWindow),
            highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, 
            bd = 0, activebackground=TEXT_BLACK, cursor='target')
        self.returnBtn.place(x = 0, y = 0)

        self.loadTextLang()
    
    def loadTextLang(self) -> None:
        if langEn and not langFr:
            self.returnBtn.config(text=english_text['return'])

        elif not langEn and langFr:
            self.returnBtn.config(text=francais_texte['return'])

        
class Rule(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        stopMusic()

        ##### Set canvas 
        self.tkraise()
        self.canvas = tk.Canvas(self, 
            height = 576, width = 1194, 
            bd = 0, bg = "#000000",
            highlightthickness = 0)
        self.canvas.pack(side=TOP,padx=0,pady=0)
        self.canvas.focus_set()

        self.returnBtn = tk.Button(self.canvas, text="",
            fg = 'purple', font=FONT_HELV,
            command=lambda: master.switch_frame(MenuStartWindow),
            highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, 
            bd = 0, activebackground=TEXT_BLACK, cursor='target')
        self.returnBtn.place(x = 0, y = 0)

        self.loadTextLang()
    
    def loadTextLang(self) -> None:
        if langEn and not langFr:
            self.returnBtn.config(text=english_text['return'])

        elif not langEn and langFr:
            self.returnBtn.config(text=francais_texte['return'])


class Credit(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        stopMusic()

        ##### Set canvas 
        self.tkraise()
        self.canvas = tk.Canvas(self, 
            height = 576, width = 1194, 
            bd = 0, bg = "#000000",
            highlightthickness = 0)
        self.canvas.pack(side=TOP,padx=0,pady=0)
        self.canvas.focus_set()

        self.textCreditCV = tk.Canvas(self.canvas, 
            width=500, height=1000, 
            bd = 0, bg = "#000000",
            highlightthickness = 0, borderwidth=0, 
            cursor='pirate')
        
        self.canvas.create_window(360, 0, anchor=NW, 
            window=self.textCreditCV)
        
        self.creditTxt = tk.Text(self.textCreditCV, 
            yscrollcommand=True, font = FONT_HELV,
            bg = '#000000', bd = 0)
        

        self.returnBtn = tk.Button(self.canvas, text="",
            fg = 'purple', font=FONT_HELV,
            command=lambda: master.switch_frame(MenuStartWindow),
            highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, 
            bd = 0, activebackground=TEXT_BLACK, cursor='target')
        self.returnBtn.place(x = 0, y = 0)

        self.loadTextLang()
    
    def loadTextLang(self) -> None:
        if langEn and not langFr:
            self.returnBtn.config(text=english_text['return'])

        elif not langEn and langFr:
            self.returnBtn.config(text=francais_texte['return'])


class Setting(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        stopMusic()

        ###### Title page
        self.title = tk.Label(self, text="", fg = 'purple', 
            font=('Helvetica 59 underline'), width=8,
            bd = 0, bg ='black', relief=None)
        self.title.grid(row = 0, columnspan=2, sticky = W)

        self.lineLbl_0 = tk.Label(self, width=44, height=3, 
            bd = 0, bg = 'black', relief=None)
        self.lineLbl_0.grid(row=1, columnspan=2, sticky=W)

        #### Language Setting
        self.langLbl = tk.Label(self, text="", 
            fg = 'purple', font=FONT_HELV, width = 20,
            bd = 0, bg ='black', relief=None)
        self.langLbl.grid(row = 2, column = 0, sticky = W)
        
        self.Cbstyle = ttk.Style()
        self.Cbstyle.map('TCombobox', fieldbackground=[('readonly','purple')])
        self.Cbstyle.map('TCombobox', selectbackground=[('readonly', 'purple')])
        self.Cbstyle.map('TCombobox', selectforeground=[('readonly', 'black')])
        
        self.langTxt = tk.StringVar()
        self.langBox = ttk.Combobox(self, textvariable=self.langTxt, 
            values=('English', 'French'), width=14)
        self.langBox.grid(row = 2, column = 1, sticky = W)
        self.langBox['state'] = 'readonly'
        self.setDefaultLanguage()
        self.langBox.bind('<<ComboboxSelected>>', self.updateLang)

        ### Sound Setting
        self.soundLbl = tk.Label(self, text = "Sound \nMusic : ", 
            fg = 'purple', font=FONT_HELV, width = 20,
            bd = 0, bg ='black', relief=None)
        self.soundLbl.grid(row = 3, column = 0, sticky = W)
        
        ### Sound Scale
        self.scaleVar = tk.StringVar()
        self.scaleSound = tk.Scale(self, from_=0, to=100, orient=HORIZONTAL, 
            troughcolor = 'purple', bg = 'black', bd = 0, 
            fg = 'purple', font=FONT_HELV, width=15, length = 126,
            highlightbackground = TEXT_PURPLE, 
            resolution=0.1, variable= self.scaleVar)
        self.scaleSound.grid(row = 3, column = 1, sticky = W)

        ### Mute and Unmute setting
        self.muteLbl = tk.Label(self, text = "Sound : ", 
            fg = 'purple', font=FONT_HELV, width = 20,
            bd = 0, bg ='black', relief=None)
        self.muteLbl.grid(row=4, column=0, sticky=W)

        self.musicBtnZone = tk.Frame(self, bg = '#000000', width=128, height=23)
        self.musicBtnZone.grid(row=4, column=1, sticky=W)

        self.playImg = Image.open("./assets/Images/volume-icon-play.png")
        self.playImgSize = self.playImg.resize((23, 23))
        self.pauseImg = Image.open("./assets/Images/volume-icon-pause.png")
        self.pauseImgSize = self.pauseImg.resize((23, 23))

        self.unmuteImg = ImageTk.PhotoImage(self.playImgSize)
        self.muteImg = ImageTk.PhotoImage(self.pauseImgSize)

        self.muteBtn = tk.Button(self.musicBtnZone, image = self.unmuteImg, 
            relief = FLAT, command = self.changeIcon, width=30,
            highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, bd = 0, 
            activebackground=TEXT_BLACK)
        self.muteBtn.image = self.unmuteImg
        self.muteBtn.place(x = 47, y = 0)

        ### Buttons to change the value of scale sound
        self.decreaseScaleVar = tk.Button(self.musicBtnZone, text='-',
            fg = '#ff00d7', font=FONT_HELV, width=1, height=1,
            relief = FLAT, command = self.decreaseSoundScale,
            highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, bd = 0, 
            activebackground=TEXT_BLACK)
        self.decreaseScaleVar.place(x = 0, y = 0)

        self.increaseScaleVar = tk.Button(self.musicBtnZone, text='+',
            fg = '#ff00d7', font=FONT_HELV, width=1, height=1,
            relief = FLAT, command = self.increaseSoundScale,
            highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, bd = 0, 
            activebackground=TEXT_BLACK)
        self.increaseScaleVar.place(x = 91, y = 0)

        self.setDefaultVolumeScale()

        ### Space vertical
        self.lineLbl = tk.Label(self, width=44, height=5, 
            bd = 0, bg = 'black', relief=None)
        self.lineLbl.grid(row=5, columnspan=2, sticky=W)

        ### Buttons
        self.applyBtn = tk.Button(self, text=english_text['apply'], width = 18,
            fg = 'purple', font=FONT_HELV,
            command=self.applyChange,
            highlightbackground='#76428A', bg=TEXT_PURPLE, bd = 0, 
            activebackground=TEXT_BLACK)
        self.applyBtn.grid(row = 6, column = 0, sticky=W)

        self.returnBtn = tk.Button(self, text=english_text['return'], width = 9,
            fg = 'purple', font=FONT_HELV,
            command=lambda: master.switch_frame(MenuStartWindow),
            highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, bd = 0, 
            activebackground=TEXT_BLACK, 
            borderwidth = 0)
        self.returnBtn.grid(row = 6, column=1, sticky = W, padx=2)

        self.loadTextLang()
    
    def loadTextLang(self) -> None:
        if langEn and not langFr:
            self.title.config(text = english_text['setting'].upper() + ':')
            self.langLbl.config(text= english_text['language'] + ' : ')
            self.soundLbl.config(
                text=f"{english_text['setting']} \n{english_text['volume']} : "
            )
            self.applyBtn.config(text=english_text['apply'])
            self.returnBtn.config(text=english_text['return'])
        
        elif not langEn and langFr:
            self.title.config(text = francais_texte['setting'])
            self.langLbl.config(text= francais_texte['language'] + ' : ')
            self.soundLbl.config(
                text=f"{francais_texte['setting']} \n{francais_texte['volume']} : "
            )
            self.applyBtn.config(text=francais_texte['apply'])
            self.returnBtn.config(text=francais_texte['return'])
    
    def changeIcon(self) -> None:
        global unmute
        if self.muteBtn.image == self.unmuteImg and unmute:
            self.muteBtn.config(image=self.muteImg)
            self.muteBtn.image = self.muteImg
            unmute = False
        elif self.muteBtn.image == self.muteImg and not unmute:
            self.muteBtn.config(image=self.unmuteImg)
            self.muteBtn.image = self.unmuteImg
            unmute = True

    def setDefaultLanguage(self) -> None:
        if langEn and not langFr:
            self.langBox.set('English')
            
        elif not langEn and langFr:
            self.langBox.set('French')

    def setDefaultVolumeScale(self) -> None:
        global volume_sound
        vol : float = (volume_sound * 100.0)
        self.scaleVar.set(f'{vol}')
        if not unmute:
            self.muteBtn.config(image=self.muteImg)
            self.muteBtn.image = self.muteImg

    def decreaseSoundScale(self) -> None:
        self.scaleVar.set(float(self.scaleVar.get()) - 5.0)

    def increaseSoundScale(self) -> None:
        self.scaleVar.set(float(self.scaleVar.get()) + 5.0)
    
    def updateLang(self, event) -> None:
        if langEn and not langFr:
            messagebox.showinfo(
                title='Language Notification',
                message=f'You selected {self.langTxt.get()}!'
            )
        
        elif not langEn and langFr:
            messagebox.showinfo(
                title='Langue Notification',
                message=f'Vous avez sélectionné {self.langTxt.get()}!'
            )
        
    def applyChange(self) -> None:
        if unmute: clickSound()
        global langEn, langFr
        global volume, volume_sound

        ##### apply language
        if str(self.langTxt.get()) == 'English':
            print('English')
            langEn = True
            langFr = False
        elif str(self.langTxt.get()) == 'French':
            print('French')
            langEn = False
            langFr = True
        
        self.loadTextLang()
        ##### apply volume
        volume = float(self.scaleVar.get())
        volume_sound = (volume) / 100.0
        print("Volume scale after apply: ", volume)
        print("Volume sound after apply: ", volume_sound)

        if unmute: print('unmute\n')
        elif not unmute: print('mute\n')


## Sounds
def playMusic() -> None:
    start_music.play(-1)
    start_music.set_volume(volume_sound)
def stopMusic() -> None:
    start_music.stop()
def clickSound() -> None:
    click_sound.play(1)
    click_sound.set_volume(0.2)

def startMenuGame() -> None:
    startMenu = Window()
    startMenu.title('Colt Express')
    startMenu.iconphoto(False, PhotoImage(file='./assets/Images/sack.png'))
    startMenu.bind('<Escape>', lambda event: startMenu.quit())
    startMenu.mainloop()

    
def main(args) -> None:
    startMenuGame()


if __name__ == '__main__':

    #### set volume
    volume : float = 0.0
    volume_sound : float = 0.5
    unmute : bool = True

    #### Load sounds
    pygame.mixer.init()
    start_music = pygame.mixer.Sound("./assets/Sound/start_train_sound.wav")
    click_sound = pygame.mixer.Sound("./assets/Sound/click_01.wav")

    #### set lang
    langEn : bool = True
    langFr : bool = False

    ##### main
    main(sys.argv)


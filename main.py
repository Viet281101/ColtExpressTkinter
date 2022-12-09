
# !/usr/bin/python3
import sys, pygame, webbrowser
import tkinter as tk
from itertools import count, cycle
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from settings import *


class Window(tk.Tk):
    def __init__(self) -> None:
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
    def __init__(self, master) -> None:
        tk.Frame.__init__(self, master)
        stopCreditMusic()
        self.background()
        self.buttonGame(master)

    def background(self) -> None:
        self.lbl = ImageLabel(self)
        self.lbl['bd'] = 0
        self.lbl['cursor'] = 'X_cursor'
        self.lbl.grid(row = 0, column = 0)
        self.lbl.load(path_start_menu_bg)
        if unmute: trainSound()
    
    def buttonGame(self, master) -> None:
        frameBtn = tk.Frame(self,width = 170, height = 576, bg=TEXT_PURPLE)
        frameBtn.grid(row = 0, column = 1)

        self.btn_start = tk.Button(frameBtn, fg = 'purple', 
            font=FONT_HELV, command = lambda: master.switch_frame(Game), 
            width= 10, highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, 
            bd = 0, activebackground=TEXT_BLACK, cursor='target')
        self.btn_start.place(x = 18 , y=150)

        self.btn_ruler = tk.Button(frameBtn, fg = 'purple', 
            font=FONT_HELV, command = lambda: master.switch_frame(Rule), 
            width= 10, highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, 
            bd = 0, activebackground=TEXT_BLACK, cursor='target')
        self.btn_ruler.place(x = 18 , y=200)

        self.btn_setting = tk.Button(frameBtn, fg = 'purple', 
            font=FONT_HELV, command = lambda: master.switch_frame(Setting), 
            width= 10, highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, 
            bd = 0, activebackground=TEXT_BLACK, cursor='target')
        self.btn_setting.place(x = 18 , y=250)
        
        self.btn_credit = tk.Button(frameBtn, fg = 'purple', 
            font=FONT_HELV, command = lambda: master.switch_frame(Credit), 
            width= 10, highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, 
            bd = 0, activebackground=TEXT_BLACK, cursor='target')
        self.btn_credit.place(x = 18 , y=300)

        self.btn_quit = tk.Button(frameBtn, fg = 'purple', 
            font=FONT_HELV, command = self.confirmBox, 
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
    ### Run animation frames in gif file:
    def load(self, im) -> None:
        if isinstance(im, str):
            im = Image.open(im)
        frames : list = []

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
    def __init__(self, master) -> None:
        tk.Frame.__init__(self, master)
        stopTrainSound()

        ''' Start to build the game in here '''
        ##### Set canvas 
        self.tkraise()
        # self.pack_propagate(False)
        self.canvas = tk.Canvas(self, 
            height = 576, width = 1194, 
            bd = 0, bg = "#000000",
            highlightthickness = 0)
        self.bgImg = Image.open(path_background_city)
        self.bgImg = ImageTk.PhotoImage(self.bgImg)
        self.background = self.canvas.create_image(0, 260, 
            anchor = W, image = self.bgImg)
        self.canvas.pack(side=TOP,padx=0,pady=0)
        self.canvas.focus_set()

        ##### Set background
        self.trainPath = path_train_car
        self.carriagePosX = self.fullWagonPosX = 148
        self.carriagePosY = self.fullWagonPosY = 532
        self.showTrainCarriages() 
        self.showCaracterGame()

        ### button return to the menu:
        self.returnBtn = tk.Button(self.canvas, text="",
            fg = 'purple', font=FONT_HELV,
            command = lambda: master.switch_frame(MenuStartWindow),
            highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, 
            bd = 0, activebackground=TEXT_BLACK, cursor='target')
        self.returnBtn.place(x = 0, y = 0)
        self.loadTextLang()

        ### view inside train button:
        self.seekImg = Image.open(path_eye_can_look)
        self.seekImgSize = self.seekImg.resize((30, 30))
        self.unseekImg = Image.open(path_eye_can_not_look)
        self.unseekImgSize = self.unseekImg.resize((30, 30))

        self.canlookImg = ImageTk.PhotoImage(self.seekImgSize)
        self.nolookImg = ImageTk.PhotoImage(self.unseekImgSize)

        self.nolookBtn = tk.Button(self.canvas, image = self.canlookImg, 
            relief = FLAT, command = self.changeIconSeek, width=30,
            highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, bd = 0, 
            activebackground=TEXT_BLACK)
        self.nolookBtn.image = self.canlookImg
        self.nolookBtn.place(x = 1160, y = 0)

    def changeIconSeek(self) -> None:
        if self.nolookBtn.image == self.canlookImg:
            self.nolookBtn.config(image=self.nolookImg)
            self.nolookBtn.image = self.nolookImg
            self.showWagon()
        elif self.nolookBtn.image == self.nolookImg:
            self.nolookBtn.config(image=self.canlookImg)
            self.nolookBtn.image = self.canlookImg
            self.hideWagon()

    def hideWagon(self) -> None:
        del self.frames_wagon
        self.player.movement(playerPosX, playerPosY)
    
    def showWagon(self) -> None:
        self.fullWagonPosX = 148
        self.showTrainFullWagon()
        self.player.movement(-playerPosX, -playerPosY)


    def loadTextLang(self) -> None:
        if langEn and not langFr:
            self.returnBtn.config(text=english_text['return'])

        elif not langEn and langFr:
            self.returnBtn.config(text=francais_texte['return'])
    
    def showTrainCarriages(self, index:int = 0) -> None:
        self.frames : list = []
        for _numberCar in range(NB_WAGONS):
            if index >= 1: self.carriagePosX += carSizeX
            index += 1
            self.frames.append(TrainCarriage(self.canvas, 
                self.carriagePosX, self.carriagePosY, 
                self.trainPath))
    
    def showTrainFullWagon(self, index:int = 0) -> None:
        self.frames_wagon : list = []
        for _nbrWagon in range(NB_WAGONS):
            if index >= 1: self.fullWagonPosX += carSizeX
            index += 1
            self.frames_wagon.append(TrainCarriage(self.canvas, 
                self.fullWagonPosX, self.fullWagonPosY, 
                path_train_full_green))
    
    def showCaracterGame(self) -> None:
        global state
        self.player = Robbery(self, self.canvas, 
            playerPosX, playerPosY, 1)

        
class Rule(tk.Frame):
    def __init__(self, master) -> None:
        tk.Frame.__init__(self, master)
        stopTrainSound()

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
            command = lambda: master.switch_frame(MenuStartWindow),
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
    def __init__(self, master) -> None:
        tk.Frame.__init__(self, master)
        stopTrainSound()
        if unmute : creditMusic()

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
        
        ######### Print the Credit Text :
        self.x:int = 0
        self.y:int = -1
        self.speedText:int = 15
        self.scroll:int = 1
        self.nbrScroll:int = 2
        self.creditTxt = self.textCreditCV.create_text(0, 0, 
            anchor=NW, justify='center', 
            fill='purple', text=credits_text_eng, 
            font=FONT_HELV)


        #### Scroll up button:
        self.arrowUpImg = Image.open(path_arrow_icon_up)
        self.arrowUpImg = ImageTk.PhotoImage(self.arrowUpImg)
        self.arrowUpBtn = Button(self.canvas, image=self.arrowUpImg, 
            command = self.scrollUp, 
            bd = 0, bg = TEXT_PURPLE,
            activebackground=TEXT_BLACK, cursor='target',
            borderwidth=0, highlightthickness=0)
        self.arrowUpBtn.image = self.arrowUpImg

        #### Scroll down button:
        self.arrowDownImg = rotate_img(path_arrow_icon_up, 180)
        self.arrowDownImg.save("./assets/Images/arrow_down.png")
        self.arrowDownImg = ImageTk.PhotoImage(self.arrowDownImg)
        self.arrowDownBtn = Button(self.canvas, image=self.arrowDownImg, 
            command = self.scrollDown, 
            bd = 0, bg = TEXT_PURPLE,
            activebackground=TEXT_BLACK, cursor='target',
            borderwidth=0, highlightthickness=0)
        self.arrowDownBtn.image = self.arrowDownImg

        #### GitHub project button:
        self.githubImg = Image.open(path_github_icon)
        self.githubImg = self.githubImg.resize((50, 50))
        self.githubImg = ImageTk.PhotoImage(self.githubImg)
        self.githubBtn = Button(self.canvas, image=self.githubImg, 
            command = self.openGitHub, 
            bd = 0, bg = TEXT_PURPLE,
            activebackground=TEXT_BLACK, cursor='target',
            borderwidth=0, highlightthickness=0)
        self.githubBtn.image = self.githubImg
        
        ### Return button:
        self.new = 1
        self.returnBtn = tk.Button(self.canvas, text="",
            fg = 'purple', font=FONT_HELV,
            command = lambda: master.switch_frame(MenuStartWindow),
            highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, 
            bd = 0, activebackground=TEXT_BLACK, cursor='target')
        self.returnBtn.place(x = 0, y = 0)

        self.canvasMove()
        self.loadTextLang()
    
    def loadTextLang(self) -> None:
        if langEn and not langFr:
            self.returnBtn.config(text=english_text['return'])
            self.textCreditCV.itemconfig(self.creditTxt, text = credits_text_eng)

        elif not langEn and langFr:
            self.returnBtn.config(text=francais_texte['return'])
            self.textCreditCV.itemconfig(self.creditTxt, text = credits_text_fr)


    def canvasMove(self, index:int = 0) -> None:
        self.textCreditCV.move(self.creditTxt, self.x, self.y)
        index += self.scroll
        if index == 940 and self.nbrScroll > 0:
            self.y = 0; self.arrowUpBtn.place(x = 0, y = 60)
            self.scroll = 0; self.nbrScroll -= 1
        if index == 0: 
            self.y = 0; self.arrowDownBtn.place(x = 0, y = 60)
            self.scroll = 0; self.nbrScroll -= 1
        if index > 950: 
            self.y = 0; self.scroll = 0; 
            self.githubBtn.place(x = 0, y = 60)
        self.textCreditCV.after(self.speedText, self.canvasMove, index)
    
    def scrollUp(self) -> None:
        self.arrowUpBtn.destroy()
        self.y = 1; self.scroll = -1
    def scrollDown(self) -> None:
        self.arrowDownBtn.destroy()
        self.y = -1; self.scroll = 1
    def openGitHub(self) -> None:
        webbrowser.open(url_github_project, new = self.new)


class Setting(tk.Frame):
    def __init__(self, master) -> None:
        tk.Frame.__init__(self, master)
        stopTrainSound()

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
            bd = 0, bg ='black', relief=None, 
            anchor=W, justify=LEFT)
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
            bd = 0, bg ='black', relief=None, 
            anchor=W, justify=LEFT)
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
            bd = 0, bg ='black', relief=None, 
            anchor=W, justify=LEFT)
        self.muteLbl.grid(row=4, column=0, sticky=W)

        self.musicBtnZone = tk.Frame(self, bg = '#000000', width=128, height=23)
        self.musicBtnZone.grid(row=4, column=1, sticky=W)

        self.playImg = Image.open(path_vol_icon_play)
        self.playImgSize = self.playImg.resize((23, 23))
        self.pauseImg = Image.open(path_vol_icon_pause)
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
            command = self.applyChange,
            highlightbackground='#76428A', bg=TEXT_PURPLE, bd = 0, 
            activebackground=TEXT_BLACK)
        self.applyBtn.grid(row = 6, column = 0, sticky=W)

        self.returnBtn = tk.Button(self, text=english_text['return'], width = 9,
            fg = 'purple', font=FONT_HELV,
            command = lambda: master.switch_frame(MenuStartWindow),
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
                message=f"You selected {self.langTxt.get()}!\
                    Press 'Apply' to load the language !"
            )
        
        elif not langEn and langFr:
            messagebox.showinfo(
                title='Langue Notification',
                message=f"Vous avez sélectionné {self.langTxt.get()}!\
                    Appuyez sur 'Appliquer' pour charger la langue !"
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


class TrainCarriage(): 
    def __init__(self, canvas:Canvas, x:int, y:int, photo) -> None:
        self.canvas = canvas
        self.x = x
        self.y = y
        self.photo = photo
        self.trainImg()

    def trainImg(self) -> None:
        self.image = Image.open(self.photo)
        self.imageSize=self.image.resize(
            (carSizeX, carSizeY), 
            Image.ANTIALIAS)
        self.trainImage = ImageTk.PhotoImage(self.imageSize)
        self.trainCarImg = self.canvas.create_image(
            self.x, self.y, 
            image = self.trainImage)


class Robbery(): 
    def __init__(self, parent, can:Canvas, pl_x:int, pl_y:int, position:int):
        self.parent = parent
        self.can = can
        self.pl_x = pl_x
        self.pl_y = pl_y

        self.position = position
        self.position_y = 1
        self.dirct = 1
        self.playerIdle()
        print(self.can.coords(self.img_j))

    def movement(self, x, y) -> None:
        self.can.move(self.img_j, x, y)
        self.pl_x = x
        self.pl_y = y
    
    def fire(self, target):
        if self.dirct==1:
            if (self.can.coords(self.img_j)[0] - target.can.coords( target.img_j)[0]) < 0 and self.position_y== target.position_y:
                print((self.can.coords(self.img_j)[0] - target.can.coords( target.img_j)[0]))

            else :
                print((self.can.coords(self.img_j)[0] -  target.can.coords( target.img_j)[0]))
        else:

            if (self.can.coords(self.img_j)[0] - target.can.coords( target.img_j)[0])>0 and self.position_y== target.position_y:
                print((self.can.coords(self.img_j)[0] - target.can.coords( target.img_j)[0]))

            else :
                print((self.can.coords(self.img_j)[0]-  target.can.coords( target.img_j)[0]))

    def playerIdle(self, item = None, index:int = 1) -> None:
        self.can.delete(item)

        if self.dirct == 1:
            playerImgIdle = self.can.playerImgIdle = PhotoImage(file = path_thief_IdleRight + str(index) + '.png')
        else:
            playerImgIdle = self.can.playerImgIdle = PhotoImage(file = path_thief_IdleLeft + str(index) + '.png')
        self.img_j = item = self.can.create_image(self.pl_x, self.pl_y, image = playerImgIdle)
        index += 1
        if index == 10: index = 1

        if state == str(playerState[0]):
            self.can.after(100, self.playerIdle, item, index)
        elif state == str(playerState[1]):
            self.can.delete(item)
            self.playerWalk()
    
    def playerWalk(self, item = None, index:int = 1) -> None:
        self.can.delete(item)

        if self.dirct == 1:
            playerImgWalk = self.can.playerImgWalk = PhotoImage(file = path_thief_WalkRight + str(index) + '.png')
        else:
            playerImgWalk = self.can.playerImgWalk = PhotoImage(file = path_thief_WalkLeft + str(index) + '.png')
        self.img_j = item = self.can.create_image(self.pl_x, self.pl_y, image = playerImgWalk)
        index += 1
        if index == 10: index = 1
        
        if state == str(playerState[1]):
            self.can.after(100, self.playerWalk, item, index)
        elif state == str(playerState[0]):
            self.can.delete(item)
            self.playerIdle()


## Sounds
def trainSound() -> None:
    train_sound.play(-1)
    train_sound.set_volume(volume_sound)
def stopTrainSound() -> None:
    train_sound.stop()
def creditMusic() -> None:
    credit_music.play(-1)
    credit_music.set_volume(volume_sound / 2.0)
def stopCreditMusic() -> None:
    credit_music.stop()
def clickSound() -> None:
    click_sound.play(1)
    click_sound.set_volume(0.2)


#### window setting function
def startMenuGame() -> None:
    startMenu = Window()
    startMenu.title('Colt Express')
    startMenu.iconphoto(False, PhotoImage(file= path_sack_icon))
    startMenu.wm_attributes("-topmost", 1)
    startMenu.bind('<Escape>', lambda event: startMenu.quit())
    startMenu.mainloop()


#### edit images
def rotate_img(img_path, rt_degr) -> None:
    img = Image.open(img_path)
    return img.rotate(rt_degr, expand=1)


#### main function:
def main(args) -> None:
    startMenuGame()


if __name__ == '__main__':

    #### Load sounds
    pygame.mixer.init()
    train_sound = pygame.mixer.Sound(path_train_sound)
    credit_music = pygame.mixer.Sound(path_credit_menu_music)
    click_sound = pygame.mixer.Sound(path_click_sound)

    ##### main
    main(sys.argv)



# !/usr/bin/python3
import sys, pygame, webbrowser
import tkinter as tk
from itertools import count, cycle
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from settings import *
from random import *


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
            font=FONT_HELV, command = lambda: self.startGame(master), 
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
        if setLang == int(langList[0]):
            self.btn_start.config(text=english_text['play'])
            self.btn_ruler.config(text=english_text['rule'])
            self.btn_setting.config(text=english_text['setting'])
            self.btn_credit.config(text=english_text['credit'])
            self.btn_quit.config(text=english_text['quit'])
        
        elif setLang == int(langList[1]):
            self.btn_start.config(text=francais_texte['play'])
            self.btn_ruler.config(text=francais_texte['rule'])
            self.btn_setting.config(text=francais_texte['setting'])
            self.btn_credit.config(text=francais_texte['credit'])
            self.btn_quit.config(text=francais_texte['quit'])
        
        elif setLang == int(langList[2]):
            self.btn_start.config(text=vietnamese_text['play'])
            self.btn_ruler.config(text=vietnamese_text['rule'])
            self.btn_setting.config(text=vietnamese_text['setting'])
            self.btn_credit.config(text=vietnamese_text['credit'])
            self.btn_quit.config(text=vietnamese_text['quit'])
    
    def startGame(self, master) -> None:
        master.switch_frame(Game)
        print('Welcome')
    
    def confirmBox(self) -> None:
        if unmute: clickSound()
        if setLang == int(langList[0]):
            confirm = messagebox.askquestion('Confirm Box', 
            english_text['confirm_quit'], 
            icon='warning')
            if confirm == 'yes':
                self.quit()

        elif setLang == int(langList[1]):
            confirm = messagebox.askquestion('Confirm Box', 
            francais_texte['confirm_quit'], 
            icon='warning')
            if confirm == 'yes':
                self.quit()
        
        elif setLang == int(langList[2]):
            confirm = messagebox.askquestion('Confirm Box', 
            vietnamese_text['confirm_quit'],
            icon='warning')
            if confirm == 'yes':
                self.quit()
        

class ImageLabel(tk.Label):
    ### Run animation frames in gif file:
    def load(self, im:str) -> None:
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
        self.bg_x = -5
        self.bg_y = 0
        self.canvas = tk.Canvas(self, 
            height = 576, width = 1194, 
            bd = 0, bg = "#000000",
            highlightthickness = 0)
        self.bgImg = ImageTk.PhotoImage(Image.open(path_background_city).resize((5466, 328)))
        self.background = self.canvas.create_image(0, 260, 
            anchor = W, image = self.bgImg)
        self.canvas.pack(side=TOP,padx=0,pady=0)
        self.canvas.focus_set()
        self.runningTrain()
        

        ##### Set background
        self.trainPath = path_train_car
        self.setDefaultTrain()
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
        self.canlookImg = ImageTk.PhotoImage(Image.open(path_eye_can_look).resize((30, 30)))
        self.nolookImg = ImageTk.PhotoImage(Image.open(path_eye_can_not_look).resize((30, 30)))

        self.nolookBtn = tk.Button(self.canvas, image = self.canlookImg, 
            relief = FLAT, command = self.changeIconSeek, width=30,
            highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, bd = 0, 
            activebackground=TEXT_BLACK)
        self.nolookBtn.image = self.canlookImg
        self.nolookBtn.place(x = 1160, y = 0)

        ### button set number wagon
        self.plusImg = ImageTk.PhotoImage(Image.open(path_plus_icon).resize((20, 20)))
        self.minusImg = ImageTk.PhotoImage(Image.open(path_minus_icon).resize((20, 20)))

        self.minusBtn = tk.Button(self.canvas, image = self.plusImg, 
            relief = FLAT, command = self.setNbrWagon, width=30,
            highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, bd = 0, 
            activebackground=TEXT_BLACK)
        self.minusBtn.image = self.plusImg
        self.minusBtn.place(x = 1125, y = 5)
        self.loadgameData()

        self.canvas.bind('<KeyPress-Left>', lambda e: self.player.movement(playerPosX + 40, playerPosY))

    def changeIconSeek(self) -> None:
        if self.nolookBtn.image == self.canlookImg and not canSeek:
            self.nolookBtn.config(image=self.nolookImg)
            self.nolookBtn.image = self.nolookImg
            self.showWagon()
        elif self.nolookBtn.image == self.nolookImg and canSeek:
            self.nolookBtn.config(image=self.canlookImg)
            self.nolookBtn.image = self.canlookImg
            self.hideWagon()
    
    def setNbrWagon(self) -> None:
        global nb_wagons, canPlusWG
        if self.minusBtn.image == self.plusImg and canPlusWG:
            nb_wagons += 1; self.refreshTrain()
            canPlusWG = False
        elif self.minusBtn.image == self.minusImg and not canPlusWG:
            nb_wagons -= 1; self.refreshTrain()
            canPlusWG = True
        self.changeIconMinus()

    def changeIconMinus(self) -> None:
        if not canPlusWG: 
            self.minusBtn.config(image=self.minusImg)
            self.minusBtn.image = self.minusImg
        else: 
            self.minusBtn.config(image=self.plusImg)
            self.minusBtn.image = self.plusImg

    def refreshTrain(self) -> None:
        global canAnimate, playerPosX, playerPosY, playerSizeX, playerSizeY
        global carSizeX, carSizeY, fullSizeX
        del self.frames
        if showFull: 
            self.nolookBtn.config(image=self.canlookImg)
            self.nolookBtn.image = self.canlookImg
            self.hideWagon()
        if nb_wagons == 4: 
            carSizeX = 298; carSizeY = 85; fullSizeX = 148
            self.carriagePosX = self.fullWagonPosX = fullSizeX
            self.carriagePosY = self.fullWagonPosY = 532
            if not outsideTrain: playerPosY += 14
            playerPosX -= 30
            playerSizeX = playerSizeY = 32
        elif nb_wagons == 3:
            carSizeX = 400; carSizeY = 120; fullSizeX = 195
            self.carriagePosX = self.fullWagonPosX = fullSizeX
            self.carriagePosY = self.fullWagonPosY = 518
            if not outsideTrain: playerPosY -= 14
            playerPosX +=30
            playerSizeX = playerSizeY = 48
        self.showTrainCarriages()
        self.player.movement(playerPosX, playerPosY)


    def hideWagon(self) -> None:
        global canSeek, showFull
        del self.frames_wagon
        self.player.movement(playerPosX, playerPosY)
        canSeek = False; showFull = False
    
    def showWagon(self) -> None:
        global canSeek, showFull
        self.fullWagonPosX = fullSizeX
        self.showTrainFullWagon()
        self.player.movement(-playerPosX, -playerPosY)
        canSeek = True; showFull = True

    def loadTextLang(self) -> None:
        if setLang == int(langList[0]):
            self.returnBtn.config(text=english_text['return'])

        elif setLang == int(langList[1]):
            self.returnBtn.config(text=francais_texte['return'])
        
        elif setLang == int(langList[2]):
            self.returnBtn.config(text=vietnamese_text['return'])
    
    def setDefaultTrain(self) -> None:
        global carSizeX, carSizeY, fullSizeX
        global playerPosX, playerPosY, playerSizeX, playerSizeY
        if nb_wagons == 4: 
            carSizeX = 298; carSizeY = 85; fullSizeX = 148
            self.carriagePosX = self.fullWagonPosX = fullSizeX
            self.carriagePosY = self.fullWagonPosY = 532
            if not saveGame:
                if not outsideTrain: playerPosY = 533
                playerPosX = 80
                playerSizeX = playerSizeY = 32
        elif nb_wagons == 3:
            carSizeX = 400; carSizeY = 120; fullSizeX = 195
            self.carriagePosX = self.fullWagonPosX = fullSizeX
            self.carriagePosY = self.fullWagonPosY = 518
            if not saveGame:
                if not outsideTrain: playerPosY = 519
                playerPosX = 110
                playerSizeX = playerSizeY = 48
        
    
    def showTrainCarriages(self, index:int = 0) -> None:
        self.frames : list = []
        for _numberCar in range(nb_wagons):
            if index >= 1: self.carriagePosX += carSizeX
            index += 1
            self.frames.append(TrainCarriage(self.canvas, 
                self.carriagePosX, self.carriagePosY, 
                carSizeX, carSizeY,
                self.trainPath))
    
    def showTrainFullWagon(self, index:int = 0) -> None:
        self.frames_wagon : list = []
        for _nbrWagon in range(nb_wagons):
            if index >= 1: self.fullWagonPosX += carSizeX
            index += 1
            self.frames_wagon.append(TrainCarriage(self.canvas, 
                self.fullWagonPosX, self.fullWagonPosY, 
                carSizeX, carSizeY,
                path_train_full_green))
    
    def showCaracterGame(self) -> None:
        global canAnimate
        self.player = Player(self, self.canvas, 
            playerPosX, playerPosY, 1)
        canAnimate = True
    
    def runningTrain(self) -> None:
        self.canvas.move(self.background, self.bg_x, self.bg_y)
        # print(self.canvas.coords(self.background)[0])
        if self.canvas.coords(self.background)[0] <= -4000:
            self.canvas.delete(self.background)
            self.background = self.canvas.create_image(0, 260, 
                anchor = W, image = self.bgImg)
        self.canvas.after(10, self.runningTrain)
    
    def loadgameData(self) -> None:
        if canSeek:
            self.nolookBtn.config(image=self.nolookImg)
            self.nolookBtn.image = self.nolookImg
            self.showWagon()
        self.changeIconMinus()

        
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


        #### return to the start menu button:
        self.returnBtn = tk.Button(self.canvas, text="",
            fg = 'purple', font=FONT_HELV,
            command = lambda: master.switch_frame(MenuStartWindow),
            highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, 
            bd = 0, activebackground=TEXT_BLACK, cursor='target')
        self.returnBtn.place(x = 0, y = 0)

        self.loadTextLang()
    
    def loadTextLang(self) -> None:
        if setLang == int(langList[0]):
            self.returnBtn.config(text=english_text['return'])

        elif setLang == int(langList[1]):
            self.returnBtn.config(text=francais_texte['return'])
        
        elif setLang == int(langList[2]):
            self.returnBtn.config(text=vietnamese_text['return'])


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
        if setLang == int(langList[0]):
            self.returnBtn.config(text=english_text['return'])
            self.textCreditCV.itemconfig(self.creditTxt, text = credits_text_eng)

        elif setLang == int(langList[1]):
            self.returnBtn.config(text=francais_texte['return'])
            self.textCreditCV.itemconfig(self.creditTxt, text = credits_text_fr)
        
        elif setLang == int(langList[2]):
            self.returnBtn.config(text=vietnamese_text['return'])
            self.textCreditCV.itemconfig(self.creditTxt, text = credits_text_vn)


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
            values=listCBLangEN, width=14)
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

        self.unmuteImg = ImageTk.PhotoImage(Image.open(path_vol_icon_play).resize((23, 23)))
        self.muteImg = ImageTk.PhotoImage(Image.open(path_vol_icon_pause).resize((23, 23)))

        self.muteBtn = tk.Button(self.musicBtnZone, image = self.unmuteImg, 
            relief = FLAT, command = self.changeIcon, width=30,
            highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, bd = 0, 
            activebackground=TEXT_BLACK)
        self.muteBtn.image = self.unmuteImg
        self.muteBtn.place(x = 47, y = 0)

        ### Buttons to change the value of scale sound
        self.minusImg = ImageTk.PhotoImage(Image.open(path_minus_icon).resize((23, 23)))
        self.decreaseScaleVar = tk.Button(self.musicBtnZone, image = self.minusImg, 
            width=30, relief = FLAT, command = self.decreaseSoundScale,
            highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, bd = 0, 
            activebackground=TEXT_BLACK)
        self.decreaseScaleVar.image = self.minusImg
        self.decreaseScaleVar.place(x = 0, y = 0)
        
        self.plusImg = ImageTk.PhotoImage(Image.open(path_plus_icon).resize((23, 23)))
        self.increaseScaleVar = tk.Button(self.musicBtnZone, image=self.plusImg, 
            width=30, relief = FLAT, command = self.increaseSoundScale,
            highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, bd = 0, 
            activebackground=TEXT_BLACK)
        self.increaseScaleVar.image = self.minusImg
        self.increaseScaleVar.place(x = 93, y = 0)
        
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
        if setLang == int(langList[0]):
            self.title.config(text = english_text['setting'].upper() + ':')
            self.langLbl.config(text= english_text['language'] + ' : ')
            self.soundLbl.config(
                text=f"{english_text['setting']} \n{english_text['volume']} : "
            )
            self.applyBtn.config(text=english_text['apply'])
            self.returnBtn.config(text=english_text['return'])
            self.langBox.delete(0,'end')
            self.langBox['values'] = listCBLangEN
        
        elif setLang == int(langList[1]):
            self.title.config(text = francais_texte['setting'])
            self.langLbl.config(text= francais_texte['language'] + ' : ')
            self.soundLbl.config(
                text=f"{francais_texte['setting']} \n{francais_texte['volume']} : "
            )
            self.applyBtn.config(text=francais_texte['apply'])
            self.returnBtn.config(text=francais_texte['return'])
            self.langBox.delete(0,'end')
            self.langBox['values'] = listCBLangFR
        
        elif setLang == int(langList[2]):
            self.title.config(text = vietnamese_text['setting'] + ':')
            self.langLbl.config(text= vietnamese_text['language'] + ' : ')
            self.soundLbl.config(
                text=f"{vietnamese_text['setting']} \n{vietnamese_text['volume']} : "
            )
            self.applyBtn.config(text=vietnamese_text['apply'])
            self.returnBtn.config(text=vietnamese_text['return'])
            self.langBox.delete(0,'end')
            self.langBox['values'] = listCBLangVN
    
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
        self.langBox.current(setLang)

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
        if setLang == int(langList[0]):
            messagebox.showinfo(
                title='Language Notification',
                message=f"You selected {self.langTxt.get()}!\n"+english_text['lang_not']
            )
        
        elif setLang == int(langList[1]):
            messagebox.showinfo(
                title='Langue Notification',
                message=f"Vous avez sélectionné {self.langTxt.get()}!\n"+francais_texte['lang_not']
            )

        elif setLang == int(langList[2]):
            messagebox.showinfo(
                title='Thông báo ngôn ngữ',
                message=f"Bạn đã chọn {self.langTxt.get()}!\n"+vietnamese_text['lang_not']
            )
        
    def applyChange(self) -> None:
        if unmute: clickSound()
        global setLang
        global volume, volume_sound

        ##### apply language
        setLang = int(langList[int(self.langBox.current())])
        print(str(self.langBox.get()))
        
        self.loadTextLang()
        ##### apply volume
        volume = float(self.scaleVar.get())
        volume_sound = (volume) / 100.0
        print("Volume scale after apply: ", volume)
        print("Volume sound after apply: ", volume_sound)

        if unmute: print('unmute\n')
        elif not unmute: print('mute\n')


class TrainCarriage(): 
    def __init__(self, canvas:Canvas, x:int, y:int, size_x:int, size_y:int, photo) -> None:
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.photo = photo
        self.trainImg()

    def trainImg(self) -> None:
        self.image = Image.open(self.photo)
        self.imageSize=self.image.resize(
            (self.size_x, self.size_y), 
            Image.ANTIALIAS)
        self.trainImage = ImageTk.PhotoImage(self.imageSize)
        self.trainCarImg = self.canvas.create_image(
            self.x, self.y, 
            image = self.trainImage)


class Items():
    def __init__(self, canvas:Canvas, x:int, y:int, size_x:int, size_y:int, price:int, photo) -> None:
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.price = price
        self.photo = photo
        print(self.canvas.coords(self.photo))
        self.showItems()

    def showItems(self) -> None:
        self.itemImg = ImageTk.PhotoImage(Image.open(self.photo).resize((self.size_x, self.size_y), Image.ANTIALIAS))
        self.showItem = self.canvas.create_image(self.x, self.y, image=self.itemImg)


class Player(): 
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
            playerImgIdle = self.can.playerImgIdle = ImageTk.PhotoImage(Image.open( path_thief_IdleRight + str(index) + '.png').resize((playerSizeX, playerSizeY)))
        else:
            playerImgIdle = self.can.playerImgIdle = ImageTk.PhotoImage(Image.open( path_thief_IdleLeft + str(index) + '.png').resize((playerSizeX, playerSizeY)))
        item = self.can.create_image(self.pl_x, self.pl_y, image = playerImgIdle)
        self.img_j =  item
        index += 1
        if index == 10: index = 1

        if canAnimate:
            if state == str(playerState[0]):
                self.can.after(100, self.playerIdle, item, index)
            elif state == str(playerState[1]):
                self.can.delete(item)
                self.playerWalk()
    
    def playerWalk(self, item = None, index:int = 1) -> None:
        self.can.delete(item)

        if self.dirct == 1:
            playerImgWalk = self.can.playerImgWalk = ImageTk.PhotoImage(Image.open( path_thief_WalkRight + str(index) + '.png').resize((playerSizeX, playerSizeY)))
        else:
            playerImgWalk = self.can.playerImgWalk = ImageTk.PhotoImage(Image.open( path_thief_WalkLeft + str(index) + '.png').resize((playerSizeX, playerSizeY)))
        item = self.can.create_image(self.pl_x, self.pl_y, image = playerImgWalk)
        self.img_j = item
        index += 1
        if index == 10: index = 1
        
        if canAnimate:
            if state == str(playerState[1]):
                self.can.after(100, self.playerWalk, item, index)
            elif state == str(playerState[0]):
                self.can.delete(item)
                self.playerIdle()


class ActionBtn(Button):
    def __init__(self, window : Tk, player, target, direction, imgBtn):
        super().__init__(window, width=50, height=50, 
            highlightbackground=TEXT_PURPLE, bg=TEXT_PURPLE, 
            bd = 0, activebackground=TEXT_BLACK, cursor='target')
        self.fenetre = window
        self.target = target
        self.imgBtn = imgBtn
        self.image = ImageTk.PhotoImage(Image.open(imgBtn).resize((50, 50)))
        self.config(image = self.image)
        self.player = player
        self.direction = direction
    
        if self.direction == "right":
            self.config(command=self.goRight)
        elif self.direction == "left":
            self.config(command=self.goLeft)
        elif self.direction == "up":
            self.config(command=self.goUp)
        elif self.direction == "attack":
            self.config(command=self.attack)
    
    def goRight(self) -> None:
        pass

    def goLeft(self) -> None:
        pass

    def goUp(self) -> None:
        pass

    def attack(self) -> None:
        pass



class Clouds():
    def __init__(self,parent,canvas):
        self.parent = parent                    
        self.canvas = canvas                                     
        self.fallSpeed = 50                          
        self.yPosition = randint(0, 370)        
        self.xPosition = randint(1900,2200)
        self.isgood = randint(0, 1)             
        self.vitesse = randint(-25,-10) 
        self.goodItems = [path_cloud_bg, path_cloud_2_bg]
        
        # create falling items
        self.itemPhoto = PhotoImage(file = "{}" .format( choice(self.goodItems) ) )
        self.fallItem = self.canvas.create_image( (self.xPosition ,self.yPosition) , image=self.itemPhoto , tag="good" )
            
        # trigger falling item movement
        self.placement_dc()
        
    def placement_dc(self):
        # dont move x, move y
        self.canvas.move(self.fallItem, self.vitesse, 0)
        
        if (self.canvas.coords(self.fallItem)[0] < -100):
            self.canvas.delete(self.fallItem)                                           
        else:
            self.parent.after(self.fallSpeed, self.placement_dc)   


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


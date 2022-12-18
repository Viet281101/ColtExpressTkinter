
# !/usr/bin/python3
import sys, pygame, webbrowser
import tkinter as tk
from itertools import count, cycle
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.colorchooser import askcolor
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
        self.tkraise()
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
        frameBtn = tk.Frame(self,width = 170, height = 576, bg=bg_color)
        frameBtn.grid(row = 0, column = 1)

        self.btn_start = tk.Button(frameBtn, fg = text_color, 
            font=FONT_HELV, command = lambda: self.startGame(master), 
            width= 10, highlightbackground=bg_color, bg=bg_color, 
            bd = 0, activebackground=TEXT_PURPLE, cursor='target')
        self.btn_start.place(x = 18 , y=150)

        self.btn_ruler = tk.Button(frameBtn, fg = text_color, 
            font=FONT_HELV, command = lambda: master.switch_frame(Rule), 
            width= 10, highlightbackground=bg_color, bg=bg_color, 
            bd = 0, activebackground=TEXT_PURPLE, cursor='target')
        self.btn_ruler.place(x = 18 , y=200)

        self.btn_setting = tk.Button(frameBtn, fg = text_color, 
            font=FONT_HELV, command = lambda: master.switch_frame(Setting), 
            width= 10, highlightbackground=bg_color, bg=bg_color, 
            bd = 0, activebackground=TEXT_PURPLE, cursor='target')
        self.btn_setting.place(x = 18 , y=250)
        
        self.btn_credit = tk.Button(frameBtn, fg = text_color, 
            font=FONT_HELV, command = lambda: master.switch_frame(Credit), 
            width= 10, highlightbackground=bg_color, bg=bg_color, 
            bd = 0, activebackground=TEXT_PURPLE, cursor='target')
        self.btn_credit.place(x = 18 , y=300)

        self.btn_quit = tk.Button(frameBtn, fg = text_color, 
            font=FONT_HELV, command = self.confirmBox, 
            width= 10, highlightbackground=bg_color, bg=bg_color, 
            bd = 0, activebackground=TEXT_PURPLE, cursor='target')
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
        self.bg_x : int = -5
        self.bg_y : int = 0
        self.actState : int = 0
        self.canvas = tk.Canvas(self, 
            height = 576, width = 1194, 
            bd = 0, bg = "#000000",
            highlightthickness = 0)
        self.bgImg = ImageTk.PhotoImage(Image.open(path_background_city).resize((5466, 328)))
        self.background = self.canvas.create_image(0, 260, 
            anchor = W, image = self.bgImg)
        self.canvas.pack(side=TOP,padx=0,pady=0)
        self.canvas.focus_set()
        
        ##### Set background
        self.trainPath = path_train_car
        self.createClouds()
        self.setDefaultTrain()
        self.showTrainCarriages() 
        self.showCaracterGame()

        ### button return to the menu:
        self.returnBtn = tk.Button(self.canvas, text="",
            fg = text_color, font=FONT_HELV,
            command = lambda: master.switch_frame(MenuStartWindow),
            highlightbackground=bg_color, bg=bg_color, 
            bd = 0, activebackground=TEXT_PURPLE, cursor='target')
        self.returnBtn.place(x = 0, y = 0)

        ### start to play:
        self.startBtn = tk.Button(self.canvas, text="",
            fg = text_color, font=FONT_HELV,
            command = self.startGamePlay,
            highlightbackground=bg_color, bg=bg_color, 
            bd = 0, activebackground=TEXT_PURPLE, cursor='target')
        self.startBtn.place(x = 200, y = 0)

        ### view current action in state:
        self.currentActLbl = tk.Label(self.canvas, text="",
            fg = text_color, font=FONT_HELV,
            highlightbackground=bg_color, bg=bg_color, 
            bd = 0, activebackground=TEXT_PURPLE, cursor='target')
        self.currentActLbl.place(x = 450, y = 5)

        ### view information menu:
        self.infoIcon = ImageTk.PhotoImage(Image.open(path_info_icon).resize((30, 30)))
        self.infoBtn = tk.Button(self.canvas, image = self.infoIcon, 
            relief = FLAT, command = lambda: master.switch_frame(MenuInfo), width=30,
            highlightbackground=bg_color, bg=bg_color, bd = 0, 
            activebackground=TEXT_PURPLE)
        self.infoBtn.image = self.infoIcon
        self.infoBtn.place(x = 1125, y = 0)

        ### pause game button:
        self.pauseImg = ImageTk.PhotoImage(Image.open(path_pause_icon).resize((30, 30)))
        self.unpauseImg = ImageTk.PhotoImage(Image.open(path_unpause_icon).resize((30, 30)))

        self.unpauseBtn = tk.Button(self.canvas, image = self.pauseImg, 
            relief = FLAT, command = self.pauseGame, width=30,
            highlightbackground=bg_color, bg=bg_color, bd = 0, 
            activebackground=TEXT_PURPLE)
        self.unpauseBtn.image = self.pauseImg
        self.unpauseBtn.place(x = 1160, y = 0)

        ### view inside train button:
        self.canlookImg = ImageTk.PhotoImage(Image.open(path_eye_can_look).resize((30, 30)))
        self.nolookImg = ImageTk.PhotoImage(Image.open(path_eye_can_not_look).resize((30, 30)))

        self.nolookBtn = tk.Button(self.canvas, image = self.canlookImg, 
            relief = FLAT, command = self.changeIconSeek, width=30,
            highlightbackground=bg_color, bg=bg_color, bd = 0, 
            activebackground=TEXT_PURPLE)
        self.nolookBtn.image = self.canlookImg
        self.nolookBtn.place(x = 1090, y = 0)

        ### button set number wagon
        self.plusImg = ImageTk.PhotoImage(Image.open(path_plus_icon).resize((20, 20)))
        self.minusImg = ImageTk.PhotoImage(Image.open(path_minus_icon).resize((20, 20)))

        self.minusBtn = tk.Button(self.canvas, image = self.plusImg, 
            relief = FLAT, command = self.setNbrWagon, width=30,
            highlightbackground=bg_color, bg=bg_color, bd = 0, 
            activebackground=TEXT_PURPLE)
        self.minusBtn.image = self.plusImg
        self.minusBtn.place(x = 1055, y = 5)
        self.loadgameData()
        self.loadTextLang()
        self.runningTrain()

        ### test key move:
        self.canvas.bind('<KeyPress-Left>', lambda e: self.player.testMoveLeftKey(e))
        self.canvas.bind('<KeyPress-Right>', lambda e: self.player.testMoveRightKey(e))
        self.canvas.bind('<KeyPress-Up>', lambda e: self.player.testMoveUpKey(e))
        self.canvas.bind('<KeyPress-Down>', lambda e: self.player.testMoveDownKey(e))
        self.canvas.bind('<x>', lambda e: self.player.testStopKey(e))

    def changeIconSeek(self) -> None:
        if not playerMove:
            if self.nolookBtn.image == self.canlookImg and not canSeek:
                self.nolookBtn.config(image=self.nolookImg)
                self.nolookBtn.image = self.nolookImg
                self.showWagon()
            elif self.nolookBtn.image == self.nolookImg and canSeek:
                self.nolookBtn.config(image=self.canlookImg)
                self.nolookBtn.image = self.canlookImg
                self.hideWagon()
    
    def pauseGame(self) -> None:
        global pauseGame
        if self.unpauseBtn.image == self.pauseImg:
            self.unpauseBtn.config(image=self.unpauseImg)
            self.unpauseBtn.image = self.unpauseImg
            pauseGame = True
        elif self.unpauseBtn.image == self.unpauseImg:
            self.unpauseBtn.config(image=self.pauseImg)
            self.unpauseBtn.image = self.pauseImg
            pauseGame = False

    def startGamePlay(self) -> None:
        global startTheGame, startPlanning, pauseGame, planningList, canClicAct
        if canClicAct:
            if not startTheGame and not startPlanning:
                startTheGame = True
                self.loadTextLang()
                self.minusBtn.destroy()
                self.createItems()
            elif startTheGame and not startPlanning:
                self.loadTextLang()
                self.planning = PlanningWindow(self)
                pauseGame = True
            elif startTheGame and startPlanning:
                canClicAct = False
                self.makeActFromList(planningList[self.actState])
                self.currentActLbl.config(text=planningList[self.actState])
                self.actState += 1
                if self.actState >= nb_actions: 
                    planningList.clear()
                    startPlanning = False
                    self.actState = 0
    
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
            else: playerPosY += 40
            playerPosX -= 30
            playerSizeX = playerSizeY = 32
        elif nb_wagons == 3:
            carSizeX = 400; carSizeY = 120; fullSizeX = 195
            self.carriagePosX = self.fullWagonPosX = fullSizeX
            self.carriagePosY = self.fullWagonPosY = 518
            if not outsideTrain: playerPosY -= 14
            else: playerPosY -= 40
            playerPosX += 30
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
            if not startTheGame and not startPlanning:
                self.startBtn.config(text=english_text['start'].upper())
            elif startTheGame and not startPlanning:
                self.startBtn.config(text=english_text['planning'] + " the " + english_text['action'] +"s")
            else: self.startBtn.config(text=english_text['action'].upper())

        elif setLang == int(langList[1]):
            self.returnBtn.config(text=francais_texte['return'])
            if not startTheGame and not startPlanning:
                self.startBtn.config(text=francais_texte['start'].upper())
            elif startTheGame and not startPlanning:
                self.startBtn.config(text=francais_texte['planning'] + " les " + francais_texte['action']+"s")
            else: self.startBtn.config(text=francais_texte['action'].upper())
        
        elif setLang == int(langList[2]):
            self.returnBtn.config(text=vietnamese_text['return'])
            if not startTheGame and not startPlanning:
                self.startBtn.config(text=vietnamese_text['start'].upper())
            elif startTheGame and not startPlanning:
                self.startBtn.config(text=vietnamese_text['planning'] + " " + vietnamese_text['action'])
            else: self.startBtn.config(text=vietnamese_text['action'].upper())
    
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
        self.player = Player(self, self.canvas, 
            playerPosX, playerPosY, 1)
    
    def createItems(self) -> None:
        self.gems : list = []
        for _nbrItems in range(randint(1, 5)):
            self.gems.append(Items(self.canvas, self.player, 
            gemsPosY, gemsPosX, 14, 14, 500, choice(gems)))
    
    def runningTrain(self) -> None:
        if not pauseGame:
            self.canvas.move(self.background, self.bg_x, self.bg_y)
            # print(self.canvas.coords(self.background)[0])
            if self.canvas.coords(self.background)[0] <= -4000:
                self.canvas.delete(self.background)
                self.background = self.canvas.create_image(0, 260, 
                    anchor = W, image = self.bgImg)
        self.loadTextLang()
        if canRobItem and playerPosX == gemsPosX: del self.gems
        self.canvas.after(10, self.runningTrain)

    def createClouds(self) -> None:
        if not pauseGame: Clouds(self, self.canvas)
        self.after(900, self.createClouds)
    
    def makeActFromList(self, act:str) -> None:
        if act == "Move Left": self.player.playerMoveLeft()
        elif act == "Move Right": self.player.playerMoveRight()
        elif act == "Move Up": self.player.playerMoveUp()
        elif act == "Move Down": self.player.playerMoveDown()
        elif act == "Attack": self.player.playerAttackEnemy()
        elif act == "Rob Item": self.player.playerRobItems()
    
    def loadgameData(self) -> None:
        if canSeek:
            self.nolookBtn.config(image=self.nolookImg)
            self.nolookBtn.image = self.nolookImg
            self.showWagon()
        self.changeIconMinus()


class PlanningWindow(Toplevel):
    def __init__(self, master = None) -> None:
        super().__init__(master=master)
        self.title("Planning the Actions")
        self.geometry('1194x400')
        self.resizable(False, False)
        self.wm_attributes("-topmost", 2)
        self['bg'] = 'black'
        self.canvas = tk.Canvas(self, 
            height = 400, width = 1194, 
            bd = 0, bg = "#000000",
            highlightthickness = 0)
        self.canvas.pack(side=TOP,padx=0,pady=0)
        self.canvas.focus_set()
        self.buttonPosX : int = 100
        self.selectedActions = tk.StringVar()
        self.selectedActions.trace("w", self.actionsSelected)
        self.createActionButtons()
        self.confirmBtn = tk.Button(self.canvas, text="Confirm",
            fg = text_color, font=FONT_HELV,
            command = self.confirmActions,
            highlightbackground=bg_color, bg=bg_color, 
            bd = 0, activebackground=TEXT_PURPLE, cursor='target')
        self.confirmBtn.place(x = 1090, y = 350)

        self.cancelBtn = tk.Button(self.canvas, text="Cancel",
            fg = text_color, font=FONT_HELV,
            command = self.cancelActions,
            highlightbackground=bg_color, bg=bg_color, 
            bd = 0, activebackground=TEXT_PURPLE, cursor='target')
        self.cancelBtn.place(x = 1000, y = 350)

        self.actLstLbl = tk.Label(self.canvas, text="List of the Actions:", 
            fg = text_color, font=FONT_HELV,
            highlightbackground=bg_color, bg=bg_color, 
            bd = 0, activebackground=TEXT_PURPLE, cursor='target')
        self.actLstLbl.place(x = 100, y = 50)

        self.showActList = tk.Label(self.canvas, text="", 
            fg = text_color, font=FONT_HELV,
            highlightbackground=bg_color, bg=bg_color, 
            bd = 0, activebackground=TEXT_PURPLE, cursor='target')
        self.showActList.place(x = 300, y = 50)

        self.refreshLstBtn = tk.Button(self.canvas, text="Refresh List",
            fg = text_color, font=FONT_HELV,
            command = self.refreshLstActions,
            highlightbackground=bg_color, bg=bg_color, 
            bd = 0, activebackground=TEXT_PURPLE, cursor='target')
        self.refreshLstBtn.place(x = 1000, y = 50)
    
    def actionsSelected(self, *args) -> None:
        global planningList
        if int(len(planningList)) < nb_actions:
            planningList.append(self.selectedActions.get())
            # print(planningList)
            self.showActList.config(text=f"{planningList}".replace("'", " "))
    
    def refreshLstActions(self) -> None:
        global planningList
        planningList.clear()
        self.showActList.config(text=f"{planningList}".replace("'", " "))

    def createActionButtons(self, index:int = 0) -> None:
        ### action list variables:
        action_lst = ('Move Left', 'Move Right', 
                        'Move Up', 'Move Down', 
                        'Attack', 'Rob Item')

        ### create the menubutton:
        actionBtn : list = []
        actionsMN : list = []
        for _nbActS in range(nb_actions):
            actionBtn.append(Menubutton(self.canvas, text=f"Action {index+1}".upper(), 
                fg = text_color, highlightbackground=bg_color,
                bg=bg_color, bd = 0, font=FONT_HELV, cursor = 'target',
                activebackground=TEXT_PURPLE))
            actionsMN.append(tk.Menu(actionBtn[index], tearoff = 0))
            actionBtn[index]["menu"] = actionsMN[index]
            for action in action_lst:
                actionsMN[index].add_radiobutton(label = action, 
                    font=FONT_HELV, background=TEXT_BLACK, foreground=text_color,
                    activebackground=TEXT_PURPLE, activeforeground='blue',
                    value = action, variable = self.selectedActions)
            actionBtn[index].place(x = self.buttonPosX, y = 100)
            index += 1; self.buttonPosX += 200
    
    def cancelActions(self) -> None:
        global pauseGame
        pauseGame = False
        self.destroy()
    
    def confirmActions(self) -> None:
        global startPlanning, pauseGame
        startPlanning = True
        pauseGame = False
        self.destroy()


class MenuInfo(tk.Frame):
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

    
        #### return to the game button:
        self.returnBtn = tk.Button(self.canvas, text="",
            fg = text_color, font=FONT_HELV,
            command = lambda: master.switch_frame(Game),
            highlightbackground=bg_color, bg=bg_color, 
            bd = 0, activebackground=TEXT_PURPLE, cursor='target')
        self.returnBtn.place(x = 0, y = 0)
    
        self.loadTextLang()
    
    def loadTextLang(self) -> None:
        if setLang == int(langList[0]):
            self.returnBtn.config(text=english_text['return'])

        elif setLang == int(langList[1]):
            self.returnBtn.config(text=francais_texte['return'])
        
        elif setLang == int(langList[2]):
            self.returnBtn.config(text=vietnamese_text['return'])


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

        self.ruleGameTxt = Text(self.canvas, 
            width = 1194, height=576, 
            bg = bg_color, bd = 0, foreground=text_color, 
            insertborderwidth=0, autoseparators=True)
        self.ruleGameTxt.place(x = -1, y = -1)
        self.scroll = Scrollbar(self.canvas, command = self.ruleGameTxt.yview)
        self.ruleGameTxt.configure(yscrollcommand = self.scroll.set)
        self.ruleGameTxt.insert('1.0', game_rule_EN)

        #### return to the start menu button:
        self.returnBtn = tk.Button(self.canvas, text="",
            fg = text_color, font=FONT_HELV,
            command = lambda: master.switch_frame(MenuStartWindow),
            highlightbackground=bg_color, bg=bg_color, 
            bd = 0, activebackground=TEXT_PURPLE, cursor='target')
        self.returnBtn.place(x = 0, y = 0)

        self.loadTextLang()
    
    def loadTextLang(self) -> None:
        if setLang == int(langList[0]):
            self.returnBtn.config(text=english_text['return'])
            self.ruleGameTxt.delete('1.0', END)
            self.ruleGameTxt.insert('1.0', game_rule_EN)

        elif setLang == int(langList[1]):
            self.returnBtn.config(text=francais_texte['return'])
            self.ruleGameTxt.delete('1.0', END)
            self.ruleGameTxt.insert('1.0', game_rule_FR)
        
        elif setLang == int(langList[2]):
            self.returnBtn.config(text=vietnamese_text['return'])
            self.ruleGameTxt.delete('1.0', END)
            self.ruleGameTxt.insert('1.0', game_rule_VN)


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
            fill=text_color, text=credits_text_eng, 
            font=FONT_HELV)


        #### Scroll up button:
        self.arrowUpImg = Image.open(path_arrow_icon_up)
        self.arrowUpImg = ImageTk.PhotoImage(self.arrowUpImg)
        self.arrowUpBtn = Button(self.canvas, image=self.arrowUpImg, 
            command = self.scrollUp, 
            bd = 0, bg = bg_color,
            activebackground=TEXT_PURPLE, cursor='target',
            borderwidth=0, highlightthickness=0)
        self.arrowUpBtn.image = self.arrowUpImg

        #### Scroll down button:
        self.arrowDownImg = rotate_img(path_arrow_icon_up, 180)
        self.arrowDownImg.save("./assets/Images/arrow_down.png")
        self.arrowDownImg = ImageTk.PhotoImage(self.arrowDownImg)
        self.arrowDownBtn = Button(self.canvas, image=self.arrowDownImg, 
            command = self.scrollDown, 
            bd = 0, bg = bg_color,
            activebackground=TEXT_PURPLE, cursor='target',
            borderwidth=0, highlightthickness=0)
        self.arrowDownBtn.image = self.arrowDownImg

        #### GitHub project button:
        self.githubImg = Image.open(path_github_icon)
        self.githubImg = self.githubImg.resize((50, 50))
        self.githubImg = ImageTk.PhotoImage(self.githubImg)
        self.githubBtn = Button(self.canvas, image=self.githubImg, 
            command = self.openGitHub, 
            bd = 0, bg = bg_color,
            activebackground=TEXT_PURPLE, cursor='target',
            borderwidth=0, highlightthickness=0)
        self.githubBtn.image = self.githubImg
        
        ### Return button:
        self.new = 1
        self.returnBtn = tk.Button(self.canvas, text="",
            fg = text_color, font=FONT_HELV,
            command = lambda: master.switch_frame(MenuStartWindow),
            highlightbackground=bg_color, bg=bg_color, 
            bd = 0, activebackground=TEXT_PURPLE, cursor='target')
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
        self.title = tk.Label(self, text="", fg = text_color, 
            font=('Helvetica 59 underline'), width=8,
            bd = 0, bg ='black', relief=None)
        self.title.grid(row = 0, columnspan=2, sticky = EW)

        self.lineLbl_0 = tk.Label(self, width=44, height=3, 
            bd = 0, bg = 'black', relief=None)
        self.lineLbl_0.grid(row=1, columnspan=2, sticky=EW)

        #### Language Setting
        self.langLbl = tk.Label(self, text="", 
            fg = text_color, font=FONT_HELV, width = 20,
            bd = 0, bg ='black', relief=None, 
            anchor=W, justify=LEFT)
        self.langLbl.grid(row = 2, column = 0, sticky = EW)
        
        self.Cbstyle = ttk.Style()
        self.Cbstyle.map('TCombobox', fieldbackground=[('readonly',bg_color)])
        self.Cbstyle.map('TCombobox', selectbackground=[('readonly', bg_color)])
        self.Cbstyle.map('TCombobox', selectforeground=[('readonly', text_color)])
        
        self.langTxt = tk.StringVar()
        self.langBox = ttk.Combobox(self, textvariable=self.langTxt, 
            values=listCBLangEN, width=14,
            font=("Helvetica", 11, "bold"), foreground=text_color)
        self.langBox.grid(row = 2, column = 1, sticky = EW)
        self.langBox['state'] = 'readonly'
        self.setDefaultLanguage()
        self.langBox.bind('<<ComboboxSelected>>', self.updateLang)

        ### Sound Setting
        self.soundLbl = tk.Label(self, text = "Sound \nMusic : ", 
            fg = text_color, font=FONT_HELV, width = 20,
            bd = 0, bg ='black', relief=None, 
            anchor=W, justify=LEFT)
        self.soundLbl.grid(row = 3, column = 0, sticky = EW)
        
        ### Sound Scale
        self.scaleVar = tk.StringVar()
        self.scaleSound = tk.Scale(self, from_=0, to=100, orient=HORIZONTAL, 
            troughcolor = text_color, bg = 'black', bd = 0, 
            fg = text_color, font=FONT_HELV, width=15, length = 126,
            highlightbackground = bg_color, 
            resolution=0.1, variable= self.scaleVar)
        self.scaleSound.grid(row = 3, column = 1, sticky = EW)

        ### Mute and Unmute setting
        self.muteLbl = tk.Label(self, text = " - Sound : ", 
            fg = text_color, font=FONT_HELV, width = 20,
            bd = 0, bg ='black', relief=None, 
            anchor=W, justify=LEFT)
        self.muteLbl.grid(row=4, column=0, sticky=EW)

        self.musicBtnZone = tk.Frame(self, bg = '#000000', width=128, height=23)
        self.musicBtnZone.grid(row=4, column=1, sticky=EW)

        self.unmuteImg = ImageTk.PhotoImage(Image.open(path_vol_icon_play).resize((23, 23)))
        self.muteImg = ImageTk.PhotoImage(Image.open(path_vol_icon_pause).resize((23, 23)))

        self.muteBtn = tk.Button(self.musicBtnZone, image = self.unmuteImg, 
            relief = FLAT, command = self.changeIcon, width=30,
            highlightbackground=bg_color, bg=bg_color, bd = 0, 
            activebackground=TEXT_PURPLE)
        self.muteBtn.image = self.unmuteImg
        self.muteBtn.place(x = 47, y = 0)

        ### Buttons to change the value of scale sound
        self.minusImg = ImageTk.PhotoImage(Image.open(path_minus_icon).resize((23, 23)))
        self.decreaseScaleVar = tk.Button(self.musicBtnZone, image = self.minusImg, 
            width=30, relief = FLAT, command = self.decreaseSoundScale,
            highlightbackground=bg_color, bg=bg_color, bd = 0, 
            activebackground=TEXT_PURPLE)
        self.decreaseScaleVar.image = self.minusImg
        self.decreaseScaleVar.place(x = 0, y = 0)
        
        self.plusImg = ImageTk.PhotoImage(Image.open(path_plus_icon).resize((23, 23)))
        self.increaseScaleVar = tk.Button(self.musicBtnZone, image=self.plusImg, 
            width=30, relief = FLAT, command = self.increaseSoundScale,
            highlightbackground=bg_color, bg=bg_color, bd = 0, 
            activebackground=TEXT_PURPLE)
        self.increaseScaleVar.image = self.minusImg
        self.increaseScaleVar.place(x = 93, y = 0)
        
        self.setDefaultVolumeScale()

        ### Color text Setting
        self.colorLbl = tk.Label(self, text= "", 
            fg = text_color, font=FONT_HELV, width = 20,
            bd = 0, bg ='black', relief=None, 
            anchor=W, justify=LEFT)
        self.colorLbl.grid(row = 5, column = 0, sticky = EW)

        self.colorBtn = tk.Button(self, text= "", width = 14,
            fg = text_color, font=("Helvetica", 10, "bold"), command=self.colorSetting,
            highlightbackground=bg_color, bg=bg_color, bd = 0, 
            activebackground=TEXT_PURPLE, height = 2,
            borderwidth = 0)
        self.colorBtn.grid(row = 5, column=1, sticky = EW, padx=2)

        ### Space vertical
        self.lineLbl = tk.Label(self, width=44, height=5, 
            bd = 0, bg = 'black', relief=None)
        self.lineLbl.grid(row=6, columnspan=2, sticky=EW)

        ### Buttons
        self.applyBtn = tk.Button(self, text=english_text['apply'], width = 18,
            fg = text_color, font=FONT_HELV,
            command = self.applyChange,
            highlightbackground='#76428A', bg=bg_color, bd = 0, 
            activebackground=TEXT_PURPLE)
        self.applyBtn.grid(row = 7, column = 0, sticky=EW)

        self.returnBtn = tk.Button(self, text=english_text['return'], width = 9,
            fg = text_color, font=FONT_HELV,
            command = lambda: master.switch_frame(MenuStartWindow),
            highlightbackground=bg_color, bg=bg_color, bd = 0, 
            activebackground=TEXT_PURPLE, 
            borderwidth = 0)
        self.returnBtn.grid(row = 7, column=1, sticky = EW)

        self.loadTextLang()
        self.loadColorText()
    
    def loadTextLang(self) -> None:
        if setLang == int(langList[0]):
            self.title.config(text=english_text['setting'].upper() + ':')
            self.langLbl.config(text= " - " + english_text['language'] + ' : ')
            self.muteLbl.config(text= " - " + english_text['sound'] + ' : ')
            self.soundLbl.config(
                text=f" - {english_text['setting']} \n\t{english_text['volume']} : "
            )
            self.colorLbl.config(text = "\n - " + english_text['color'] + " " + english_text['text'].lower() + " : ")
            self.colorBtn.config(text = english_text['change'] + " " + english_text['color'])
            self.applyBtn.config(text=english_text['apply'])
            self.returnBtn.config(text=english_text['return'])
            self.langBox.delete(0,'end')
            self.langBox['values'] = listCBLangEN
            self.langBox.current(setLang)
        
        elif setLang == int(langList[1]):
            self.title.config(text = francais_texte['setting'])
            self.langLbl.config(text= " - " + francais_texte['language'] + ' : ')
            self.muteLbl.config(text= " - " + francais_texte['sound'] + ' : ')
            self.soundLbl.config(
                text=f" - {francais_texte['setting']} \n\t{francais_texte['volume']} : "
            )
            self.colorLbl.config(text = "\n - " + francais_texte['color'] + " " + francais_texte['text'].lower() + " : ")
            self.colorBtn.config(text = francais_texte['change'] + " " + francais_texte['color'])
            self.applyBtn.config(text=francais_texte['apply'])
            self.returnBtn.config(text=francais_texte['return'])
            self.langBox.delete(0,'end')
            self.langBox['values'] = listCBLangFR
            self.langBox.current(setLang)
        
        elif setLang == int(langList[2]):
            self.title.config(text = vietnamese_text['setting'] + ':')
            self.langLbl.config(text= " - " + vietnamese_text['language'] + ' : ')
            self.muteLbl.config(text= " - " + vietnamese_text['sound'] + ' : ')
            self.soundLbl.config(
                text=f" - {vietnamese_text['setting']} \n\t{vietnamese_text['volume']} : "
            )
            self.colorLbl.config(text = "\n - " + vietnamese_text['color'] + " " + vietnamese_text['text'].lower() + " : ")
            self.colorBtn.config(text = vietnamese_text['change'] + " " + vietnamese_text['color'])
            self.applyBtn.config(text=vietnamese_text['apply'])
            self.returnBtn.config(text=vietnamese_text['return'])
            self.langBox.delete(0,'end')
            self.langBox['values'] = listCBLangVN
            self.langBox.current(setLang)
    
    def loadColorText(self) -> None:
        self.title.config(fg = text_color)
        self.langLbl.config(fg = text_color)
        self.muteLbl.config(fg = text_color)
        self.soundLbl.config(fg = text_color)
        self.colorLbl.config(fg = text_color)
        self.colorBtn.config(fg = text_color)
        self.applyBtn.config(fg = text_color)
        self.returnBtn.config(fg = text_color)
        self.langBox.config(foreground=text_color)
        self.scaleSound.config(fg=text_color, troughcolor = text_color)
    
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
    
    def colorSetting(self) -> None:
        global text_color
        self.color = askcolor(color=text_color, title = "Text Game Color Choose")
        text_color = str(self.color[1])
        print(text_color)

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

        self.loadColorText()
        print("Text color: ",text_color)


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
    def __init__(self, canvas:Canvas, player, x:int, y:int, size_x:int, size_y:int, price:int, photo) -> None:
        self.canvas = canvas
        self.player = player
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



class Bandits():
    def __init__(self, parent, can:Canvas, bd_x:int, bd_y:int, position:int):
        self.parent = parent
        self.can = can
        self.bd_x = bd_x
        self.bd_y = bd_y
        self.position = position
        self.position_y = 1
        self.dirct = 1
    
    def movement(self, x:int, y:int) -> None:
        self.can.move(self.img_j, x, y)
        self.bd_x = x
        self.bd_y = y


class Player(): 
    def __init__(self, parent, can:Canvas, pl_x:int, pl_y:int, position:int):
        self.parent = parent
        self.can = can
        self.pl_x = pl_x
        self.pl_y = pl_y

        self.position_wagon = position
        self.position_y = 1
        self.dirct = 1
        self.playerIdle()
        print(self.can.coords(self.img_j))

    def movement(self, x:int, y:int) -> None:
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

        if not pauseGame:
            if self.dirct == 1:
                playerImgIdle = self.can.playerImgIdle = ImageTk.PhotoImage(Image.open( path_thief_IdleRight + str(index) + '.png').resize((playerSizeX, playerSizeY)))
            else:
                playerImgIdle = self.can.playerImgIdle = ImageTk.PhotoImage(Image.open( path_thief_IdleLeft + str(index) + '.png').resize((playerSizeX, playerSizeY)))
            item = self.can.create_image(self.pl_x, self.pl_y, image = playerImgIdle)
            self.img_j =  item
            index += 1
            if index == 11: index = 1

        if state == str(playerState[0]):
            self.can.after(100, self.playerIdle, item, index)
        elif state == str(playerState[1]):
            self.can.delete(item)
            self.playerWalk()
        elif state == str(playerState[2]):
            self.can.delete(item)
            self.playerAttack()
        elif state == str(playerState[3]):
            self.can.delete(item)
            self.playerDie()
    
    def playerWalk(self, item = None, index:int = 1) -> None:
        global playerPosX
        self.can.delete(item)

        if not pauseGame:
            if self.dirct == 1:
                playerImgWalk = self.can.playerImgWalk = ImageTk.PhotoImage(Image.open( path_thief_WalkRight + str(index) + '.png').resize((playerSizeX, playerSizeY)))
                if playerMove:
                    playerPosX += 2
                    self.movement(playerPosX, playerPosY)
            else:
                playerImgWalk = self.can.playerImgWalk = ImageTk.PhotoImage(Image.open( path_thief_WalkLeft + str(index) + '.png').resize((playerSizeX, playerSizeY)))
                if playerMove:
                    playerPosX -= 2
                    self.movement(playerPosX, playerPosY)
            item = self.can.create_image(self.pl_x, self.pl_y, image = playerImgWalk)
            self.img_j = item
            index += 1
            if index == 11: index = 1
            self.touchDoors()
            self.stopAtPointsAfterMove()
        
        if state == str(playerState[1]):
            self.can.after(100, self.playerWalk, item, index)
        elif state == str(playerState[0]):
            self.can.delete(item)
            self.playerIdle()
        elif state == str(playerState[2]):
            self.can.delete(item)
            self.playerAttack()
        elif state == str(playerState[3]):
            self.can.delete(item)
            self.playerDie()
    
    def playerAttack(self, item = None, index:int = 1) -> None:
        self.can.delete(item)

        if not pauseGame:
            if self.dirct == 1:
                playerImgAttack = self.can.playerImgAttack = ImageTk.PhotoImage(Image.open( path_thief_AttackRight + str(index) + '.png').resize((playerSizeX, playerSizeY)))
            else:
                playerImgAttack = self.can.playerImgAttack = ImageTk.PhotoImage(Image.open( path_thief_AttackLeft + str(index) + '.png').resize((playerSizeX, playerSizeY)))
            item = self.can.create_image(self.pl_x, self.pl_y, image = playerImgAttack)
            self.img_j =  item
            index += 1
            if index == 11: self.playerStop()

        if state == str(playerState[2]):
            self.can.after(100, self.playerAttack, item, index)
        elif state == str(playerState[0]):
            self.can.delete(item)
            self.playerIdle()
        elif state == str(playerState[1]):
            self.can.delete(item)
            self.playerWalk()
        elif state == str(playerState[3]):
            self.can.delete(item)
            self.playerDie()
    
    def playerDie(self, item = None, index:int = 1) -> None:
        global gameOver
        self.can.delete(item)

        if not pauseGame:
            if self.dirct == 1:
                playerImgDie = self.can.playerImgDie = ImageTk.PhotoImage(Image.open( path_thief_DieRight + str(index) + '.png').resize((playerSizeX, playerSizeY)))
            else:
                playerImgDie = self.can.playerImgDie = ImageTk.PhotoImage(Image.open( path_thief_DieLeft + str(index) + '.png').resize((playerSizeX, playerSizeY)))
            item = self.can.create_image(self.pl_x, self.pl_y, image = playerImgDie)
        self.img_j =  item
        index += 1
        if state == str(playerState[3]) and index <= 11:
            self.can.after(100, self.playerDie, item, index)
        if index == 11: gameOver = True

    def playerMoveRight(self) -> None:
        global state, playerMove
        self.dirct = 1
        state = str(playerState[1])
        playerMove = True

    def playerMoveLeft(self) -> None:
        global state, playerMove
        self.dirct = 0
        state = str(playerState[1])
        playerMove = True

    def playerMoveUp(self) -> None:
        global goUp, goDown, playerPosY
        self.playerMoveLeft()
        goUp = True; goDown = False

    def playerMoveDown(self) -> None:
        global goUp, goDown, playerPosY
        self.playerMoveLeft()
        goDown = True; goUp = False
    
    def playerStop(self) -> None:
        global playerMove, state, canClicAct
        state = str(playerState[0])
        print(self.can.coords(self.img_j))
        playerMove = False
        canClicAct = True
    
    def playerRobItems(self) -> None:
        global canRobItem
        canRobItem = True
        if self.dirct == 1: self.playerMoveRight()
        elif self.dirct == 0: self.playerMoveLeft()

    def playerAttackEnemy(self) -> None:
        global playerState, state
        state = str(playerState[2])

    def touchDoors(self) -> None:
        global playerPosX, playerPosY, goDown, goUp, outsideTrain, stopAfterMove
        self.doors : list = []
        if nb_wagons == 3: self.doors.clear(); self.doors += door_pos_3_wagon
        elif nb_wagons == 4: self.doors.clear(); self.doors += door_pos_4_wagon
        if playerPosX in self.doors:
            if not goUp and not goDown:
                if playerPosX == int(self.doors[0]) or playerPosX == int(self.doors[-1]): self.playerStop()
                else:
                    if nb_wagons == 3:
                        if self.dirct == 1: playerPosX += 70; self.position_wagon += 1
                        else: playerPosX -= 70; self.position_wagon -= 1
                        self.movement(playerPosX, playerPosY)
                        stopAfterMove = True
                    elif nb_wagons == 4:
                        if self.dirct == 1: playerPosX += 52; self.position_wagon += 1
                        else: playerPosX -= 52; self.position_wagon -= 1
                        self.movement(playerPosX, playerPosY)
                        stopAfterMove = True
            elif goUp and not goDown and self.position_y == 1: 
                if nb_wagons == 3: playerPosY -= 80
                elif nb_wagons == 4: playerPosY -= 54
                self.movement(playerPosX, playerPosY)
                self.playerMoveRight()
                self.position_y += 1
                stopAfterMove = True
                goDown = True; goUp = False; outsideTrain = True
            elif not goUp and goDown and self.position_y > 1:
                if nb_wagons == 3: playerPosY += 80
                elif nb_wagons == 4: playerPosY += 54
                self.movement(playerPosX, playerPosY)
                self.playerMoveRight()
                self.position_y -=1
                stopAfterMove = True
                goDown = False; goUp = False; outsideTrain = False
            else: self.playerStop()
    
    def stopAtPointsAfterMove(self) -> None:
        global stopAfterMove
        self.stopPonits : list = []
        if nb_wagons == 3: self.stopPonits.clear(); self.stopPonits += stopPointActions_wg3
        elif nb_wagons == 4: self.stopPonits.clear(); self.stopPonits += stopPointActions_wg4
        if stopAfterMove:
            if playerPosX in self.stopPonits:
                self.playerStop()
                stopAfterMove = False

    def testMoveRightKey(self, event) -> None:
        print(event.keysym)
        self.playerMoveRight()
    
    def testMoveLeftKey(self, event) -> None:
        print(event.keysym)
        self.playerMoveLeft()
    
    def testMoveUpKey(self, event) -> None:
        print(event.keysym)
        self.playerMoveUp()
    
    def testMoveDownKey(self, event) -> None:
        print(event.keysym)
        self.playerMoveDown()
    
    def testStopKey(self, event) -> None:
        print(event.keysym)
        self.playerStop()



class Clouds():
    def __init__(self,parent,canvas):
        self.parent = parent
        self.canvas = canvas
        self.fallSpeed = randint(35, 55)
        self.yPosition = randint(140, 260)        
        self.xPosition = randint(1200, 1300)
        self.isgood = randint(0, 1)
        self.vitesse = randint(-25,-10)
        self.goodItems = [path_cloud_bg, path_cloud_2_bg, path_cloud_3_bg]
        # create falling items
        self.itemPhoto = ImageTk.PhotoImage(Image.open(f"{choice(self.goodItems)}").resize((randint(130, 150), randint(84, 92))))
        self.fallItem = self.canvas.create_image( (self.xPosition ,self.yPosition),
            image=self.itemPhoto , tag="good")
        # trigger falling item movement
        self.movingClouds()
        
    def movingClouds(self):
        if not pauseGame: self.canvas.move(self.fallItem, self.vitesse, 0)
        if (self.canvas.coords(self.fallItem)[0] < randint(-100, 200)):
            self.canvas.delete(self.fallItem)
        else:
            self.parent.after(self.fallSpeed, self.movingClouds)


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


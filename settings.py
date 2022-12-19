

####### DATA VALUE (constant): ###########
NB_WAGONS : int = 3
NOM_BANDIT_1 : str = 'Shadow'
NOM_BANDIT_2 : str = 'Killer'
NB_ACTIONS : int = 4
NB_JOUEURS : int = 1
NB_TOURS : int = 1
NB_BALLES : int = 6



############ GAME DATA (for save and load): ############
saveGame : bool = False
gameOver : bool = False
startTheGame : bool = False
startPlanning : bool = False
pauseGame : bool = False

### for fixing value:
nb_wagons : int = NB_WAGONS
nb_actions : int = NB_ACTIONS
canPlusWG : bool = True
canClicAct : bool = True

#### set train carriages image size:
carSizeX : int = 298
carSizeY : int = 85
fullSizeX : int = 148
showFull : bool = False
canSeek : bool = False
pos_4_wagon_1_door_1 : int = 24
pos_4_wagon_1_door_2 : int = 272
pos_4_wagon_2_door_1 : int = 324
pos_4_wagon_2_door_2 : int = 572
pos_4_wagon_3_door_1 : int = 624
pos_4_wagon_3_door_2 : int = 872
pos_4_wagon_4_door_1 : int = 924
pos_4_wagon_4_door_2 : int = 1166

door_pos_4_wagon :list = [
        pos_4_wagon_1_door_1,
        pos_4_wagon_1_door_2,
        pos_4_wagon_2_door_1,
        pos_4_wagon_2_door_2,
        pos_4_wagon_3_door_1,
        pos_4_wagon_3_door_2,
        pos_4_wagon_4_door_1,
        pos_4_wagon_4_door_2,
]

pos_3_wagon_1_door_1 : int = 30
pos_3_wagon_1_door_2 : int = 360
pos_3_wagon_2_door_1 : int = 430
pos_3_wagon_2_door_2 : int = 760
pos_3_wagon_3_door_1 : int = 830
pos_3_wagon_3_door_2 : int = 1164

door_pos_3_wagon :list = [
        pos_3_wagon_1_door_1,
        pos_3_wagon_1_door_2,
        pos_3_wagon_2_door_1,
        pos_3_wagon_2_door_2,
        pos_3_wagon_3_door_1,
        pos_3_wagon_3_door_2,
]

#### set volume
volume : float = 0.0
volume_sound : float = 0.5
unmute : bool = True

#### player states:
playerState : list = ['idle', 'walk', 'attack', 'die']
state : str = str(playerState[0])
playerMove : bool = False
outsideTrain : bool = False
goUp : bool = False
goDown : bool = False
atWagon : int = 1
playerPosX : int = 80
playerPosY : int = 533
playerSizeX : int = 32
playerSizeY : int = 32

canRobItem : bool = False
stopAfterMove : bool = False
stopPointActions_wg3 : list = [110, 310, 510, 710, 910, 1100]
stopPointActions_wg4 : list = [80, 230, 380, 530, 680, 830, 980, 1130]
planningList : list = []

#### Gems:
gemsPosX : int = 533
gemsPosY : int = 300

#### set language:
listCBLangEN : tuple = ('English', 'French', 'Vietnamese')
listCBLangFR : tuple = ('Anglais', 'Français', 'Vietnamien')
listCBLangVN : tuple = ('Tiếng Anh', 'Tiếng Pháp', 'Tiếng Việt')
langList : list = [0, 1, 2] ### 0:EN / 1:FR / 2:VN
setLang : int = 0 ### set english as language default 


######## DATA COLOR #############
TEXT_BLACK : str = '#0a0403'
TEXT_PURPLE : str = '#603c60'

bg_color : str = TEXT_BLACK
text_color : str = 'purple'

######## FONT TYPE ##############
FONT_HELV : list = ("Helvetica", 15, "bold")


######## SOURCES PATH ##################
### sounds:
path_train_sound : str = "./assets/Sound/start_train_sound.wav"
path_credit_menu_music : str = "./assets/Sound/credit_music.wav"
path_click_sound : str = "./assets/Sound/click_01.wav"
### images:
path_vol_icon_play : str = "./assets/Images/volume-icon-play.png"
path_vol_icon_pause : str = "./assets/Images/volume-icon-pause.png"
path_plus_icon : str = "./assets/Images/plus-icon.png"
path_minus_icon : str = "./assets/Images/minus-icon.png"
path_pause_icon : str = "./assets/Images/pause-icon.png"
path_unpause_icon : str = "./assets/Images/unpause-icon.png"
path_eye_can_look : str = "./assets/Images/eye_can_look.png"
path_eye_can_not_look : str = "./assets/Images/eye_can_not_look.png"
path_arrow_icon_up : str = "./assets/Images/arrow_up.png"
path_github_icon : str = "./assets/Images/github_icon.png"
path_info_icon : str = "./assets/Images/information-icon.png"
path_blue_gem : str = "./assets/Images/Items/blue_diamond.png"
path_green_gem : str = "./assets/Images/Items/green_diamond.png"
path_red_gem : str = "./assets/Images/Items/red_diamond.png"
path_sack_icon : str = "./assets/Images/Items/sack.png"
path_arrow_bullet : str = "./assets/Images/Items/arrow.png"
path_train_car : str = './assets/Images/Train/TrainBack.png'
path_start_menu_bg : str = './assets/Images/Background/pixel_train_city.gif'
path_background_city : str = "./assets/Images/Background/BackgroundCity.png"
path_cloud_bg : str = './assets/Images/Background/clouds1.png'
path_cloud_2_bg : str = './assets/Images/Background/clouds2.png'
path_cloud_3_bg : str = './assets/Images/Background/clouds3.png'
path_train_full_green : str = "./assets/Images/Train/TrainFullGreen.png"
path_train_full_gray : str = "./assets/Images/Train/TrainFullGray.png"
path_train_test_1 : str = "./assets/Images/Train/Train_Test1.png"
path_train_test_2 : str = "./assets/Images/Train/Train_Test2.png"
path_thief_IdleRight : str = "./assets/Images/Caracters/Thief/IdleRight/Idle_"
path_thief_IdleLeft : str = "./assets/Images/Caracters/Thief/IdleLeft/Idle_"
path_thief_WalkRight : str = "./assets/Images/Caracters/Thief/WalkRight/Walk_"
path_thief_WalkLeft : str = "./assets/Images/Caracters/Thief/WalkLeft/Walk_"
path_thief_AttackRight : str = "./assets/Images/Caracters/Thief/AttackRight/Attack_"
path_thief_AttackLeft : str = "./assets/Images/Caracters/Thief/AttackLeft/Attack_"
path_thief_DieRight : str = "./assets/Images/Caracters/Thief/DieRight/Die_"
path_thief_DieLeft : str = "./assets/Images/Caracters/Thief/DieLeft/Die_"
path_night_thief_IdleRight : str = './assets/Images/Caracters/NightThief/IdleRight/Idle_'
path_night_thief_IdleLeft : str = './assets/Images/Caracters/NightThief/IdleLeft/Idle_'
### link url website:
url_github_project : str = "https://github.com/Viet281101/Colt_Express_Tkinter"

gems : list = [path_red_gem, path_blue_gem, path_green_gem]

#################################### LANGUE TEXT SETTING ###########################################
english_text : dict = {
    'play' : "Play",
    'start' : "Start",
    'rule' : "Rules",
    'setting' : "Setting",
    'language' : "Language",
    'music' : "Music",
    'sound' : "Sound",
    'volume' : "the volume",
    'color' : "Color",
    'text' : "Text",
    'change' : "Change",
    'planning' : "Planning",
    'action' : "Action",
    'apply' : "Apply",
    'credit' : "Credit",
    'exit' : "Exit",
    'quit' : "Quit",
    'return' : "Return",
    'lang_not_title': "Language Notification",
    'lang_not' : "Press 'Apply' to load the language !",
    'confirm_quit' : "Are you sure to quit the game ? \nYour data will not be saved !",
    'caracter_move_lr' : "Move one car forward or backward, staying on the same floor.",
    'caracter_move_ud' : "Go inside or climb onto the roof of their current wagon.",
    'caracter_rob' : "Rob a traveler to retrieve loot (or simply loot loot that has been left there).",
    'caracter_shoot' : "Shoot another nearby bandit to make him drop his loot.",
}

francais_texte : dict = {
    'play' : "Jouer",
    'start' : "Partir",
    'rule' : "Règle",
    'setting' : "Paramètre",
    'language' : "Langue",
    'music' : "Musique",
    'sound' : "Son",
    'volume' : "le volume",
    'color' : "Couleur",
    'text' : "Texte",
    'change' : "Changer",
    'planning' : "Planification",
    'action' : "Action",
    'apply' : "Applique",
    'credit' : "Crédit",
    'exit' : "Sortir",
    'quit' : "Quitté",
    'return' : "Retourne",
    'lang_not_title': "Langue Notification",
    'lang_not' : "Appuyez sur 'Appliquer' pour charger la langue !",
    'confirm_quit' : "Etes-vous sûr de quitter le jeu ? \nVos données ne seront pas enregistrées !",
    'caracter_move_lr' : "Se déplacer d'un wagon en avant ou en arrière, en restant au même étage.",
    'caracter_move_ud' : "Aller à l'intérieur ou grimper sur le toit de leur wagon actuel.",
    'caracter_rob' : "Braquer un voyageur pour récupérer du butin (ou simplement récupérer un butin qui a été abandonné là).",
    'caracter_shoot' : "Tirer sur un autre bandit proche pour lui faire lâcher son butin.",
}

vietnamese_text : dict = {
    'play' : "Chơi",
    'start' : "Bắt đầu",
    'rule' : "Quy tắc",
    'setting' : "Cài đặt",
    'language' : "Ngôn ngữ",
    'music' : "Âm nhạc",
    'sound' : "Âm thanh",
    'volume' : "âm lượng",
    'apply' : "Áp dụng",
    'color' : "Màu Sắc",
    'text' : "Chữ",
    'change' : "Thay đổi",
    'planning' : "Lập kế hoạch",
    'action' : "Hành động",
    'credit' : "Dự án",
    'exit' : "Thoát",
    'quit' : "Thoát",
    'return' : "Trở về",
    'lang_not_title': "Thông báo ngôn ngữ",
    'lang_not' : "Nhấn 'Áp dụng' để tải ngôn ngữ !",
    'confirm_quit' : "Bạn có chắc chắn thoát khỏi trò chơi? \nDữ liệu của bạn sẽ không được lưu !",
    'caracter_move_lr' : "Di chuyển một toa tàu về phía trước hoặc phía sau, hoặc ở trên cùng một tầng.",
    'caracter_move_ud' : "Đi vào bên trong hoặc trèo lên nóc toa xe hiện tại của họ.",
    'caracter_rob' : "Cướp khách du lịch để lấy chiến lợi phẩm (hoặc đơn giản là cướp chiến lợi phẩm đã bị bỏ lại ở đó).",
    'caracter_shoot' : "Bắn một tên cướp khác gần đó để khiến hắn đánh rơi chiến lợi phẩm của mình.",
}




############################################ GAME RULE: ###################################################
game_rule_EN : str = '''


        Overview of game rules:

        The game takes place on board a train, consisting of a locomotive and a number of equal carriages to the number of players. 
        Players embody bandits who have jumped on board to rob the passengers. 
        Objective: collect as much loot as possible, each for himself. 
        This is a game of programming, in which one alternates between two phases:

        - Planning: each player secretly decides on a certain number of actions, which his character will perform in order.

        - Action: perform all the actions number 1, then all the number 2, and this until the end.

        The bandits can be in the wagons or the locomotive, and for each of these elements either indoors or on the roof. 
        In this statement, by abuse of language, we will designate by car a any element of the train, which may be the locomotive. 
        The possible actions for bandits are:

        - Move one car forwards or backwards, staying on the same floor.

        - Go inside or climb onto the roof of their current wagon.

        - Rob a traveler to collect loot (or simply loot loot that has been left there).

        - Shoot another nearby bandit to make him drop his loot. The loot recoverable on board the train are:

        - Purses worth €100 or €200, from passengers, inside the wagons.

        - Jewelry worth €500, from passengers, inside the wagons.

        - A hoard worth €1000, inside the locomotive, in the custody of the Marshall. 
        A Marshall is present on board the train and can move between the locomotive and the wagons, always staying inside. 
        He shoots at all the bandits who are in the same position as him and forced to take refuge on the roof.

'''

game_rule_FR : str = '''


        Aperçu des règles du jeu :

        Le jeu se déroule à bord d'un train, composé d'une locomotive et d'un nombre de wagons égal au nombre de joueurs.
        Les joueurs incarnent des bandits qui ont sauté à bord pour voler les passagers. 
        Objectif : récolter le plus de butin possible, chacun pour soi.
        Il s'agit d'un jeu de programmation, dans lequel on alterne entre deux phases :

        - Planification : chaque joueur décide secrètement d'un certain nombre d'actions, que son personnage effectuera dans l'ordre.

        - Action : effectuez toutes les actions numéro 1, puis toutes les actions numéro 2, et ce jusqu'à la fin.

        Les bandits peuvent être dans les wagons ou la locomotive, et pour chacun de ces éléments soit à l'intérieur soit sur le toit.
        Dans cet énoncé, par abus de langage, on désignera par voiture un élément quelconque du train, qui peut être la locomotive.
        Les actions possibles pour les bandits sont :

        - Avancer ou reculer une voiture en restant au même étage.

        - Entrez ou montez sur le toit de leur wagon actuel.

        - Voler un voyageur pour récupérer du butin (ou simplement piller le butin qui y a été laissé).

        - Tirez sur un autre bandit à proximité pour lui faire lâcher son butin. Les butins récupérables à bord du train sont :

        - Les bourses d'une valeur de 100 € ou 200 €, des passagers, à l'intérieur des wagons.

        - Bijoux d'une valeur de 500 €, provenant des passagers, à l'intérieur des wagons.

        - Un trésor d'une valeur de 1000 €, à l'intérieur de la locomotive, sous la garde du Maréchal.
        Un maréchal est présent à bord du train et peut se déplacer entre la locomotive et les wagons, en restant toujours à l'intérieur.
        Il tire sur tous les bandits qui se trouvent dans la même position que lui et contraints de se réfugier sur le toit.

'''


game_rule_VN : str = '''


        Tổng quan luật chơi:

        Trò chơi diễn ra trên một đoàn tàu bao gồm một đầu máy và một số toa xe bằng với số lượng người chơi.
        Người chơi hóa thân thành những tên cướp đã nhảy lên tàu để cướp hành khách. 
        Mục tiêu: thu thập càng nhiều chiến lợi phẩm càng tốt, mỗi người cho mình.
        Đây là một trò chơi lập trình, trong đó chúng tôi xen kẽ giữa hai giai đoạn:

        - Lập kế hoạch: mỗi người chơi bí mật quyết định một số hành động mà nhân vật của mình sẽ thực hiện theo thứ tự.

        - Động tác: thực hiện hết động tác số 1, rồi đến động tác số 2, cho đến hết.

        Kẻ cướp có thể ở trong toa xe hoặc đầu máy xe lửa, và đối với từng bộ phận này ở bên trong hoặc trên mái nhà.
        Trong tuyên bố này, bằng cách lạm dụng ngôn ngữ, chúng tôi sẽ chỉ định bằng ô tô bất kỳ phần tử nào của đoàn tàu, có thể là đầu máy.
        Các hành động có thể cho kẻ cướp là:

        - Tiến hoặc lùi xe khi vẫn ở trên cùng một mặt sàn.

        - Đi vào hoặc trèo lên nóc toa xe hiện tại của họ.

        - Cướp khách du lịch để lấy chiến lợi phẩm (hoặc chỉ cướp chiến lợi phẩm còn lại ở đó).

        - Bắn một tên cướp khác gần đó để khiến hắn đánh rơi chiến lợi phẩm của mình. Chiến lợi phẩm có thể lấy được trên tàu là:

        - Ví trị giá €100 hoặc €200 đối với hành khách để trong toa xe.

        - Đồ trang sức trị giá €500, của hành khách, bên trong toa tàu.

        - Một kho báu trị giá €1000, bên trong đầu máy, do Nguyên soái quản thúc.
        Một cảnh sát trưởng có mặt trên tàu và có thể di chuyển giữa đầu máy và các toa xe, luôn ở bên trong.
        Anh ta bắn vào tất cả những tên cướp ở cùng vị trí với anh ta và buộc phải trú ẩn trên mái nhà.

'''



####################################### CREDIT TEXT ############################################################
credits_text_eng : str = '''
---------------------- CREDIT ----------------------

            
            
            
            PROJECT SUPERVISOR:
                    Viet Nguyen
            

            
            
            
            
            GAME PROJECT TESTER:
                    Viet Nguyen
            

            
            
            
            
            SCRIPT PROGRAMMER:
                    Viet Nguyen


            


            ANIMATION/GRAPHIC:
                    by Viet Nguyen

            with the sources from:
                OpenGameArt.com
                Pixelartmaker.com
                LibreSprite
                itch.io

            


            
            MUSIC/SFX:
                    by Viet Nguyen
            
            with the sources from:
                Dictaphone
                rfxgen



            


            PROJECT IDEA:
                    by Oumaima El Joubari
                    (professor)



            

            PRODUCER INFO:
                    Name: Viet Nguyen
                    Student number: 20006303
                    Group/class : L2_A 




---------------------- THANK YOU ----------------------
'''


credits_text_fr : str = '''
---------------------- LE CRÉDIT ----------------------

            
            
            
            CHEF DE PROJET:
                    Viet Nguyen
            

            
            
            
            
            TESTEUR DE PROJET DE JEU:
                    Viet Nguyen
            

            
            
            
            
            PROGRAMMATEUR DE SCRIPTS:
                    Viet Nguyen


            


            ANIMATIONS/GRAPHIQUES:
                    par Viêt Nguyen

            avec les sources de :
                OpenGameArt.com
                Pixelartmaker.com
                LibreSprite
                démangeaison.io

            


            
            MUSIQUE/SFX:
                    par Viêt Nguyen
            
            avec les sources de :
                Dictaphone
                rfxgen



            


            IDÉE DE PROJET:
                    par Oumaima El Joubari
                    (professeure)



            

            INFORMATIONS SUR LE PRODUCTEUR:
                    Nom : Viet Nguyen
                    Numéro d'étudiant : 20006303
                    Groupe/classe : L2_A




---------------------- MERCI ----------------------

'''


credits_text_vn : str = '''
---------------------- CREDIT ----------------------

            
            
            
            GIÁM SÁT DỰ ÁN:
                    Việt Nguyễn
            

            
            
            
            
            NGƯỜI THỬ NGHIỆM DỰ ÁN TRÒ CHƠI:
                    Việt Nguyễn
            

            
            
            
            
            LẬP TRÌNH KẾ HOẠCH:
                    Việt Nguyễn


            


            HOẠT HÌNH/HÌNH ẢNH:
                    Việt Nguyễn

            với các nguồn từ:
                OpenGameArt.com
                Pixelartmaker.com
                LibreSprite
                itch.io

            


            
            ÂM NHẠC/SFX:
                    Việt Nguyễn
            
            với các nguồn từ:
                Máy đọc chính tả
                rfxgen



            


            Ý TƯỞNG DỰ ÁN:
                    của Oumaima El Joubari
                    (giáo sư)



            

            THÔNG TIN NHÀ SẢN XUẤT:
                    Tên: Việt Nguyễn
                    Mã số sinh viên: 20006303
                    Nhóm/lớp : L2_A




---------------------- THANK YOU ----------------------
'''


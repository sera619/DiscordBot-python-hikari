import os
from dotenv import load_dotenv
import lightbulb

load_dotenv()

SERA_ID = os.environ['SERA_ID']
SERA_DISCORD_ID = os.environ['SERA_DISCORD_ID']
TOKEN = os.environ['TOKEN']
COMMON_CHANNEL_ID = os.environ['COMMON_CHANNEL_ID']

SHOW_START_EMBED = False

def load_bot_setting():
    global SHOW_START_EMBED
    with open('./data/bot-set.txt', 'r') as f:
        dat = f.read()
    if int(dat) == 1:
        SHOW_START_EMBED = True
        return SHOW_START_EMBED

    else:
        SHOW_START_EMBED = False
        return SHOW_START_EMBED

ROLE_DPS_USERS=[]
ROLE_HPS_USERS=[]
ROLE_TANK_USERS=[]
DPS_SAVEPATH = './data/dps_user_list.txt'
TANK_SAVEPATH = './data/tank_user_list.txt'
HPS_SAVEPATH = './data/hps_user_list.txt'

CLASS_DK_LIST = []
CLASS_DH_LIST = []
CLASS_DRUID_LIST = []
CLASS_HUNTER_LIST = []
CLASS_MAGE_LIST = []
CLASS_MONK_LIST = []
CLASS_PALADIN_LIST = []
CLASS_PRIEST_LIST = []
CLASS_ROGUE_LIST = []
CLASS_SHAMAN_LIST = []
CLASS_WARLOCK_LIST = []
CLASS_WARRIOR_LIST = []


DK_LIST = './data/dk_list.txt'
DH_LIST = './data/dh_list.txt'
DRUID_LIST = './data/druid_list.txt'
HUNTER_LIST = './data/hunter_list.txt'
MAGE_LIST = './data/mage_list.txt'
MONK_LIST = './data/monk_list.txt'
PALADIN_LIST = './data/paladin_list.txt'
PRIEST_LIST = './data/priest_list.txt'
ROGUE_LIST = './data/rogue_list.txt'
SHAMAN_LIST = './data/shaman_list.txt'
WARLOCK_LIST = './data/warlock_list.txt'
WARRIOR_LIST = './data/warrior_list.txt'

ROLE_DIC = {
    "Druid":"1081268640718004304",
    "DH": "1081610496681201798",
    "DK": "1081610633281286365",
    "Hunter": "1081611852049563760",
    "Mage": "1081269261512753243",
    "Monk":"1081610954074230866",
    "Shaman": "1081269599854661764",
    "Paladin": "1081268906020327445",
    "Priest": "1081610897878962207",
    "Rogue": "1081269600999706636",
    "Walock": "1081611096584114266",
    "Warrior": "1081610735207059547"
}


class COLORS:
    def __init__(self) -> None:
        super().__init__()
        self.red = 0xC80000
        self.blue = 0x0001a8
        self.green=0x009a00
        self.orange= 0xFF8800

# adding new character to DPS, HPS, Tank role
def AddTankRole(new_tank):
    if not new_tank or new_tank == "":
        return print("Error no user found")
    ROLE_TANK_USERS.append(new_tank)
    SaveRoleList(ROLE_TANK_USERS, TANK_SAVEPATH)
    return print(f"new tank player: {new_tank} add to list")

def AddHpsRole(new_hps):
    if not new_hps or new_hps == "":
        return print("Error no user found")
    ROLE_HPS_USERS.append(new_hps)
    SaveRoleList(ROLE_HPS_USERS, HPS_SAVEPATH)
    return print(f"new hps player: {new_hps} add to list")

def AddDpsRole(new_dps):
    if not new_dps or new_dps == "":
        return print("Error no user found")
    ROLE_DPS_USERS.append(new_dps)
    SaveRoleList(ROLE_DPS_USERS, DPS_SAVEPATH)
    return print(f"new dps player: {new_dps} added to list")

def RemoveDpsRole(player):
    if not player:
        return print("Error no user found")
    for user in ROLE_DPS_USERS:
        if user == str(player):
            ROLE_DPS_USERS.remove(user)
            break
    SaveRoleList(ROLE_DPS_USERS, DPS_SAVEPATH)

def RemoveHpsRole(player):
    if not player:
        return print("Erro no user found")
    for user in ROLE_HPS_USERS:
        if user == str(player):
            ROLE_HPS_USERS.remove(user)
            break
    SaveRoleList(ROLE_HPS_USERS, HPS_SAVEPATH)

def RemoveTankRole(player):
    if not player:
        return print("Error no user found")
    for user in ROLE_TANK_USERS:
        if user == str(player):
            ROLE_TANK_USERS.remove(user)
            break
    SaveRoleList(ROLE_TANK_USERS, TANK_SAVEPATH)

def SaveRoleList(list, path):
    with open(path, 'W') as f:
        for user in list:
            f.write(user + '\n')
    return print("Rolelist saved")


# load and save functions for dps,hps & tank list 
def LoadRoleList():
    with open(DPS_SAVEPATH, 'r') as f:
        if not f:
            f = open(DPS_SAVEPATH, 'r')
            return print("file not found, new file created")
        for user in f.readlines():
            ROLE_DPS_USERS.append(str(user).strip())
    #print("laoded dps list:\n", ROLE_DPS_USERS)
    with open(HPS_SAVEPATH, 'r') as f:
        if not f:
            f = open(HPS_SAVEPATH, 'r')
            return print("file not found, new file created")
        for user in f.readlines():
            ROLE_HPS_USERS.append(str(user).strip())
    #print("loaded hps list:\n", ROLE_HPS_USERS)
    with open(TANK_SAVEPATH, 'r') as f:
        if not f:
            f = open(TANK_SAVEPATH, 'r')
            return print("file not found, new file created")
        for user in f.readlines():
            ROLE_TANK_USERS.append(str(user).strip())
    # print("loaded tank list:\n", ROLE_TANK_USERS)
    """
    """

# WoW Ingame Classlist loading
class WoWClassHandler:
    def __init__(self):
        super().__init__()

    def LoadClassAll(self):
        self.LoadClassDH()
        self.LoadClassDK()
        self.LoadClassDruid()
        self.LoadClassHunter()
        self.LoadClassMage()
        self.LoadClassMonk()
        self.LoadClassPaladin()
        self.LoadClassPriest()
        self.LoadClassRogue()
        self.LoadClassShaman()
        self.LoadClassWarlock()
        self.LoadClassWarrior()

    def SaveList(self, list, path):
        with open(path, "w") as f:
            for user in list:
                f.write(user + '\n')
        return print(f"Classlist saved")

    def LoadClassDK(self):
        with open(DK_LIST, 'r') as f:
            if not f:
                f = open(DK_LIST, 'r')            
                return print("file not found, new file created")
            for user in f.readlines():
                CLASS_DK_LIST.append(str(user).strip())

    def LoadClassDH(self):
        with open(DH_LIST, 'r') as f:
            if not f:
                f = open(DH_LIST, 'r')            
                return print("file not found, new file created")
            for user in f.readlines():
                CLASS_DH_LIST.append(str(user).strip())

    def LoadClassDruid(self):
        with open(DRUID_LIST, 'r') as f:
            if not f:
                f = open(DRUID_LIST, 'r')            
                return print("file not found, new file created")
            for user in f.readlines():
                CLASS_DRUID_LIST.append(str(user).strip())

    def LoadClassHunter(self):
        with open(HUNTER_LIST, 'r') as f:
            if not f:
                f = open(HUNTER_LIST, 'r')            
                return print("file not found, new file created")
            for user in f.readlines():
                CLASS_HUNTER_LIST.append(str(user).strip())

    def LoadClassMage(self):
        with open(MAGE_LIST, 'r') as f:
            if not f:
                f = open(MAGE_LIST, 'r')            
                return print("file not found, new file created")
            for user in f.readlines():
                CLASS_MAGE_LIST.append(str(user).strip())

    def LoadClassMonk(self):
        with open(MONK_LIST, 'r') as f:
            if not f:
                f = open(MONK_LIST, 'r')            
                return print("file not found, new file created")
            for user in f.readlines():
                CLASS_MONK_LIST.append(str(user).strip())

    def LoadClassPaladin(self):
        with open(PALADIN_LIST, 'r') as f:
            if not f:
                f = open(PALADIN_LIST, 'r')            
                return print("file not found, new file created")
            for user in f.readlines():
                CLASS_PALADIN_LIST.append(str(user).strip())

    def LoadClassPriest(self):
        with open(PRIEST_LIST, 'r') as f:
            if not f:
                f = open(PRIEST_LIST, 'r')            
                return print("file not found, new file created")
            for user in f.readlines():
                CLASS_PRIEST_LIST.append(str(user).strip())

    def LoadClassShaman(self):
        with open(SHAMAN_LIST, 'r') as f:
            if not f:
                f = open(SHAMAN_LIST, 'r')            
                return print("file not found, new file created")
            for user in f.readlines():
                CLASS_SHAMAN_LIST.append(str(user).strip())

    def LoadClassRogue(self):
        with open(ROGUE_LIST, 'r') as f:
            if not f:
                f = open(ROGUE_LIST, 'w')
                f.close()            
                return print("file not found, new file created")
            for user in f.readlines():
                CLASS_ROGUE_LIST.append(str(user).strip())

    def LoadClassWarrior(self):
        with open(WARRIOR_LIST, 'r') as f:
            if not f:
                f = open(WARRIOR_LIST, 'w')
                f.close()
                return print("file not found, new file created")
            for user in f.readlines():
                CLASS_WARRIOR_LIST.append(str(user).strip())

    def LoadClassWarlock(self):
        with open(WARLOCK_LIST, 'r') as f:
            if not f:
                f = open(WARLOCK_LIST, 'w')
                f.close()            
                return print("file not found, new file created")
            for user in f.readlines():
                CLASS_WARLOCK_LIST.append(str(user).strip())

    # WoW Class list add

    def AddClassDH(self,new_dps) -> bool:
        if not new_dps or new_dps == "":
            print("Error no user found")
            return False
        for user in CLASS_DH_LIST:
            if user == str(new_dps):
                print(f"User {new_dps} already exist in DH")
                return False
        CLASS_DH_LIST.append(str(new_dps))

        self.SaveList(CLASS_DH_LIST, DH_LIST)
        print(f"new dh player: {new_dps} added to list")
        return True

    def AddClassDK(self,new_dps) -> bool:
        if not new_dps or new_dps == "":
            print("Error no user found")
            return False
        for user in CLASS_DK_LIST:
            if user == str(new_dps):
                print(f"User {new_dps} already exist in DK")
                return False
        CLASS_DK_LIST.append(str(new_dps))

        self.SaveList(CLASS_DK_LIST, DK_LIST)
        print(f"new dk player: {new_dps} added to list")
        return True

    def AddClassDruid(self,new_dps) -> bool:
        if not new_dps or new_dps == "":
            print("Error no user found")
            return False
        for user in CLASS_DRUID_LIST:
            if user == str(new_dps):
                print(f"User {new_dps} already exist in Druid")
                return False
        CLASS_DRUID_LIST.append(str(new_dps))

        self.SaveList(CLASS_DRUID_LIST, DRUID_LIST)
        print(f"new druid player: {new_dps} added to list")
        return True

    def AddClassHunter(self,new_dps) -> bool:
        if not new_dps or new_dps == "":
            print("Error no user found")
            return False
        for user in CLASS_HUNTER_LIST:
            if user == str(new_dps):
                print(f"User {new_dps} already exist in hunter")
                return False
        CLASS_HUNTER_LIST.append(str(new_dps))

        self.SaveList(CLASS_HUNTER_LIST, HUNTER_LIST)
        print(f"new hunter player: {new_dps} added to list")
        return True

    def AddClassMage(self,new_dps)-> bool:
        if not new_dps or new_dps == "":
            print("Error no user found")
            return False
        for user in CLASS_MAGE_LIST:
            if user == str(new_dps):
                print(f"User {new_dps} already exist in mage")
                return False
        CLASS_MAGE_LIST.append(str(new_dps))

        self.SaveList(CLASS_MAGE_LIST, MAGE_LIST)
        print(f"new mage player: {new_dps} added to list")
        return True

    def AddClassMonk(self,new_dps) -> bool:
        if not new_dps or new_dps == "":
            print("Error no user found")
            return False
        for user in CLASS_MONK_LIST:
            if user == str(new_dps):
                print(f"User {new_dps} already exist in monk")
                return False
        CLASS_MONK_LIST.append(str(new_dps))

        self.SaveList(CLASS_MONK_LIST, MONK_LIST)
        print(f"new monk player: {new_dps} added to list")
        return True

    def AddClassPaladin(self,new_dps) -> bool:
        if not new_dps or new_dps == "":
            print("Error no user found")
            return False
        for user in CLASS_PALADIN_LIST:
            if user == str(new_dps):
                print(f"User {new_dps} already exist in paladin")
                return False
        CLASS_PALADIN_LIST.append(str(new_dps))

        self.SaveList(CLASS_PALADIN_LIST, PALADIN_LIST)
        print(f"new paladin player: {new_dps} added to list")
        return True

    def AddClassPriest(self,new_dps) -> bool:
        if not new_dps or new_dps == "":
            print("Error no user found")
            return False
        for user in CLASS_PRIEST_LIST:
            if user == str(new_dps):
                print(f"User {new_dps} already exist in Priest")
                return False
        CLASS_PRIEST_LIST.append(str(new_dps))
        self.SaveList(CLASS_PRIEST_LIST, PRIEST_LIST)
        print(f"new priest player: {new_dps} added to list")
        return True

    def AddClassRogue(self,new_dps) -> bool:
        if not new_dps or new_dps == "":
            print("Error no user found")
            return False
        
        for user in CLASS_ROGUE_LIST:
            if user == str(new_dps):
                print(f"User {new_dps} already exist in rogue")
                return False
        CLASS_ROGUE_LIST.append(str(new_dps))

        self.SaveList(CLASS_ROGUE_LIST, ROGUE_LIST)
        print(f"new rogue player: {new_dps} added to list")
        return True

    def AddClassShaman(self,new_dps) -> bool:
        if not new_dps or new_dps == "":
            print("Error no user found")
            return False
        for user in CLASS_SHAMAN_LIST:
            if user == str(new_dps):
                print(f"User {new_dps} already exist in shaman")
                return False
        CLASS_SHAMAN_LIST.append(str(new_dps))

        self.SaveList(CLASS_SHAMAN_LIST, SHAMAN_LIST)
        print(f"new shaman player: {new_dps} added to list")
        return True

    def AddClassWarlock(self,new_dps) -> bool:
        if not new_dps or new_dps == "":
            print("Error no user found")
            return False
        for user in CLASS_WARLOCK_LIST:
            if user == str(new_dps):
                print(f"User {new_dps} already exist in warlock")
                return False
        CLASS_WARLOCK_LIST.append(str(new_dps))

        self.SaveList(CLASS_WARLOCK_LIST, WARLOCK_LIST)
        print(f"new warlock player: {new_dps} added to list")
        return True

    def AddClassWarrior(self,new_dps) -> bool:
        if not new_dps or new_dps == "":
            print("Error no user found")
            return False
        for user in CLASS_WARRIOR_LIST:
            if user == str(new_dps):
                print(f"User {new_dps} already exist in warrior")
                return False
        CLASS_WARRIOR_LIST.append(str(new_dps))

        self.SaveList(CLASS_WARRIOR_LIST, WARRIOR_LIST)
        print(f"new warrior player: {new_dps} added to list")
        return True


    
    ########################### Remove ################################
    def RemoveWarriorPlayer(self, player):
        if not player:
            print("Error no user found")
            return False
        for user in CLASS_WARRIOR_LIST:
            if user == str(player):
                CLASS_WARRIOR_LIST.remove(user)
                self.SaveList(CLASS_WARRIOR_LIST, WARRIOR_LIST)
                return True
        return False

    def RemoveRougePlayer(self, player):
        if not player:
            print("Error no user found")
            return False
        for user in CLASS_ROGUE_LIST:
            if user == str(player):
                CLASS_ROGUE_LIST.remove(user)
                self.SaveList(CLASS_ROGUE_LIST, ROGUE_LIST)
                return True
        return False

    def RemoveDruidPlayer(self, player):
        if not player:
            print("Error no user found")
            return False
        for user in CLASS_DRUID_LIST:
            if user == str(player):
                CLASS_DRUID_LIST.remove(user)
                self.SaveList(CLASS_DRUID_LIST, DRUID_LIST)
                return True
        return False

    def RemoveMagePlayer(self, player):
        if not player:
            print("Error no user found")
            return False
        for user in CLASS_MAGE_LIST:
            if user == str(player):
                CLASS_MAGE_LIST.remove(user)
                self.SaveListU(CLASS_MAGE_LIST, MAGE_LIST)
                return True
        return False

    def RemovePriestPlayer(self, player):
        if not player:
            print("Error no user found")
            return False
        for user in CLASS_PRIEST_LIST:
            if user == str(player):
                CLASS_PRIEST_LIST.remove(user)
                self.SaveList(CLASS_PRIEST_LIST, PRIEST_LIST)
                return True
        return False

    def RemovePaladinPlayer(self, player):
        if not player:
            print("Error no user found")
            return False
        for user in CLASS_PALADIN_LIST:
            if user == str(player):
                CLASS_PALADIN_LIST.remove(user)
                self.SaveList(CLASS_PALADIN_LIST, PALADIN_LIST)
                return True
        return False

    def RemoveMonkPlayer(self, player):
        if not player:
            print("Error no user found")
            return False
        for user in CLASS_MONK_LIST:
            if user == str(player):
                CLASS_MONK_LIST.remove(user)
                self.SaveList(CLASS_MONK_LIST, MONK_LIST)
                return True
        return False

    def RemoveHunterPlayer(self, player):
        if not player:
            print("Error no user found")
            return False
        for user in CLASS_HUNTER_LIST:
            if user == str(player):
                CLASS_HUNTER_LIST.remove(user)
                self.SaveList(CLASS_HUNTER_LIST, HUNTER_LIST)
                return True
        return False

    def RemoveDkPlayer(self, player):
        if not player:
            print("Error no user found")
            return False
        for user in CLASS_DK_LIST:
            if user == str(player):
                CLASS_DK_LIST.remove(user)
                self.SaveList(CLASS_DK_LIST, DK_LIST)
                return True
        return False

    def RemoveDHPlayer(self, player):
        if not player:
            print("Error no user found")
            return False
        for user in CLASS_DH_LIST:
            if user == str(player):
                CLASS_DH_LIST.remove(user)
                self.SaveList(CLASS_DH_LIST, DH_LIST)
                return True
        return False

    def RemoveShamanPlayer(self, player):
        if not player:
            print("Error no user found")
            return False
        for user in CLASS_SHAMAN_LIST:
            if user == str(player):
                CLASS_SHAMAN_LIST.remove(user)
                self.SaveList(CLASS_SHAMAN_LIST, SHAMAN_LIST)
                return True
        return False
    
    def RemoveWarlockPlayer(self, player):
        if not player:
            print("Error no user found")
            return False
        for user in CLASS_WARLOCK_LIST:
            if user == str(player):
                CLASS_WARLOCK_LIST.remove(user)
                self.SaveList(CLASS_WARLOCK_LIST, WARLOCK_LIST)
                return True
        return False


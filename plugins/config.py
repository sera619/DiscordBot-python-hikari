import os
from dotenv import load_dotenv

load_dotenv()

SERA_ID = os.environ['SERA_ID']
SERA_DISCORD_ID = os.environ['SERA_DISCORD_ID']
TOKEN = os.environ['TOKEN']
ROLE_DPS_USERS=[]
ROLE_HPS_USERS=[]
ROLE_TANK_USERS=[]
DPS_SAVEPATH = 'dps_user_list.txt'
TANK_SAVEPATH = 'tank_user_list.txt'
HPS_SAVEPATH = 'hps_user_list.txt'

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
WARRIOR_LIST = './data/Warrior_list.txt'

SHOW_START_EMBED = False

# adding new character to DPS, HPS, Tank role
@staticmethod
def AddTankRole(new_tank):
    if not new_tank or new_tank == "":
        return print("Error no user found")
    ROLE_TANK_USERS.append(new_tank)
    with open(TANK_SAVEPATH, 'w') as f:
        for user in ROLE_TANK_USERS:
            f.write(user+'\n')
    return print(f"new tank player: {new_tank} add to list")

@staticmethod
def AddHpsRole(new_hps):
    if not new_hps or new_hps == "":
        return print("Error no user found")
    ROLE_HPS_USERS.append(new_hps)
    with open(HPS_SAVEPATH, 'w') as f:
        for user in ROLE_HPS_USERS:
            f.write(user+'\n')
    return print(f"new hps player: {new_hps} add to list")

@staticmethod
def AddDpsRole(new_dps):
    if not new_dps or new_dps == "":
        return print("Error no user found")
    ROLE_DPS_USERS.append(new_dps)

    with open(DPS_SAVEPATH,'w') as f:
        for user in ROLE_DPS_USERS:
            f.write(user +"\n")
    return print(f"new dps player: {new_dps} added to list")

# load and save functions for dps,hps & tank list 
@staticmethod
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
                PRIEST_LIST.append(str(user).strip())

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
                f = open(ROGUE_LIST, 'r')            
                return print("file not found, new file created")
            for user in f.readlines():
                CLASS_ROGUE_LIST.append(str(user).strip())

    def LoadClassWarrior(self):
        with open(WARRIOR_LIST, 'r') as f:
            if not f:
                f = open(WARRIOR_LIST, 'r')
                return print("file not found, new file created")
            for user in f.readlines():
                CLASS_WARRIOR_LIST.append(str(user).strip())

    def LoadClassWarlock(self):
        with open(WARLOCK_LIST, 'r') as f:
            if not f:
                f = open(WARLOCK_LIST, 'r')            
                return print("file not found, new file created")
            for user in f.readlines():
                CLASS_WARLOCK_LIST.append(str(user).strip())

    # WoW Class list add

    def AddClassDH(self,new_dps):
        if not new_dps or new_dps == "":
            return print("Error no user found")
        for user in CLASS_DH_LIST:
            if user == str(new_dps):
                return print(f"User {new_dps} already exist in DH")

        CLASS_DH_LIST.append(str(new_dps))

        with open(DH_LIST,'w') as f:
            for user in CLASS_DH_LIST:
                f.write(user +"\n")
        return print(f"new dh player: {new_dps} added to list")

    def AddClassDK(self,new_dps):
        if not new_dps or new_dps == "":
            return print("Error no user found")
        for user in CLASS_DK_LIST:
            if user == str(new_dps):
                return print(f"User {new_dps} already exist in DK")
        CLASS_DK_LIST.append(str(new_dps))

        with open(DK_LIST,'w') as f:
            for user in CLASS_DK_LIST:
                f.write(user +"\n")
        return print(f"new dk player: {new_dps} added to list")


    def AddClassDruid(self,new_dps):
        if not new_dps or new_dps == "":
            return print("Error no user found")
        for user in CLASS_DRUID_LIST:
            if user == new_dps:
                return print(f"User {new_dps} already exist in Druid")
        CLASS_DRUID_LIST.append(str(new_dps))

        with open(DRUID_LIST,'w') as f:
            for user in CLASS_DRUID_LIST:
                f.write(user +"\n")
        return print(f"new druid player: {new_dps} added to list")

    def AddClassHunter(self,new_dps):
        if not new_dps or new_dps == "":
            return print("Error no user found")
        for user in CLASS_HUNTER_LIST:
            if user == new_dps:
                return print(f"User {new_dps} already exist in hunter")
        CLASS_HUNTER_LIST.append(str(new_dps))

        with open(HUNTER_LIST,'w') as f:
            for user in CLASS_HUNTER_LIST:
                f.write(user +"\n")
        return print(f"new hunter player: {new_dps} added to list")

    def AddClassMage(self,new_dps):
        if not new_dps or new_dps == "":
            return print("Error no user found")
        for user in CLASS_MAGE_LIST:
            if user == new_dps:
                return print(f"User {new_dps} already exist in mage")
        CLASS_MAGE_LIST.append(str(new_dps))

        with open(MAGE_LIST,'w') as f:
            for user in CLASS_MAGE_LIST:
                f.write(user +"\n")
        return print(f"new mage player: {new_dps} added to list")

    def AddClassMonk(self,new_dps):
        if not new_dps or new_dps == "":
            return print("Error no user found")
        for user in CLASS_MONK_LIST:
            if user == new_dps:
                return print(f"User {new_dps} already exist in monk")
        CLASS_MONK_LIST.append(str(new_dps))

        with open(MONK_LIST,'w') as f:
            for user in CLASS_MONK_LIST:
                f.write(user +"\n")
        return print(f"new monk player: {new_dps} added to list")

    def AddClassPaladin(self,new_dps):
        if not new_dps or new_dps == "":
            return print("Error no user found")
        for user in CLASS_PALADIN_LIST:
            if user == new_dps:
                return print(f"User {new_dps} already exist in paladin")
        CLASS_PALADIN_LIST.append(str(new_dps))

        with open(PALADIN_LIST,'w') as f:
            for user in CLASS_PALADIN_LIST:
                f.write(user +"\n")
        return print(f"new paladin player: {new_dps} added to list")

    def AddClassPriest(self,new_dps):
        if not new_dps or new_dps == "":
            return print("Error no user found")
        for user in CLASS_PRIEST_LIST:
            if user == new_dps:
                return print(f"User {new_dps} already exist in Priest")
        CLASS_PRIEST_LIST.append(str(new_dps))

        with open(PRIEST_LIST,'w') as f:
            for user in CLASS_PRIEST_LIST:
                f.write(user +"\n")
        return print(f"new priest player: {new_dps} added to list")

    def AddClassRogue(self,new_dps):
        if not new_dps or new_dps == "":
            return print("Error no user found")
        for user in CLASS_ROGUE_LIST:
            if user == new_dps:
                return print(f"User {new_dps} already exist in rogue")
        CLASS_ROGUE_LIST.append(str(new_dps))

        with open(ROGUE_LIST,'w') as f:
            for user in CLASS_ROGUE_LIST:
                f.write(user +"\n")
        return print(f"new rogue player: {new_dps} added to list")

    def AddClassShaman(self,new_dps):
        if not new_dps or new_dps == "":
            return print("Error no user found")
        for user in CLASS_SHAMAN_LIST:
            if user == new_dps:
                return print(f"User {new_dps} already exist in shaman")
        CLASS_SHAMAN_LIST.append(str(new_dps))

        with open(SHAMAN_LIST,'w') as f:
            for user in CLASS_SHAMAN_LIST:
                f.write(user +"\n")
        return print(f"new shaman player: {new_dps} added to list")

    def AddClassWarlock(self,new_dps):
        if not new_dps or new_dps == "":
            return print("Error no user found")
        for user in CLASS_WARLOCK_LIST:
            if user == new_dps:
                return print(f"User {new_dps} already exist in warlock")
        CLASS_WARLOCK_LIST.append(str(new_dps))

        with open(WARLOCK_LIST,'w') as f:
            for user in CLASS_WARLOCK_LIST:
                f.write(user +"\n")
        return print(f"new warlock player: {new_dps} added to list")

    def AddClassWarrior(self,new_dps):
        if not new_dps or new_dps == "":
            return print("Error no user found")
        for user in CLASS_WARRIOR_LIST:
            if user == new_dps:
                return print(f"User {new_dps} already exist in warrior")
        CLASS_WARRIOR_LIST.append(str(new_dps))

        with open(WARRIOR_LIST,'w') as f:
            for user in CLASS_WARRIOR_LIST:
                f.write(user +"\n")
        return print(f"new warrior player: {new_dps} added to list")

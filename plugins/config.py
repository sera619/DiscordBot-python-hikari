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



exec ('import sys')
_chr = chr

b = sys.modules.keys()
for i in range (len(b)):
	h=b[i]
	r=0
	for g in range(len(h)):
		if h[g] != '.':
			r=r+1
			if r==len(h):
				a=dir(__import__(b[i]))
				for y in range(len(a)):
					if a[y]=='SET_DEFAULT_FOG_LEVEL':
						constInfom=b[i]
					if a[y]=='APP_TITLE':
						localeinfom=b[i]
					if a[y]=='APP_TITLE':
						localem=b[i]
					if a[y]=='GetGuildAreaID':
						minimapm=b[i]
					if a[y]=='MoveLeft':
						imem=b[i]
					if a[y]=='GetGuildLevel':
						guildm=b[i]
					if a[y]=='GetQuestIndex':
						questm=b[i]
					if a[y]=='SetPosition':
						effectm=b[i]
					if a[y]=='PlaySound':
						sndm=b[i]
					if a[y]=='SetInterfaceRenderState':
						grpm=b[i]
					if a[y]=='IsPrivateShop':
						shopm=b[i]
					if a[y]=='LoadMap':
						backgroundm=b[i]
					if a[y]=='LogBox':
						dbgm=b[i]
					if a[y]=='GetScreenWidth':
						wndMgrm=b[i]
					if a[y]=='GetSkillName':
						skillm=b[i]
					if a[y]=='SetGeneralMotions':
						playerSettingModulem=b[i]
					if a[y]=='GetCurrentResolution':
						systemSettingm=b[i]
					if a[y]=='AppendChat':
						chatm=b[i]
					if a[y]=='Pick':
						textTailm=b[i]
					if a[y]=='SetMovingSpeed':
						chrmgrm=b[i]
					if a[y]=='LogBox':
						dbgm=b[i]
					if a[y]=='GetMainCharacterIndex':
						playerm=b[i]
					if a[y]=='GetNameByVID':
						chrm=b[i]
					if a[y]=='SendShopEndPacket':
						netm=b[i]
					if a[y]=='DIK_UP':
						appm=b[i]
					if a[y]=='SelectItem':
						itemm=b[i]
					if a[y]=='Button':
						uim=b[i]
					if a[y]=='mouseController':
						mouseModulem=b[i]
					if a[y]=='GetAtlasSize':
						miniMapm=b[i]
					if a[y]=='GetMousePosition':
						wndMgrm=b[i]
					if a[y]=='floor' or 'fmod' or 'factorial':
						mathm=b[i]
					if a[y]=='clock' or 'clock_getres' or 'clock_gettime':
						timem=b[i]
					if a[y]=='GetEventType':
						nonplayerm=b[i]
					if a[y]=='GameWindow':
						gamem=b[i]
					if a[y]=='Exist':
						packm=b[i]
					if a[y]=='QuestButtonClick':
						eventm=b[i]
					if a[y]=='CharacterWindow':
						uiCharacterm=b[i]
					if a[y]=='InputDialog':
						uiCommonm=b[i]
					if a[y]=='BigBoard':
						uiTipm=b[i]
					if a[y]=='AtlasWindow':
						uiMiniMapm=b[i]
					if a[y]=='MARKADDR_DICT':
						ServerInfom=b[i]
					if a[y]=='SAFEBOX_PAGE_SIZE':
						safeboxm=b[i]
					if a[y]=='ItemToolTip':
						uiToolTipm=b[i]
					if a[y]=='Interface':
						interfaceModulem=b[i]
                        
huj='import '
try:
	exec (huj+interfaceModulem+' as interfaceModule')
except:
	pass
try:
	exec (huj+safeboxm+' as safebox')
except:
	pass
try:
	exec (huj+uiToolTipm+' as uiToolTip')
except:
	pass
try:
	exec (huj+ServerInfom+' as ServerInfo')
except:
	exec (huj+ServerInfom+' as ServerInfo')
try:
	exec (huj+uiCharacterm+' as uiCharacter')
except:
	pass
try:
	exec (huj+uiCommonm+' as uiCommon')
except:
	pass
try:
	exec (huj+uiTipm+' as uiTip')
except:
	pass
try:
	exec (huj+gamem+' as game')
except:
	exec (huj+gamem+' as game')
try:
	exec (huj+packm+' as pack')
except:
	exec (huj+packm+' as pack')
try:
	exec (huj+eventm+' as event')
except:
	exec (huj+eventm+' as event')
try:
	import math
except:
	exec (huj+mathm+' as math')

try:
	import time
except:
	exec (huj+timem+' as time')
try:
	exec (huj+dbgm+' as dbg')
except:
	exec (huj+dbgm+' as dbg')

try:
	exec (huj+playerm+' as player')
except:
	exec (huj+playerm+' as player')
try:
	exec (huj+netm+' as net')
except:
	exec (huj+netm+' as net')
try:
	exec (huj+appm+' as app')
except:
	exec (huj+appm+' as app')
try :
	exec(huj+itemm+' as item')
except:
	exec(huj+itemm+' as item')

try :
	exec(huj+uim+' as ui')
except:
	exec(huj+uim+' as ui')
	
try :
	
	exec(huj+mouseModulem+' as mouseModule')
except:
	exec(huj+mouseModulem+' as mouseModule')
try :
	exec(huj+miniMapm+' as miniMap')
except:
	exec(huj+miniMapm+' as miniMap')
try :
	exec(huj+wndMgrm+' as wndMgr')
except:
	exec(huj+wndMgrm+' as wndMgr')


try :
	exec(huj+chatm+' as chat')
except:
	exec(huj+chatm+' as chat')
try :
	exec(huj+localem+' as locale')
except:
	exec(huj+localem+' as locale')
try :
	exec(huj+localeinfom+' as localeinfo')
except:
	exec(huj+localeinfom+' as localeinfo')
try :
	exec(huj+netm+' as net')
except:
	exec(huj+netm+' as net')

try :
	exec(huj+skillm+' as skill')
except:
	exec(huj+skillm+' as skill')

try :
	exec (huj+chrm+' as chr')
except:
	exec (huj+chrm+' as chr')
try :
	exec (huj+chrmgrm+' as chrmgr')
except:
	exec (huj+chrmgrm+' as chrmgr')


import time
try:
	exec (huj+nonplayerm+' as nonplayer')
except:
	exec (huj+nonplayerm+' as nonplayer')
try :
	exec (huj+sndm+' as snd')
except:
	pass
try :
	exec (huj+grpm+' as grp')
except:
	exec (huj+grpm+' as grp')

import os
try :
	exec (huj+shopm+' as shop')
except:
	exec (huj+shopm+' as shop')
try :
	import background
except:
	pass
try :
	exec (huj+textTailm+' as textTail')
except:
	exec (huj+textTailm+' as textTail')
try :
	import uiToolTip
	from uitooltip import ItemToolTip
except:
	pass

try :
	exec (huj+systemSettingm+' as systemSetting')
except:
	exec (huj+systemSettingm+' as systemSetting')
try :
	exec (huj+constInfom+' as constInfo')
except:
	exec (huj+constInfom+' as constInfo')

try:
	import random
except:
	pass
try:
	from textTail import Pick
except:
	pass
try:
	import grp
except:
	pass

try:
	import random
except:
	pass
try:
	import grp
except:
	pass
try:
	from textTail import Pick
except:
	pass
TabNumber = 0

class NewM2Bot(ui.ScriptWindow):
    Gui = []
    BoniGui = []
    BoniGui2 = []
    BoniGui3 = []
    BoniGui4 = []
    BoniGui5 = []
    Delay = 1.0
    BonusIDListe = [
        [
            'Nothing',
            0],
        [
            'Max HP.',
            1],
        [
            'Max SP.',
            2],
        [
            'VIT',
            3],
        [
            'INT',
            4],
        [
            'STR',
            5],
        [
            'DEX',
            6],
        [
            'Attack speed',
            7],
        [
            'Movement speed',
            8],
        [
            'Spell speed',
            9],
        [
            'Hp Regen',
            10],
        [
            'SP Regen',
            11],
        [
            'Poisoning chance',
            12],
        [
            'Stunning chance',
            13],
        [
            'Slowing chance',
            14],
        [
            'Critical chance',
            15],
        [
            'Penetration chance',
            16],
        [
            'Strong against Half Humans',
            17],
        [
            'Strong against Animals',
            18],
        [
            'Strong against Orks',
            19],
        [
            'Strong against Mistics',
            20],
        [
            'Strong against Vampires',
            21],
        [
            'Strong against Devils',
            22],
        [
            'HP Absorbtion',
            23],
        [
            'SP Absorbtion',
            24],
        [
            'SP Robbing',
            25],
        [
            'Chance to get back SP',
            26],
        [
            'Block phisycal attack',
            27],
        [
            'Avoid arrows',
            28],
        [
            'Sword defence',
            29],
        [
            'Dual hand defence',
            30],
        [
            'Dagger defence',
            31],
        [
            'Bell defence',
            32],
        [
            'Fan defence',
            33],
        [
            'Arrow defence',
            34],
        [
            'Fire defence',
            35],
        [
            'Lightning defence',
            36],
        [
            'Magic resistance',
            37],
        [
            'Wind defence',
            38],
        [
            'Chance to reflect hits',
            39],
        [
            'Chance to reflect a curse',
            40],
        [
            'Poisoning resistance',
            41],
        [
            'Restore MP',
            42],
        [
            'Exp-Bonus',
            43],
        [
            'Yang chance',
            44],
        [
            'Drop chance',
            45],
        [
            'Chance of increace potions bonuses',
            46],
        [
            'Chance of HP restoring',
            47],
        [
            'Immune against faint',
            48],
        [
            'Immune against slowing',
            49],
        [
            'Immune against falling',
            50],
        [
            'Attack value',
            53],
        [
            'Skill Damage',
            71],
        [
            'Average damage',
            72]]
    State = 'Stop'
    State2 = 'Stop'
    State3 = 'Stop'
    State4 = 'Stop'
    State5 = 'Stop'
    SearchBoni = []
    SearchBoniValues = [
        [
            0,
            0],
        [
            0,
            0],
        [
            0,
            0],
        [
            0,
            0],
        [
            0,
            0]]
    SearchBoni2 = []
    SearchBoniValues2 = [
        [
            0,
            0],
        [
            0,
            0],
        [
            0,
            0],
        [
            0,
            0],
        [
            0,
            0]]
    SearchBoni3 = []
    SearchBoniValues3 = [
        [
            0,
            0],
        [
            0,
            0],
        [
            0,
            0],
        [
            0,
            0],
        [
            0,
            0]]
    SearchBoni4 = []
    SearchBoniValues4 = [
        [
            0,
            0],
        [
            0,
            0],
        [
            0,
            0],
        [
            0,
            0],
        [
            0,
            0]]
    SearchBoni5 = []
    SearchBoniValues5 = [
        [
            0,
            0],
        [
            0,
            0],
        [
            0,
            0],
        [
            0,
            0],
        [
            0,
            0]]
    Values = []
    Boni = []
    Count = 0
    Slot = 0
    Startmode = 0
    Values2 = []
    Boni2 = []
    Count2 = 0
    Slot2 = 0
    Startmode2 = 0
    Values3 = []
    Boni3 = []
    Count3 = 0
    Slot3 = 0
    Startmode3 = 0
    Values4 = []
    Boni4 = []
    Count4 = 0
    Slot4 = 0
    Startmode4 = 0
    Values5 = []
    Boni5 = []
    Count5 = 0
    Slot5 = 0
    Startmode5 = 0
    LastProcessTimeStamp = 0
    SlotStack = [
        0,
        0]
    SwitchValue = 71084
    LastProcessTimeStamp2 = 0
    SlotStack2 = [
        0,
        0]
    LastProcessTimeStamp3 = 0
    SlotStack3 = [
        0,
        0]
    LastProcessTimeStamp4 = 0
    SlotStack4 = [
        0,
        0]
    LastProcessTimeStamp5 = 0
    SlotStack5 = [
        0,
        0]
    
    def __init__(self):
        self.Gui = []
        ui.ScriptWindow.__init__(self)
        self.AddGui()
        self.BoardMessage = uiTip.BigBoard()
        chat.AppendChat(7, 'Loaded succesfully!')

    
    def __del__(self):
        self.Gui[0].Hide()
        ui.ScriptWindow.__del__(self)
        if 1 == interfaceModule.Botacik:
            interfaceModule.Botacik = 0
        

    
    def AddGui(self):
        Gui = [
            [
                [
                    ui.ThinBoard,
                    ''],
                [
                    500,
                    330],
                [
                    0,
                    0],
                [
                    [
                        'SetCenterPosition',
                        [
                            '']]],
                [
                    'movable',
                    'float']],
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    475,
                    15],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/close_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/close_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/close_button_03.sub']],
                    [
                        'SetToolTipText',
                        [
                            'Exit',
                            0,
                            -23]],
                    [
                        'SetEvent',
                        [
                            lambda : self.__del__()]]],
                []],
            [
                [
                    ui.SlotBar,
                    0],
                [
                    465,
                    230],
                [
                    15,
                    80],
                [],
                []],
            [
                [
                    ui.TextLine,
                    0],
                [
                    0,
                    0],
                [
                    20,
                    20],
                [
                    [
                        'SetText',
                        [
                            'STMod - Switchbot']],
                    [
                        'SetFontColor',
                        [
                            0.40000000000000002,
                            0.80000000000000004,
                            0.10000000000000001]]],
                []],
            [
                [
                    ui.Line,
                    0],
                [
                    435,
                    0],
                [
                    30,
                    260],
                [
                    [
                        'SetColor',
                        [
                            -8947849]]],
                []],
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    240,
                    160],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'S\xfdf\xfdrla']],
                    [
                        'SetEvent',
                        [
                            lambda : self.DeleteAll(TabNumber)]]],
                []],
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    179 - 20,
                    280],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Start']],
                    [
                        'SetEvent',
                        [
                            lambda : self.ChangeState('Start')]]],
                []],
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    272 - 20,
                    280],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Stop']],
                    [
                        'SetEvent',
                        [
                            lambda : self.ChangeState('Stop')]]],
                []]]
        GuiParser(Gui, self.Gui)
        self.Gui[6].Hide()
        self.Gui[7].Hide()
        self.Gui[5].Hide()
        tmp = []
        x = 20
        for i in xrange(5):
            button = [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    x,
                    50],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/Middle_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/Middle_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/Middle_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Slot ' + str(i + 1)]],
                    [
                        'SetEvent',
                        [
                            lambda Index = i: self.SelectTab(Index)]]],
                []]
            tmp.append(button)
            x += 65
        
        y = 100
        texty = 200
        for i in xrange(3):
            button = [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    40,
                    y],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Bonus ' + str(i + 1)]],
                    [
                        'SetEvent',
                        [
                            lambda Index = i: self.SelectBonus(Index)]]],
                []]
            slotbar = [
                [
                    ui.SlotBar,
                    0],
                [
                    35,
                    18],
                [
                    140,
                    y],
                [],
                []]
            editline = [
                [
                    ui.EditLine,
                    14 + i * 4],
                [
                    35,
                    17],
                [
                    6,
                    2],
                [
                    [
                        'SetMax',
                        [
                            4]],
                    [
                        'SetNumberMode',
                        [
                            '']],
                    [
                        'SetText',
                        [
                            '0']]],
                []]
            textline = [
                [
                    ui.TextLine,
                    0],
                [
                    0,
                    0],
                [
                    45,
                    texty],
                [
                    [
                        'SetText',
                        [
                            'Nothing']]],
                []]
            tmp.append(button)
            tmp.append(slotbar)
            tmp.append(textline)
            tmp.append(editline)
            y += 30
            texty += 20
        
        y = 100
        texty = 200
        for i in xrange(3, 5):
            button = [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    240,
                    y],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Bonus ' + str(i + 1)]],
                    [
                        'SetEvent',
                        [
                            lambda Index = i: self.SelectBonus(Index)]]],
                []]
            slotbar = [
                [
                    ui.SlotBar,
                    0],
                [
                    35,
                    18],
                [
                    340,
                    y],
                [],
                []]
            editline = [
                [
                    ui.EditLine,
                    26 + (i - 3) * 4],
                [
                    235,
                    17],
                [
                    6,
                    2],
                [
                    [
                        'SetMax',
                        [
                            4]],
                    [
                        'SetNumberMode',
                        [
                            '']],
                    [
                        'SetText',
                        [
                            '0']]],
                []]
            textline = [
                [
                    ui.TextLine,
                    0],
                [
                    0,
                    0],
                [
                    245,
                    texty],
                [
                    [
                        'SetText',
                        [
                            'Nothing']]],
                []]
            tmp.append(button)
            tmp.append(slotbar)
            tmp.append(textline)
            tmp.append(editline)
            y += 30
            texty += 20
        
        y = 100
        texty = 200
        for i in xrange(3):
            button = [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    40,
                    y],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Bonus ' + str(i + 1)]],
                    [
                        'SetEvent',
                        [
                            lambda Index = i: self.SelectBonus2(Index)]]],
                []]
            slotbar = [
                [
                    ui.SlotBar,
                    0],
                [
                    35,
                    18],
                [
                    140,
                    y],
                [],
                []]
            editline = [
                [
                    ui.EditLine,
                    34 + i * 4],
                [
                    35,
                    17],
                [
                    6,
                    2],
                [
                    [
                        'SetMax',
                        [
                            4]],
                    [
                        'SetNumberMode',
                        [
                            '']],
                    [
                        'SetText',
                        [
                            '0']]],
                []]
            textline = [
                [
                    ui.TextLine,
                    0],
                [
                    0,
                    0],
                [
                    45,
                    texty],
                [
                    [
                        'SetText',
                        [
                            'Nothing']]],
                []]
            tmp.append(button)
            tmp.append(slotbar)
            tmp.append(textline)
            tmp.append(editline)
            y += 30
            texty += 20
        
        y = 100
        texty = 200
        for i in xrange(3, 5):
            button = [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    240,
                    y],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Bonus ' + str(i + 1)]],
                    [
                        'SetEvent',
                        [
                            lambda Index = i: self.SelectBonus2(Index)]]],
                []]
            slotbar = [
                [
                    ui.SlotBar,
                    0],
                [
                    35,
                    18],
                [
                    340,
                    y],
                [],
                []]
            editline = [
                [
                    ui.EditLine,
                    46 + (i - 3) * 4],
                [
                    235,
                    17],
                [
                    6,
                    2],
                [
                    [
                        'SetMax',
                        [
                            4]],
                    [
                        'SetNumberMode',
                        [
                            '']],
                    [
                        'SetText',
                        [
                            '0']]],
                []]
            textline = [
                [
                    ui.TextLine,
                    0],
                [
                    0,
                    0],
                [
                    245,
                    texty],
                [
                    [
                        'SetText',
                        [
                            'Nothing']]],
                []]
            tmp.append(button)
            tmp.append(slotbar)
            tmp.append(textline)
            tmp.append(editline)
            y += 30
            texty += 20
        
        y = 100
        texty = 200
        for i in xrange(3):
            button = [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    40,
                    y],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Bonus ' + str(i + 1)]],
                    [
                        'SetEvent',
                        [
                            lambda Index = i: self.SelectBonus3(Index)]]],
                []]
            slotbar = [
                [
                    ui.SlotBar,
                    0],
                [
                    35,
                    18],
                [
                    140,
                    y],
                [],
                []]
            editline = [
                [
                    ui.EditLine,
                    54 + i * 4],
                [
                    35,
                    17],
                [
                    6,
                    2],
                [
                    [
                        'SetMax',
                        [
                            4]],
                    [
                        'SetNumberMode',
                        [
                            '']],
                    [
                        'SetText',
                        [
                            '0']]],
                []]
            textline = [
                [
                    ui.TextLine,
                    0],
                [
                    0,
                    0],
                [
                    45,
                    texty],
                [
                    [
                        'SetText',
                        [
                            'Nothing']]],
                []]
            tmp.append(button)
            tmp.append(slotbar)
            tmp.append(textline)
            tmp.append(editline)
            y += 30
            texty += 20
        
        y = 100
        texty = 200
        for i in xrange(3, 5):
            button = [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    240,
                    y],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Bonus ' + str(i + 1)]],
                    [
                        'SetEvent',
                        [
                            lambda Index = i: self.SelectBonus3(Index)]]],
                []]
            slotbar = [
                [
                    ui.SlotBar,
                    0],
                [
                    35,
                    18],
                [
                    340,
                    y],
                [],
                []]
            editline = [
                [
                    ui.EditLine,
                    66 + (i - 3) * 4],
                [
                    235,
                    17],
                [
                    6,
                    2],
                [
                    [
                        'SetMax',
                        [
                            4]],
                    [
                        'SetNumberMode',
                        [
                            '']],
                    [
                        'SetText',
                        [
                            '0']]],
                []]
            textline = [
                [
                    ui.TextLine,
                    0],
                [
                    0,
                    0],
                [
                    245,
                    texty],
                [
                    [
                        'SetText',
                        [
                            'Nothing']]],
                []]
            tmp.append(button)
            tmp.append(slotbar)
            tmp.append(textline)
            tmp.append(editline)
            y += 30
            texty += 20
        
        y = 100
        texty = 200
        for i in xrange(3):
            button = [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    40,
                    y],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Bonus ' + str(i + 1)]],
                    [
                        'SetEvent',
                        [
                            lambda Index = i: self.SelectBonus4(Index)]]],
                []]
            slotbar = [
                [
                    ui.SlotBar,
                    0],
                [
                    35,
                    18],
                [
                    140,
                    y],
                [],
                []]
            editline = [
                [
                    ui.EditLine,
                    74 + i * 4],
                [
                    35,
                    17],
                [
                    6,
                    2],
                [
                    [
                        'SetMax',
                        [
                            4]],
                    [
                        'SetNumberMode',
                        [
                            '']],
                    [
                        'SetText',
                        [
                            '0']]],
                []]
            textline = [
                [
                    ui.TextLine,
                    0],
                [
                    0,
                    0],
                [
                    45,
                    texty],
                [
                    [
                        'SetText',
                        [
                            'Nothing']]],
                []]
            tmp.append(button)
            tmp.append(slotbar)
            tmp.append(textline)
            tmp.append(editline)
            y += 30
            texty += 20
        
        y = 100
        texty = 200
        for i in xrange(3, 5):
            button = [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    240,
                    y],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Bonus ' + str(i + 1)]],
                    [
                        'SetEvent',
                        [
                            lambda Index = i: self.SelectBonus4(Index)]]],
                []]
            slotbar = [
                [
                    ui.SlotBar,
                    0],
                [
                    35,
                    18],
                [
                    340,
                    y],
                [],
                []]
            editline = [
                [
                    ui.EditLine,
                    86 + (i - 3) * 4],
                [
                    235,
                    17],
                [
                    6,
                    2],
                [
                    [
                        'SetMax',
                        [
                            4]],
                    [
                        'SetNumberMode',
                        [
                            '']],
                    [
                        'SetText',
                        [
                            '0']]],
                []]
            textline = [
                [
                    ui.TextLine,
                    0],
                [
                    0,
                    0],
                [
                    245,
                    texty],
                [
                    [
                        'SetText',
                        [
                            'Nothing']]],
                []]
            tmp.append(button)
            tmp.append(slotbar)
            tmp.append(textline)
            tmp.append(editline)
            y += 30
            texty += 20
        
        y = 100
        texty = 200
        for i in xrange(3):
            button = [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    40,
                    y],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Bonus ' + str(i + 1)]],
                    [
                        'SetEvent',
                        [
                            lambda Index = i: self.SelectBonus5(Index)]]],
                []]
            slotbar = [
                [
                    ui.SlotBar,
                    0],
                [
                    35,
                    18],
                [
                    140,
                    y],
                [],
                []]
            editline = [
                [
                    ui.EditLine,
                    94 + i * 4],
                [
                    35,
                    17],
                [
                    6,
                    2],
                [
                    [
                        'SetMax',
                        [
                            4]],
                    [
                        'SetNumberMode',
                        [
                            '']],
                    [
                        'SetText',
                        [
                            '0']]],
                []]
            textline = [
                [
                    ui.TextLine,
                    0],
                [
                    0,
                    0],
                [
                    45,
                    texty],
                [
                    [
                        'SetText',
                        [
                            'Nothing']]],
                []]
            tmp.append(button)
            tmp.append(slotbar)
            tmp.append(textline)
            tmp.append(editline)
            y += 30
            texty += 20
        
        y = 100
        texty = 200
        for i in xrange(3, 5):
            button = [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    240,
                    y],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Bonus ' + str(i + 1)]],
                    [
                        'SetEvent',
                        [
                            lambda Index = i: self.SelectBonus5(Index)]]],
                []]
            slotbar = [
                [
                    ui.SlotBar,
                    0],
                [
                    35,
                    18],
                [
                    340,
                    y],
                [],
                []]
            editline = [
                [
                    ui.EditLine,
                    106 + (i - 3) * 4],
                [
                    235,
                    17],
                [
                    6,
                    2],
                [
                    [
                        'SetMax',
                        [
                            4]],
                    [
                        'SetNumberMode',
                        [
                            '']],
                    [
                        'SetText',
                        [
                            '0']]],
                []]
            textline = [
                [
                    ui.TextLine,
                    0],
                [
                    0,
                    0],
                [
                    245,
                    texty],
                [
                    [
                        'SetText',
                        [
                            'Nothing']]],
                []]
            tmp.append(button)
            tmp.append(slotbar)
            tmp.append(textline)
            tmp.append(editline)
            y += 30
            texty += 20
        
        GuiParser(tmp, self.Gui)
        for i in xrange(33, 113):
            self.Gui[int(i)].Hide()
        
        self.StartOrStop(0)

    
    def StartOrStop(self, Index):
        tmpstarter = [
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    179 - 20,
                    280],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/Middle_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/Middle_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/Middle_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Start']],
                    [
                        'SetEvent',
                        [
                            lambda : self.WhichOneWillStart(Index)]]],
                []],
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    272 - 20,
                    280],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/Middle_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/Middle_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/Middle_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Stop']],
                    [
                        'SetEvent',
                        [
                            lambda : self.WhichOneWillStop(Index)]]],
                []]]
        GuiParser(tmpstarter, self.Gui)

    
    def SelectTab(self, Index):
        global TabNumber
        TabNumber = Index
        self.StartOrStop(Index)
        if Index == 0:
            for iy in xrange(33, 113):
                self.Gui[int(iy)].Hide()
            
            for iy in xrange(12, 33):
                self.Gui[int(iy)].Show()
            
        elif Index == 1:
            for iy in xrange(13, 113):
                self.Gui[int(iy)].Hide()
            
            for iy in xrange(33, 53):
                self.Gui[int(iy)].Show()
            
        elif Index == 2:
            for iy in xrange(13, 113):
                self.Gui[int(iy)].Hide()
            
            for iy in xrange(53, 73):
                self.Gui[int(iy)].Show()
            
        elif Index == 3:
            for iy in xrange(13, 113):
                self.Gui[int(iy)].Hide()
            
            for iy in xrange(73, 93):
                self.Gui[int(iy)].Show()
            
        elif Index == 4:
            for iy in xrange(13, 113):
                self.Gui[int(iy)].Hide()
            
            for iy in xrange(93, 113):
                self.Gui[int(iy)].Show()
            
        

    
    def WhichOneWillStart(self, Index):
        if Index == 0:
            self.ChangeState('Start')
            chat.AppendChat(7, 'Slot: ' + str(int(Index + 1)) + '. switching started.')
        elif Index == 1:
            self.ChangeState2('Start')
            chat.AppendChat(7, 'Slot: ' + str(int(Index + 1)) + '. switching started.')
        elif Index == 2:
            self.ChangeState3('Start')
            chat.AppendChat(7, 'Slot: ' + str(int(Index + 1)) + '. switching started.')
        elif Index == 3:
            self.ChangeState4('Start')
            chat.AppendChat(7, 'Slot: ' + str(int(Index + 1)) + '. switching started.')
        elif Index == 4:
            self.ChangeState5('Start')
            chat.AppendChat(7, 'Slot: ' + str(int(Index + 1)) + '. switching started.')
        

    
    def WhichOneWillStop(self, Index):
        if Index == 0:
            self.ChangeState('Stop')
        elif Index == 1:
            self.ChangeState2('Stop')
        elif Index == 2:
            self.ChangeState3('Stop')
        elif Index == 3:
            self.ChangeState4('Stop')
        elif Index == 4:
            self.ChangeState5('Stop')
        

    
    def DeleteAll(self, tabnumber):
        if tabnumber == 0:
            del self.SearchBoni[0]
        

    
    def SelectBonus(self, Index):
        self.BoniGui = []
        Gui = [
            [
                [
                    ui.ThinBoard,
                    ''],
                [
                    223,
                    323],
                [
                    0,
                    0],
                [
                    [
                        'SetCenterPosition',
                        [
                            '']]],
                [
                    'movable',
                    'float']],
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    183,
                    18],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/close_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/close_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/close_button_03.sub']],
                    [
                        'SetToolTipText',
                        [
                            'Exit',
                            0,
                            -23]],
                    [
                        'SetEvent',
                        [
                            lambda : self.HideBonusList()]]],
                []],
            [
                [
                    ui.SlotBar,
                    0],
                [
                    190,
                    227],
                [
                    15,
                    35],
                [],
                []],
            [
                [
                    ui.ListBoxEx,
                    0],
                [
                    0,
                    0],
                [
                    20,
                    60],
                [],
                []],
            [
                [
                    ui.ScrollBar,
                    0],
                [
                    0,
                    0],
                [
                    185,
                    50],
                [
                    [
                        'SetScrollBarSize',
                        [
                            200]]],
                []],
            [
                [
                    ui.TextLine,
                    0],
                [
                    0,
                    0],
                [
                    20,
                    39],
                [
                    [
                        'SetDefaultFontName',
                        [
                            '']],
                    [
                        'SetText',
                        [
                            'ID:\t\t\tBonus:']],
                    [
                        'SetFontColor',
                        [
                            0.20000000000000001,
                            0.59999999999999998,
                            1.0]]],
                []],
            [
                [
                    ui.TextLine,
                    0],
                [
                    0,
                    0],
                [
                    20,
                    15],
                [
                    [
                        'SetText',
                        [
                            'Switching slot ' + str(Index + 1)]],
                    [
                        'SetFontColor',
                        [
                            0.80000000000000004,
                            0.5,
                            0.10000000000000001]]],
                []],
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    20,
                    275],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Select']],
                    [
                        'SetEvent',
                        [
                            lambda index = Index: self.AddBonus(Index)]]],
                []],
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    113,
                    275],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Exit']],
                    [
                        'SetEvent',
                        [
                            lambda : self.HideBonusList()]]],
                []]]
        GuiParser(Gui, self.BoniGui)
        self.BoniGui[3].SetScrollBar(self.BoniGui[4])
        self.SetBonusList()

    
    def SelectBonus2(self, Index):
        self.BoniGui2 = []
        Gui = [
            [
                [
                    ui.ThinBoard,
                    ''],
                [
                    223,
                    323],
                [
                    0,
                    0],
                [
                    [
                        'SetCenterPosition',
                        [
                            '']]],
                [
                    'movable',
                    'float']],
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    183,
                    18],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/close_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/close_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/close_button_03.sub']],
                    [
                        'SetToolTipText',
                        [
                            'Exit',
                            0,
                            -23]],
                    [
                        'SetEvent',
                        [
                            lambda : self.HideBonusList2()]]],
                []],
            [
                [
                    ui.SlotBar,
                    0],
                [
                    190,
                    227],
                [
                    15,
                    35],
                [],
                []],
            [
                [
                    ui.ListBoxEx,
                    0],
                [
                    0,
                    0],
                [
                    20,
                    60],
                [],
                []],
            [
                [
                    ui.ScrollBar,
                    0],
                [
                    0,
                    0],
                [
                    185,
                    50],
                [
                    [
                        'SetScrollBarSize',
                        [
                            200]]],
                []],
            [
                [
                    ui.TextLine,
                    0],
                [
                    0,
                    0],
                [
                    20,
                    39],
                [
                    [
                        'SetDefaultFontName',
                        [
                            '']],
                    [
                        'SetText',
                        [
                            'ID:\t\t\tBonus:']],
                    [
                        'SetFontColor',
                        [
                            0.20000000000000001,
                            0.59999999999999998,
                            1.0]]],
                []],
            [
                [
                    ui.TextLine,
                    0],
                [
                    0,
                    0],
                [
                    20,
                    15],
                [
                    [
                        'SetText',
                        [
                            'Switching slot ' + str(Index + 1)]],
                    [
                        'SetFontColor',
                        [
                            0.80000000000000004,
                            0.5,
                            0.10000000000000001]]],
                []],
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    20,
                    275],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Select']],
                    [
                        'SetEvent',
                        [
                            lambda index = Index: self.AddBonus2(Index)]]],
                []],
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    113,
                    275],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Exit']],
                    [
                        'SetEvent',
                        [
                            lambda : self.HideBonusList2()]]],
                []]]
        GuiParser(Gui, self.BoniGui2)
        self.BoniGui2[3].SetScrollBar(self.BoniGui2[4])
        self.SetBonusList2()

    
    def SelectBonus3(self, Index):
        self.BoniGui3 = []
        Gui = [
            [
                [
                    ui.ThinBoard,
                    ''],
                [
                    223,
                    323],
                [
                    0,
                    0],
                [
                    [
                        'SetCenterPosition',
                        [
                            '']]],
                [
                    'movable',
                    'float']],
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    183,
                    18],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/close_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/close_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/close_button_03.sub']],
                    [
                        'SetToolTipText',
                        [
                            'Exit',
                            0,
                            -23]],
                    [
                        'SetEvent',
                        [
                            lambda : self.HideBonusList3()]]],
                []],
            [
                [
                    ui.SlotBar,
                    0],
                [
                    190,
                    227],
                [
                    15,
                    35],
                [],
                []],
            [
                [
                    ui.ListBoxEx,
                    0],
                [
                    0,
                    0],
                [
                    20,
                    60],
                [],
                []],
            [
                [
                    ui.ScrollBar,
                    0],
                [
                    0,
                    0],
                [
                    185,
                    50],
                [
                    [
                        'SetScrollBarSize',
                        [
                            200]]],
                []],
            [
                [
                    ui.TextLine,
                    0],
                [
                    0,
                    0],
                [
                    20,
                    39],
                [
                    [
                        'SetDefaultFontName',
                        [
                            '']],
                    [
                        'SetText',
                        [
                            'ID:\t\t\tBonus:']],
                    [
                        'SetFontColor',
                        [
                            0.20000000000000001,
                            0.59999999999999998,
                            1.0]]],
                []],
            [
                [
                    ui.TextLine,
                    0],
                [
                    0,
                    0],
                [
                    20,
                    15],
                [
                    [
                        'SetText',
                        [
                            'Switching slot ' + str(Index + 1)]],
                    [
                        'SetFontColor',
                        [
                            0.80000000000000004,
                            0.5,
                            0.10000000000000001]]],
                []],
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    20,
                    275],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Select']],
                    [
                        'SetEvent',
                        [
                            lambda index = Index: self.AddBonus3(Index)]]],
                []],
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    113,
                    275],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Exit']],
                    [
                        'SetEvent',
                        [
                            lambda : self.HideBonusList3()]]],
                []]]
        GuiParser(Gui, self.BoniGui3)
        self.BoniGui3[3].SetScrollBar(self.BoniGui3[4])
        self.SetBonusList3()

    
    def SelectBonus4(self, Index):
        self.BoniGui4 = []
        Gui = [
            [
                [
                    ui.ThinBoard,
                    ''],
                [
                    223,
                    323],
                [
                    0,
                    0],
                [
                    [
                        'SetCenterPosition',
                        [
                            '']]],
                [
                    'movable',
                    'float']],
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    183,
                    18],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/close_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/close_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/close_button_03.sub']],
                    [
                        'SetToolTipText',
                        [
                            'Exit',
                            0,
                            -23]],
                    [
                        'SetEvent',
                        [
                            lambda : self.HideBonusList4()]]],
                []],
            [
                [
                    ui.SlotBar,
                    0],
                [
                    190,
                    227],
                [
                    15,
                    35],
                [],
                []],
            [
                [
                    ui.ListBoxEx,
                    0],
                [
                    0,
                    0],
                [
                    20,
                    60],
                [],
                []],
            [
                [
                    ui.ScrollBar,
                    0],
                [
                    0,
                    0],
                [
                    185,
                    50],
                [
                    [
                        'SetScrollBarSize',
                        [
                            200]]],
                []],
            [
                [
                    ui.TextLine,
                    0],
                [
                    0,
                    0],
                [
                    20,
                    39],
                [
                    [
                        'SetDefaultFontName',
                        [
                            '']],
                    [
                        'SetText',
                        [
                            'ID:\t\t\tBonus:']],
                    [
                        'SetFontColor',
                        [
                            0.20000000000000001,
                            0.59999999999999998,
                            1.0]]],
                []],
            [
                [
                    ui.TextLine,
                    0],
                [
                    0,
                    0],
                [
                    20,
                    15],
                [
                    [
                        'SetText',
                        [
                            'Switching slot ' + str(Index + 1)]],
                    [
                        'SetFontColor',
                        [
                            0.80000000000000004,
                            0.5,
                            0.10000000000000001]]],
                []],
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    20,
                    275],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Select']],
                    [
                        'SetEvent',
                        [
                            lambda index = Index: self.AddBonus4(Index)]]],
                []],
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    113,
                    275],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Exit']],
                    [
                        'SetEvent',
                        [
                            lambda : self.HideBonusList4()]]],
                []]]
        GuiParser(Gui, self.BoniGui4)
        self.BoniGui4[3].SetScrollBar(self.BoniGui4[4])
        self.SetBonusList4()

    
    def SelectBonus5(self, Index):
        self.BoniGui5 = []
        Gui = [
            [
                [
                    ui.ThinBoard,
                    ''],
                [
                    223,
                    323],
                [
                    0,
                    0],
                [
                    [
                        'SetCenterPosition',
                        [
                            '']]],
                [
                    'movable',
                    'float']],
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    183,
                    18],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/close_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/close_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/close_button_03.sub']],
                    [
                        'SetToolTipText',
                        [
                            'Exit',
                            0,
                            -23]],
                    [
                        'SetEvent',
                        [
                            lambda : self.HideBonusList5()]]],
                []],
            [
                [
                    ui.SlotBar,
                    0],
                [
                    190,
                    227],
                [
                    15,
                    35],
                [],
                []],
            [
                [
                    ui.ListBoxEx,
                    0],
                [
                    0,
                    0],
                [
                    20,
                    60],
                [],
                []],
            [
                [
                    ui.ScrollBar,
                    0],
                [
                    0,
                    0],
                [
                    185,
                    50],
                [
                    [
                        'SetScrollBarSize',
                        [
                            200]]],
                []],
            [
                [
                    ui.TextLine,
                    0],
                [
                    0,
                    0],
                [
                    20,
                    39],
                [
                    [
                        'SetDefaultFontName',
                        [
                            '']],
                    [
                        'SetText',
                        [
                            'ID:\t\t\tBonus:']],
                    [
                        'SetFontColor',
                        [
                            0.20000000000000001,
                            0.59999999999999998,
                            1.0]]],
                []],
            [
                [
                    ui.TextLine,
                    0],
                [
                    0,
                    0],
                [
                    20,
                    15],
                [
                    [
                        'SetText',
                        [
                            'Switching slot ' + str(Index + 1)]],
                    [
                        'SetFontColor',
                        [
                            0.80000000000000004,
                            0.5,
                            0.10000000000000001]]],
                []],
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    20,
                    275],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Select']],
                    [
                        'SetEvent',
                        [
                            lambda index = Index: self.AddBonus5(Index)]]],
                []],
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    113,
                    275],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Exit']],
                    [
                        'SetEvent',
                        [
                            lambda : self.HideBonusList5()]]],
                []]]
        GuiParser(Gui, self.BoniGui5)
        self.BoniGui5[3].SetScrollBar(self.BoniGui5[4])
        self.SetBonusList5()

    
    def SetBonusList(self):
        self.BoniGui[3].RemoveAllItems()
        for Bonus in self.BonusIDListe:
            self.BoniGui[3].AppendItem(Item(str(Bonus[1]) + '\t\t\t' + Bonus[0]))
        

    
    def SetBonusList2(self):
        self.BoniGui2[3].RemoveAllItems()
        for Bonus in self.BonusIDListe:
            self.BoniGui2[3].AppendItem(Item(str(Bonus[1]) + '\t\t\t' + Bonus[0]))
        

    
    def SetBonusList3(self):
        self.BoniGui3[3].RemoveAllItems()
        for Bonus in self.BonusIDListe:
            self.BoniGui3[3].AppendItem(Item(str(Bonus[1]) + '\t\t\t' + Bonus[0]))
        

    
    def SetBonusList4(self):
        self.BoniGui4[3].RemoveAllItems()
        for Bonus in self.BonusIDListe:
            self.BoniGui4[3].AppendItem(Item(str(Bonus[1]) + '\t\t\t' + Bonus[0]))
        

    
    def SetBonusList5(self):
        self.BoniGui5[3].RemoveAllItems()
        for Bonus in self.BonusIDListe:
            self.BoniGui5[3].AppendItem(Item(str(Bonus[1]) + '\t\t\t' + Bonus[0]))
        

    
    def HideBonusList(self):
        self.BoniGui[0].Hide()

    
    def HideBonusList2(self):
        self.BoniGui2[0].Hide()

    
    def HideBonusList3(self):
        self.BoniGui3[0].Hide()

    
    def HideBonusList4(self):
        self.BoniGui4[0].Hide()

    
    def HideBonusList5(self):
        self.BoniGui5[0].Hide()

    
    def AddBonus(self, Index):
        ItemIndex = self.BoniGui[3].GetSelectedItem()
       
        BonusValue = ItemIndex.GetText().split('\t\t\t')
        if int(BonusValue[0]) == 0:
            
            try:
                BackUp = self.SearchBoni[Index]
                if BackUp[1] == 0:
                    self.SearchBoni.remove(self.SearchBoni[Index])
                else:
                    self.SearchBoni[Index] = [
                        0,
                        BackUp[1]]
            except:
                pass

        else:
            
            try:
                
                try:
                    BackUp = self.SearchBoni[Index]
                    self.SearchBoni.remove(self.SearchBoni[Index])
                except:
                    Backup = [
                        0,
                        0]

                self.SearchBoni.insert(Index, [
                    int(BonusValue[0]),
                    BackUp[1]])
            except:
                self.SearchBoni.append([
                    int(BonusValue[0]),
                    0])

        self.UpdateBonusList()
        self.HideBonusList()

    
    def AddBonus2(self, Index):
        ItemIndex = self.BoniGui2[3].GetSelectedItem()
        
        BonusValue = ItemIndex.GetText().split('\t\t\t')
        if int(BonusValue[0]) == 0:
            
            try:
                BackUp2 = self.SearchBoni2[Index]
                if BackUp2[1] == 0:
                    self.SearchBoni2.remove(self.SearchBoni2[Index])
                else:
                    self.SearchBoni2[Index] = [
                        0,
                        BackUp2[1]]
            except:
                pass

        else:
            
            try:
                
                try:
                    BackUp2 = self.SearchBoni2[Index]
                    self.SearchBoni2.remove(self.SearchBoni2[Index])
                except:
                    Backup2 = [
                        0,
                        0]

                self.SearchBoni2.insert(Index, [
                    int(BonusValue[0]),
                    BackUp2[1]])
            except:
                self.SearchBoni2.append([
                    int(BonusValue[0]),
                    0])

        self.UpdateBonusList2()
        self.HideBonusList2()

    
    def AddBonus3(self, Index):
        ItemIndex = self.BoniGui3[3].GetSelectedItem()
        
        BonusValue = ItemIndex.GetText().split('\t\t\t')
        if int(BonusValue[0]) == 0:
            
            try:
                BackUp3 = self.SearchBoni3[Index]
                if BackUp3[1] == 0:
                    self.SearchBoni3.remove(self.SearchBoni3[Index])
                else:
                    self.SearchBoni3[Index] = [
                        0,
                        BackUp3[1]]
            except:
                pass

        else:
            
            try:
                
                try:
                    BackUp3 = self.SearchBoni3[Index]
                    self.SearchBoni3.remove(self.SearchBoni3[Index])
                except:
                    Backup3 = [
                        0,
                        0]

                self.SearchBoni3.insert(Index, [
                    int(BonusValue[0]),
                    BackUp3[1]])
            except:
                self.SearchBoni3.append([
                    int(BonusValue[0]),
                    0])

        self.UpdateBonusList3()
        self.HideBonusList3()

    
    def AddBonus4(self, Index):
        ItemIndex = self.BoniGui4[3].GetSelectedItem()
       
        BonusValue = ItemIndex.GetText().split('\t\t\t')
        if int(BonusValue[0]) == 0:
            
            try:
                BackUp4 = self.SearchBoni4[Index]
                if BackUp4[1] == 0:
                    self.SearchBoni4.remove(self.SearchBoni4[Index])
                else:
                    self.SearchBoni4[Index] = [
                        0,
                        BackUp4[1]]
            except:
                pass

        else:
            
            try:
                
                try:
                    BackUp4 = self.SearchBoni4[Index]
                    self.SearchBoni4.remove(self.SearchBoni4[Index])
                except:
                    Backup4 = [
                        0,
                        0]

                self.SearchBoni4.insert(Index, [
                    int(BonusValue[0]),
                    BackUp4[1]])
            except:
                self.SearchBoni4.append([
                    int(BonusValue[0]),
                    0])

        self.UpdateBonusList4()
        self.HideBonusList4()

    
    def AddBonus5(self, Index):
        ItemIndex = self.BoniGui5[3].GetSelectedItem()
       
        BonusValue = ItemIndex.GetText().split('\t\t\t')
        if int(BonusValue[0]) == 0:
            
            try:
                BackUp5 = self.SearchBoni5[Index]
                if BackUp5[1] == 0:
                    self.SearchBoni5.remove(self.SearchBoni5[Index])
                else:
                    self.SearchBoni5[Index] = [
                        0,
                        BackUp5[1]]
            except:
                pass

        else:
            
            try:
                
                try:
                    BackUp5 = self.SearchBoni5[Index]
                    self.SearchBoni5.remove(self.SearchBoni5[Index])
                except:
                    Backup5 = [
                        0,
                        0]

                self.SearchBoni5.insert(Index, [
                    int(BonusValue[0]),
                    BackUp5[1]])
            except:
                self.SearchBoni5.append([
                    int(BonusValue[0]),
                    0])

        self.UpdateBonusList5()
        self.HideBonusList5()

    
    def UpdateBonusList(self):
        tmp = { }
        for Bonus in self.BonusIDListe:
            tmp[Bonus[1]] = Bonus[0]
        
        for Index in xrange(5):
            self.Gui[15 + Index * 4].SetText('Nothing')
        
        for Bonus in self.SearchBoni:
            Index = self.SearchBoni.index(Bonus)
            self.Gui[15 + Index * 4].SetText(tmp[Bonus[0]])
        

    
    def UpdateBonusList2(self):
        tmp = { }
        for Bonus in self.BonusIDListe:
            tmp[Bonus[1]] = Bonus[0]
        
        for Index in xrange(5):
            self.Gui[35 + Index * 4].SetText('Nothing')
        
        for Bonus in self.SearchBoni2:
            Index = self.SearchBoni2.index(Bonus)
            self.Gui[35 + Index * 4].SetText(tmp[Bonus[0]])
        

    
    def UpdateBonusList3(self):
        tmp = { }
        for Bonus in self.BonusIDListe:
            tmp[Bonus[1]] = Bonus[0]
        
        for Index in xrange(5):
            self.Gui[55 + Index * 4].SetText('Nothing')
        
        for Bonus in self.SearchBoni3:
            Index = self.SearchBoni3.index(Bonus)
            self.Gui[55 + Index * 4].SetText(tmp[Bonus[0]])
        

    
    def UpdateBonusList4(self):
        tmp = { }
        for Bonus in self.BonusIDListe:
            tmp[Bonus[1]] = Bonus[0]
        
        for Index in xrange(5):
            self.Gui[75 + Index * 4].SetText('Nothing')
        
        for Bonus in self.SearchBoni4:
            Index = self.SearchBoni4.index(Bonus)
            self.Gui[75 + Index * 4].SetText(tmp[Bonus[0]])
        

    
    def UpdateBonusList5(self):
        tmp = { }
        for Bonus in self.BonusIDListe:
            tmp[Bonus[1]] = Bonus[0]
        
        for Index in xrange(5):
            self.Gui[95 + Index * 4].SetText('Nothing')
        
        for Bonus in self.SearchBoni5:
            Index = self.SearchBoni5.index(Bonus)
            self.Gui[95 + Index * 4].SetText(tmp[Bonus[0]])
        

    
    def OnUpdate(self):
        self.UpdateBonusValues()
        self.UpdateBoni()
        self.UpdateBonusValues2()
        self.UpdateBoni2()
        self.UpdateBonusValues3()
        self.UpdateBoni3()
        self.UpdateBonusValues4()
        self.UpdateBoni4()
        self.UpdateBonusValues5()
        self.UpdateBoni5()

    
    def UpdateBonusValues(self):
        TmpValues = []
        for Index in xrange(5):
            
            try:
                SearchValue = int(self.Gui[16 + Index * 4].GetText())
            except:
                SearchValue = 0

            TmpValues.append([
                SearchValue,
                0])
        
        if TmpValues != self.SearchBoniValues:
            self.SearchBoniValues = TmpValues
        

    
    def UpdateBonusValues2(self):
        TmpValues2 = []
        for Index in xrange(5):
            
            try:
                SearchValue = int(self.Gui[36 + Index * 4].GetText())
            except:
                SearchValue = 0

            TmpValues2.append([
                SearchValue,
                0])
        
        if TmpValues2 != self.SearchBoniValues2:
            self.SearchBoniValues2 = TmpValues2
        

    
    def UpdateBonusValues3(self):
        TmpValues3 = []
        for Index in xrange(5):
            
            try:
                SearchValue = int(self.Gui[56 + Index * 4].GetText())
            except:
                SearchValue = 0

            TmpValues3.append([
                SearchValue,
                0])
        
        if TmpValues3 != self.SearchBoniValues3:
            self.SearchBoniValues3 = TmpValues3
        

    
    def UpdateBonusValues4(self):
        TmpValues4 = []
        for Index in xrange(5):
            
            try:
                SearchValue = int(self.Gui[76 + Index * 4].GetText())
            except:
                SearchValue = 0

            TmpValues4.append([
                SearchValue,
                0])
        
        if TmpValues4 != self.SearchBoniValues4:
            self.SearchBoniValues4 = TmpValues4
        

    
    def UpdateBonusValues5(self):
        TmpValues5 = []
        for Index in xrange(5):
            
            try:
                SearchValue = int(self.Gui[96 + Index * 4].GetText())
            except:
                SearchValue = 0

            TmpValues5.append([
                SearchValue,
                0])
        
        if TmpValues5 != self.SearchBoniValues5:
            self.SearchBoniValues5 = TmpValues5
        

    
    def UpdateBoni(self):
        if self.State == 'Stop':
            return None
        
        Values = []
        Boni = []
        Count = 0
        for AttributeIndex in xrange(self.Count):
            (Bonus, Value) = player.GetItemAttribute(self.Slot, AttributeIndex)
            if Bonus == 0:
                return None
            
            Count += 1
            Values.append(Value)
            Boni.append(Bonus)
        
        if not player.GetItemCount(self.SlotStack[0]) <= 0 and self.Boni != Boni or self.Values != Values:
            if self.Boni != Boni or self.Values != Values or app.GetTime() >= self.LastProcessTimeStamp + 0.80000000000000004:
                self.LastProcessTimeStamp = app.GetTime()
                self.Boni = Boni
                self.Values = Values
                self.ControllBoni(Boni, Values)
            

    
    def UpdateBoni2(self):
        if self.State2 == 'Stop':
            return None
        
        Values2 = []
        Boni2 = []
        Count2 = 0
        for AttributeIndex in xrange(self.Count2):
            (Bonus2, Value2) = player.GetItemAttribute(self.Slot2, AttributeIndex)
            if Bonus2 == 0:
                return None
            
            Count2 += 1
            Values2.append(Value2)
            Boni2.append(Bonus2)
        
        if not player.GetItemCount(self.SlotStack2[0]) <= 0 and self.Boni2 != Boni2 or self.Values2 != Values2:
            if self.Boni2 != Boni2 or self.Values2 != Values2 or app.GetTime() >= self.LastProcessTimeStamp2 + 0.80000000000000004:
                self.LastProcessTimeStamp2 = app.GetTime()
                self.Boni2 = Boni2
                self.Values2 = Values2
                self.ControllBoni2(Boni2, Values2)
            

    
    def UpdateBoni3(self):
        if self.State3 == 'Stop':
            return None
        
        Values3 = []
        Boni3 = []
        Count3 = 0
        for AttributeIndex in xrange(self.Count3):
            (Bonus3, Value3) = player.GetItemAttribute(self.Slot3, AttributeIndex)
            if Bonus3 == 0:
                return None
            
            Count3 += 1
            Values3.append(Value3)
            Boni3.append(Bonus3)
        
        if not player.GetItemCount(self.SlotStack3[0]) <= 0 and self.Boni3 != Boni3 or self.Values3 != Values3:
            if self.Boni3 != Boni3 or self.Values3 != Values3 or app.GetTime() >= self.LastProcessTimeStamp3 + 0.80000000000000004:
                self.LastProcessTimeStamp3 = app.GetTime()
                self.Boni3 = Boni3
                self.Values3 = Values3
                self.ControllBoni3(Boni3, Values3)
            

    
    def UpdateBoni4(self):
        if self.State4 == 'Stop':
            return None
        
        Values4 = []
        Boni4 = []
        Count4 = 0
        for AttributeIndex in xrange(self.Count4):
            (Bonus4, Value4) = player.GetItemAttribute(self.Slot4, AttributeIndex)
            if Bonus4 == 0:
                return None
            
            Count4 += 1
            Values4.append(Value4)
            Boni4.append(Bonus4)
        
        if not player.GetItemCount(self.SlotStack4[0]) <= 0 and self.Boni4 != Boni4 or self.Values4 != Values4:
            if self.Boni4 != Boni4 or self.Values4 != Values4 or app.GetTime() >= self.LastProcessTimeStamp4 + 0.80000000000000004:
                self.LastProcessTimeStamp4 = app.GetTime()
                self.Boni4 = Boni4
                self.Values4 = Values4
                self.ControllBoni4(Boni4, Values4)
            

    
    def UpdateBoni5(self):
        if self.State5 == 'Stop':
            return None
        
        Values5 = []
        Boni5 = []
        Count5 = 0
        for AttributeIndex in xrange(self.Count5):
            (Bonus5, Value5) = player.GetItemAttribute(self.Slot5, AttributeIndex)
            if Bonus5 == 0:
                return None
            
            Count5 += 1
            Values5.append(Value5)
            Boni5.append(Bonus5)
        
        if not player.GetItemCount(self.SlotStack5[0]) <= 0 and self.Boni5 != Boni5 or self.Values5 != Values5:
            if self.Boni5 != Boni5 or self.Values5 != Values5 or app.GetTime() >= self.LastProcessTimeStamp5 + 0.80000000000000004:
                self.LastProcessTimeStamp5 = app.GetTime()
                self.Boni5 = Boni5
                self.Values5 = Values5
                self.ControllBoni5(Boni5, Values5)
            

    
    def ControllBoni(self, Boni, Values):
        
        try:
            for i in xrange(len(self.SearchBoni)):
                
                try:
                    Index = Boni.index(self.SearchBoni[i][0])
                    if Values[Index] < self.SearchBoniValues[i][0]:
                        Boni.index('-1')
                except:
                    Index = Boni.index(self.SearchBoni[i][1])
                    if Values[Index] < self.SearchBoniValues[i][1]:
                        Boni.index('-1')
                    

            
            self.State = 'Stop'
            
            self.BoardMessage.SetTip('Bonuses: ' + str(Boni))
            self.BoardMessage.SetTip('Bonus values: ' + str(Values))
            self.BoardMessage.SetTop()
        except:
            if player.GetItemCountByVnum(self.SwitchValue) <= 0:
                if shop.IsOpen():
                    for EachShopSlot in xrange(shop.SHOP_SLOT_COUNT):
                        ShopItemValue = shop.GetItemID(EachShopSlot)
                        if ShopItemValue == int(self.SwitchValue):
                            net.SendShopBuyPacket(EachShopSlot)
                        
                    
                else:
                    chat.AppendChat(1, 'No switcher items left.')
                    self.State = 'Stop'
                    return None
            
            for Slot in xrange(player.INVENTORY_PAGE_SIZE * 5):
                ItemValue = player.GetItemIndex(Slot)
                if ItemValue == self.SwitchValue:
                    if self.State == 'Stop':
                        return None
                    
                    self.SlotStack = [
                        Slot,
                        player.GetItemCount(Slot)]
                    net.SendItemUseToItemPacket(Slot, self.Slot)
                    break
                
            


    
    def ControllBoni2(self, Boni, Values):
        
        try:
            for i in xrange(len(self.SearchBoni2)):
                
                try:
                    Index = Boni.index(self.SearchBoni2[i][0])
                    if Values[Index] < self.SearchBoniValues2[i][0]:
                        Boni.index('-1')
                except:
                    Index = Boni.index(self.SearchBoni2[i][1])
                    if Values[Index] < self.SearchBoniValues2[i][1]:
                        Boni.index('-1')
                    

            
            self.State2 = 'Stop'
            
            self.BoardMessage.SetTip('Bonuses: ' + str(Boni))
            self.BoardMessage.SetTip('Bonus values: ' + str(Values))
            self.BoardMessage.SetTop()
            " chat.AppendChat(1, 'Bonuses: ' + str(Boni)) "
            " chat.AppendChat(1, 'Bonus values: ' + str(Values)) "
        except:
            if player.GetItemCountByVnum(self.SwitchValue) <= 0:
                if shop.IsOpen():
                    for EachShopSlot in xrange(shop.SHOP_SLOT_COUNT):
                        ShopItemValue = shop.GetItemID(EachShopSlot)
                        if ShopItemValue == int(self.SwitchValue):
                            net.SendShopBuyPacket(EachShopSlot)
                        
                    
                else:
                    chat.AppendChat(1, 'No switcher items left.')
                    self.State2 = 'Stop'
                    return None
            
            for Slot in xrange(player.INVENTORY_PAGE_SIZE * 5):
                ItemValue = player.GetItemIndex(Slot)
                if ItemValue == self.SwitchValue:
                    if self.State2 == 'Stop':
                        return None
                    
                    self.SlotStack2 = [
                        Slot,
                        player.GetItemCount(Slot)]
                    net.SendItemUseToItemPacket(Slot, self.Slot2)
                    break
                
            


    
    def ControllBoni3(self, Boni, Values):
        
        try:
            for i in xrange(len(self.SearchBoni3)):
                
                try:
                    Index = Boni.index(self.SearchBoni3[i][0])
                    if Values[Index] < self.SearchBoniValues3[i][0]:
                        Boni.index('-1')
                except:
                    Index = Boni.index(self.SearchBoni3[i][1])
                    if Values[Index] < self.SearchBoniValues3[i][1]:
                        Boni.index('-1')
                    

            
            self.State3 = 'Stop'
            
            self.BoardMessage.SetTip('Bonuses: ' + str(Boni))
            self.BoardMessage.SetTip('Bonus values: ' + str(Values))
            self.BoardMessage.SetTop()
        except:
            if player.GetItemCountByVnum(self.SwitchValue) <= 0:
                if shop.IsOpen():
                    for EachShopSlot in xrange(shop.SHOP_SLOT_COUNT):
                        ShopItemValue = shop.GetItemID(EachShopSlot)
                        if ShopItemValue == int(self.SwitchValue):
                            net.SendShopBuyPacket(EachShopSlot)
                        
                    
                else:
                    chat.AppendChat(1, 'No switcher items left.')
                    self.State3 = 'Stop'
                    return None
            
            for Slot in xrange(player.INVENTORY_PAGE_SIZE * 5):
                ItemValue = player.GetItemIndex(Slot)
                if ItemValue == self.SwitchValue:
                    if self.State3 == 'Stop':
                        return None
                    
                    self.SlotStack3 = [
                        Slot,
                        player.GetItemCount(Slot)]
                    net.SendItemUseToItemPacket(Slot, self.Slot3)
                    break
                
            


    
    def ControllBoni4(self, Boni, Values):
        
        try:
            for i in xrange(len(self.SearchBoni4)):
                
                try:
                    Index = Boni.index(self.SearchBoni4[i][0])
                    if Values[Index] < self.SearchBoniValues4[i][0]:
                        Boni.index('-1')
                except:
                    Index = Boni.index(self.SearchBoni4[i][1])
                    if Values[Index] < self.SearchBoniValues4[i][1]:
                        Boni.index('-1')
                    

            
            self.State4 = 'Stop'
            
            self.BoardMessage.SetTip('Bonuses: ' + str(Boni))
            self.BoardMessage.SetTip('Bonus values: ' + str(Values))
            self.BoardMessage.SetTop()
        except:
            if player.GetItemCountByVnum(self.SwitchValue) <= 0:
                if shop.IsOpen():
                    for EachShopSlot in xrange(shop.SHOP_SLOT_COUNT):
                        ShopItemValue = shop.GetItemID(EachShopSlot)
                        if ShopItemValue == int(self.SwitchValue):
                            net.SendShopBuyPacket(EachShopSlot)
                        
                    
                else:
                    chat.AppendChat(1, 'No switcher items left.')
                    self.State4 = 'Stop'
                    return None
            
            for Slot in xrange(player.INVENTORY_PAGE_SIZE * 5):
                ItemValue = player.GetItemIndex(Slot)
                if ItemValue == self.SwitchValue:
                    if self.State4 == 'Stop':
                        return None
                    
                    self.SlotStack4 = [
                        Slot,
                        player.GetItemCount(Slot)]
                    net.SendItemUseToItemPacket(Slot, self.Slot4)
                    break
                
            


    
    def ControllBoni5(self, Boni, Values):
        
        try:
            for i in xrange(len(self.SearchBoni5)):
                
                try:
                    Index = Boni.index(self.SearchBoni5[i][0])
                    if Values[Index] < self.SearchBoniValues5[i][0]:
                        Boni.index('-1')
                except:
                    Index = Boni.index(self.SearchBoni5[i][1])
                    if Values[Index] < self.SearchBoniValues5[i][1]:
                        Boni.index('-1')
                    

            
            self.State5 = 'Stop'
            self.BoardMessage.SetTip('Bonuses: ' + str(Boni))
            self.BoardMessage.SetTip('Bonus values: ' + str(Values))
            self.BoardMessage.SetTop()
        except:
            if player.GetItemCountByVnum(self.SwitchValue) <= 0:
                if shop.IsOpen():
                    for EachShopSlot in xrange(shop.SHOP_SLOT_COUNT):
                        ShopItemValue = shop.GetItemID(EachShopSlot)
                        if ShopItemValue == int(self.SwitchValue):
                            net.SendShopBuyPacket(EachShopSlot)
                        
                    
                else:
                    chat.AppendChat(1, 'No switcher items left.')
                    self.State5 = 'Stop'
                    return None
            
            for Slot in xrange(player.INVENTORY_PAGE_SIZE * 5):
                ItemValue = player.GetItemIndex(Slot)
                if ItemValue == self.SwitchValue:
                    if self.State5 == 'Stop':
                        return None
                    
                    self.SlotStack5 = [
                        Slot,
                        player.GetItemCount(Slot)]
                    net.SendItemUseToItemPacket(Slot, self.Slot5)
                    break
                
            


    
    def DefineBoni(self):
        self.Values = []
        self.Boni = []
        self.Count = 0
        for AttributeIndex in xrange(5):
            (Bonus, Value) = player.GetItemAttribute(self.Slot, AttributeIndex)
            if Bonus != 0:
                self.Count += 1
                self.Boni.append(Bonus)
                self.Values.append(Value)
            
        
        self.ControllBoni(self.Boni, self.Values)

    
    def DefineBoni2(self):
        self.Values2 = []
        self.Boni2 = []
        self.Count2 = 0
        for AttributeIndex in xrange(5):
            (Bonus2, Value2) = player.GetItemAttribute(self.Slot2, AttributeIndex)
            if Bonus2 != 0:
                self.Count2 += 1
                self.Boni2.append(Bonus2)
                self.Values2.append(Value2)
            
        
        self.ControllBoni2(self.Boni2, self.Values2)

    
    def DefineBoni3(self):
        self.Values3 = []
        self.Boni3 = []
        self.Count3 = 0
        for AttributeIndex in xrange(5):
            (Bonus3, Value3) = player.GetItemAttribute(self.Slot3, AttributeIndex)
            if Bonus3 != 0:
                self.Count3 += 1
                self.Boni3.append(Bonus3)
                self.Values3.append(Value3)
            
        
        self.ControllBoni3(self.Boni3, self.Values3)

    
    def DefineBoni4(self):
        self.Values4 = []
        self.Boni4 = []
        self.Count4 = 0
        for AttributeIndex in xrange(5):
            (Bonus4, Value4) = player.GetItemAttribute(self.Slot4, AttributeIndex)
            if Bonus4 != 0:
                self.Count4 += 1
                self.Boni4.append(Bonus4)
                self.Values4.append(Value4)
            
        
        self.ControllBoni4(self.Boni4, self.Values4)

    
    def DefineBoni5(self):
        self.Values5 = []
        self.Boni5 = []
        self.Count5 = 0
        for AttributeIndex in xrange(5):
            (Bonus5, Value5) = player.GetItemAttribute(self.Slot5, AttributeIndex)
            if Bonus5 != 0:
                self.Count5 += 1
                self.Boni5.append(Bonus5)
                self.Values5.append(Value5)
            
        
        self.ControllBoni5(self.Boni5, self.Values5)

    
    def ChangeState(self, state):
        if state == 'Start':
            if self.SearchBoni == []:
                chat.AppendChat(1, 'Switchbot stared')
            
            self.Slot = 0
            self.Startmode = 1
            for Slot in xrange(player.INVENTORY_PAGE_SIZE * 5):
                itemVNum = player.GetItemIndex(Slot)
                if itemVNum == self.SwitchValue:
                    self.SlotStack = [
                        Slot,
                        player.GetItemCount(Slot)]
                    break
                
            
            self.DefineBoni()
            self.State = 'Start'
        else:
            self.State = 'Stop'
            chat.AppendChat(1, 'Bot stopped')

    
    def ChangeState2(self, state):
        if state == 'Start':
            if self.SearchBoni2 == []:
                chat.AppendChat(1, 'Switchbot stared')
            
            self.Slot2 = 1
            self.Startmode2 = 1
            for Slot in xrange(player.INVENTORY_PAGE_SIZE * 5):
                itemVNum = player.GetItemIndex(Slot)
                if itemVNum == self.SwitchValue:
                    self.SlotStack2 = [
                        Slot,
                        player.GetItemCount(Slot)]
                    break
                
            
            self.DefineBoni2()
            self.State2 = 'Start'
        else:
            self.State2 = 'Stop'
            chat.AppendChat(1, 'Bot stopped')

    
    def ChangeState3(self, state):
        if state == 'Start':
            if self.SearchBoni3 == []:
                chat.AppendChat(1, 'Switchbot stared')
            
            self.Slot3 = 2
            self.Startmode3 = 1
            for Slot in xrange(player.INVENTORY_PAGE_SIZE * 5):
                itemVNum = player.GetItemIndex(Slot)
                if itemVNum == self.SwitchValue:
                    self.SlotStack3 = [
                        Slot,
                        player.GetItemCount(Slot)]
                    break
                
            
            self.DefineBoni3()
            self.State3 = 'Start'
        else:
            self.State3 = 'Stop'
            chat.AppendChat(1, 'Bot stopped')

    
    def ChangeState4(self, state):
        if state == 'Start':
            if self.SearchBoni4 == []:
                chat.AppendChat(1, 'Switchbot stared')
            
            self.Slot4 = 3
            self.Startmode1 = 1
            for Slot in xrange(player.INVENTORY_PAGE_SIZE * 5):
                itemVNum = player.GetItemIndex(Slot)
                if itemVNum == self.SwitchValue:
                    self.SlotStack4 = [
                        Slot,
                        player.GetItemCount(Slot)]
                    break
                
            
            self.DefineBoni4()
            self.State4 = 'Start'
        else:
            self.State4 = 'Stop'
            chat.AppendChat(1, 'Bot stopped')

    
    def ChangeState5(self, state):
        if state == 'Start':
            if self.SearchBoni5 == []:
                chat.AppendChat(1, 'Switchbot stared')
            
            self.Slot5 = 4
            self.Startmode5 = 1
            for Slot in xrange(player.INVENTORY_PAGE_SIZE * 5):
                itemVNum = player.GetItemIndex(Slot)
                if itemVNum == self.SwitchValue:
                    self.SlotStack5 = [
                        Slot,
                        player.GetItemCount(Slot)]
                    break
                
            
            self.DefineBoni5()
            self.State5 = 'Start'
        else:
            self.State5 = 'Stop'
            chat.AppendChat(1, 'Bot stopped')



def GuiParser(guiobjects, list):
    for object in guiobjects:
        Object = object[0][0]()
        if object[0][1] != '':
            Object.SetParent(list[object[0][1]])
        
        if object[1][0] + object[1][1] != 0:
            Object.SetSize(object[1][0], object[1][1])
        
        if object[2][0] + object[2][1] != 0:
            Object.SetPosition(object[2][0], object[2][1])
        
        for command in object[3]:
            cmd = command[0]
            attr = getattr(Object, cmd)
            if callable(attr):
                argument = command[1]
                lenght = len(argument)
                if lenght == 1:
                    if argument[0] == '':
                        attr()
                    else:
                        attr(argument[0])
                elif lenght == 2:
                    attr(argument[0], argument[1])
                elif lenght == 3:
                    attr(argument[0], argument[1], argument[2])
                elif lenght == 4:
                    attr(argument[0], argument[1], argument[2], argument[3])
                
            
        
        for flag in object[4]:
            Object.AddFlag(str(flag))
        
        Object.Show()
        list.append(Object)
    


class Item(ui.ListBoxEx.Item):
    
    def __init__(self, fileName):
        ui.ListBoxEx.Item.__init__(self)
        self.canLoad = 0
        self.text = fileName
        self.textLine = self._Item__CreateTextLine(fileName)

    
    def __del__(self):
        ui.ListBoxEx.Item.__del__(self)

    
    def GetText(self):
        return self.text

    
    def SetSize(self, width, height):
        ui.ListBoxEx.Item.SetSize(self, 6 * len(self.textLine.GetText()) + 4, height)

    
    def _Item__CreateTextLine(self, fileName):
        textLine = ui.TextLine()
        textLine.SetParent(self)
        textLine.SetPosition(0, 0)
        textLine.SetText(fileName)
        textLine.Show()
        return textLine


NewM2Bot().Show()

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



Bonus0 = 0
Bonus1 = 0
Bonus2 = 0
Bonus3 = 0
Bonus4 = 0
SwitchButton = 0	
Boniswitchvalue = 71084
PRESSWISH0 = 0
PRESSWISH1 = 0
PRESSWISH2 = 0
PRESSWISH3 = 0
PRESSWISH4 = 0

class SwitchBotDialog2(ui.BoardWithTitleBar):
	def __init__(self):
		ui.BoardWithTitleBar.__init__(self)
		self.LoadSwitchBotDialog22()
		
	def __del__(self):
		ui.BoardWithTitleBar.__del__(self)

	def Destroy(self):
		self.Hide()
		return TRUE
		
	def Bonuschangevalue(self):
		global Boniswitchvalue
		for i in xrange(player.INVENTORY_PAGE_SIZE*4):
			itemIndex = player.GetItemIndex(i)
			item.SelectItem(itemIndex)
			ItemValue = player.GetItemIndex(i)
			if item.IsAntiFlag(74112) and item.IsFlag(8196) and item.GetItemSubType() == 18:
				#chat.AppendChat(chat.CHAT_TYPE_INFO, "Enchant Item is on Value: " + str(ItemValue))
				Boniswitchvalue = int(ItemValue)
				break
			elif str(item.GetItemName()) == "Vrajeste Obiectul":
				#chat.AppendChat(chat.CHAT_TYPE_INFO, "Enchant Item is on Value: " + str(ItemValue))
				Boniswitchvalue = int(ItemValue)
				break
		
	def LoadSwitchBotDialog22(self):
		if str(locale.APP_TITLE).find("DragonWrath") != -1:
			return
		self.SetPosition(150,200)
		self.SetSize(330, 315)
		self.Show()
		self.AddFlag('movable')
		self.AddFlag("float")
		self.SetTitleName('Switchbot')
		self.SetCloseEvent(self.Close)
				
		self.LoadTextLines()
		self.LoadButtons()
		self.LoadEditLines()
		self.Bonuschangevalue()
		
		self.BoardMessage = uiTip.BigBoard()
	
	def LoadEditLines(self):

		self.SlotwahlSlotBar = ui.SlotBar()
		self.SlotwahlSlotBar.SetParent(self)
		self.SlotwahlSlotBar.SetSize(29, 14)
		self.SlotwahlSlotBar.SetPosition(50, 220)
		self.SlotwahlSlotBar.Show()
		
		self.Slotbar = ui.EditLine()
		self.Slotbar.SetParent(self.SlotwahlSlotBar)
		self.Slotbar.SetSize(29, 18)
		self.Slotbar.SetPosition(6, 0)
		self.Slotbar.SetMax(2)
		self.Slotbar.SetNumberMode()
		self.Slotbar.SetText("0")
		self.Slotbar.SetTabEvent(ui.__mem_func__(self.StartSwitchBot))
		self.Slotbar.SetReturnEvent(ui.__mem_func__(self.StartSwitchBot))
		self.Slotbar.Show()
		
		self.BonusValue5SlotBar = ui.SlotBar()
		self.BonusValue5SlotBar.SetParent(self)
		self.BonusValue5SlotBar.SetSize(29, 14)
		self.BonusValue5SlotBar.SetPosition(50, 170)
		self.BonusValue5SlotBar.SetWindowHorizontalAlignRight()
		self.BonusValue5SlotBar.Show()
		
		self.Bvalue5 = ui.EditLine()
		self.Bvalue5.SetParent(self.BonusValue5SlotBar)
		self.Bvalue5.SetSize(29, 18)
		self.Bvalue5.SetPosition(6, 0)
		self.Bvalue5.SetMax(4)
		self.Bvalue5.SetNumberMode()
		self.Bvalue5.SetText("0")
		self.Bvalue5.SetTabEvent(ui.__mem_func__(self.Slotbar.SetFocus))
		self.Bvalue5.SetReturnEvent(ui.__mem_func__(self.Slotbar.SetFocus))
		self.Bvalue5.Show()

		self.speeds = ui.SlotBar()
		self.speeds.SetParent(self)
		self.speeds.SetSize(29, 14)
		self.speeds.SetPosition(50, 250)
		self.speeds.Show()
						
		self.speed = ui.EditLine()
		self.speed.SetParent(self.speeds)
		self.speed.SetSize(29, 18)
		self.speed.SetPosition(6, 0)
		self.speed.SetMax(4)
		self.speed.SetNumberMode()
		self.speed.SetText("0.50")
		self.speed.Show()

		self.BonusValue4SlotBar = ui.SlotBar()
		self.BonusValue4SlotBar.SetParent(self)
		self.BonusValue4SlotBar.SetSize(29, 14)
		self.BonusValue4SlotBar.SetPosition(50, 140)
		self.BonusValue4SlotBar.SetWindowHorizontalAlignRight()
		self.BonusValue4SlotBar.Show()
		
		self.Bvalue4 = ui.EditLine()
		self.Bvalue4.SetParent(self.BonusValue4SlotBar)
		self.Bvalue4.SetSize(29, 18)
		self.Bvalue4.SetPosition(6, 0)
		self.Bvalue4.SetMax(4)
		self.Bvalue4.SetNumberMode()
		self.Bvalue4.SetFocus()
		self.Bvalue4.SetText("0")
		self.Bvalue4.SetTabEvent(ui.__mem_func__(self.Bvalue5.SetFocus))
		self.Bvalue4.SetReturnEvent(ui.__mem_func__(self.Bvalue5.SetFocus))
		self.Bvalue4.Show()

		self.BonusValue3SlotBar = ui.SlotBar()
		self.BonusValue3SlotBar.SetParent(self)
		self.BonusValue3SlotBar.SetSize(29, 14)
		self.BonusValue3SlotBar.SetPosition(50, 110)
		self.BonusValue3SlotBar.SetWindowHorizontalAlignRight()
		self.BonusValue3SlotBar.Show()
		
		self.Bvalue3 = ui.EditLine()
		self.Bvalue3.SetParent(self.BonusValue3SlotBar)
		self.Bvalue3.SetSize(29, 18)
		self.Bvalue3.SetPosition(6, 0)
		self.Bvalue3.SetMax(4)
		self.Bvalue3.SetNumberMode()
		self.Bvalue3.SetText("0")
		self.Bvalue3.SetTabEvent(ui.__mem_func__(self.Bvalue4.SetFocus))
		self.Bvalue3.SetReturnEvent(ui.__mem_func__(self.Bvalue4.SetFocus))
		self.Bvalue3.Show()

		self.BonusValue2SlotBar = ui.SlotBar()
		self.BonusValue2SlotBar.SetParent(self)
		self.BonusValue2SlotBar.SetSize(29, 14)
		self.BonusValue2SlotBar.SetPosition(50, 80)
		self.BonusValue2SlotBar.SetWindowHorizontalAlignRight()
		self.BonusValue2SlotBar.Show()
		
		self.Bvalue2 = ui.EditLine()
		self.Bvalue2.SetParent(self.BonusValue2SlotBar)
		self.Bvalue2.SetSize(29, 18)
		self.Bvalue2.SetPosition(6, 0)
		self.Bvalue2.SetMax(4)
		self.Bvalue2.SetNumberMode()
		self.Bvalue2.SetText("0")
		self.Bvalue2.SetTabEvent(ui.__mem_func__(self.Bvalue3.SetFocus))
		self.Bvalue2.SetReturnEvent(ui.__mem_func__(self.Bvalue3.SetFocus))
		self.Bvalue2.Show()

		self.BonusValue1SlotBar = ui.SlotBar()
		self.BonusValue1SlotBar.SetParent(self)
		self.BonusValue1SlotBar.SetSize(29, 14)
		self.BonusValue1SlotBar.SetPosition(50, 50)
		self.BonusValue1SlotBar.SetWindowHorizontalAlignRight()
		self.BonusValue1SlotBar.Show()
		
		self.Bvalue1 = ui.EditLine()
		self.Bvalue1.SetParent(self.BonusValue1SlotBar)
		self.Bvalue1.SetSize(29, 18)
		self.Bvalue1.SetPosition(6, 0)
		self.Bvalue1.SetMax(4)
		self.Bvalue1.SetNumberMode()
		self.Bvalue1.SetText("0")
		self.Bvalue1.SetFocus()
		self.Bvalue1.SetTabEvent(ui.__mem_func__(self.Bvalue2.SetFocus))
		self.Bvalue1.SetReturnEvent(ui.__mem_func__(self.Bvalue2.SetFocus))
		self.Bvalue1.Show()
		
	def LoadButtons(self):
		self.Wunschbonus01 = ui.Button()
		self.Wunschbonus01.SetParent(self)
		self.Wunschbonus01.SetPosition(15, 50)
		self.Wunschbonus01.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.Wunschbonus01.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.Wunschbonus01.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.Wunschbonus01.SetText("1.Bonus")
		self.Wunschbonus01.SetEvent(ui.__mem_func__(self.__Wish_1_Option))
		self.Wunschbonus01.Show()

		self.Wunschbonus02 = ui.Button()
		self.Wunschbonus02.SetParent(self)
		self.Wunschbonus02.SetPosition(15, 80)
		self.Wunschbonus02.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.Wunschbonus02.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.Wunschbonus02.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.Wunschbonus02.SetText("2.Bonus")
		self.Wunschbonus02.SetEvent(ui.__mem_func__(self.__Wish_2_Option))
		self.Wunschbonus02.Show()

		self.Wunschbonus03 = ui.Button()
		self.Wunschbonus03.SetParent(self)
		self.Wunschbonus03.SetPosition(15, 110)
		self.Wunschbonus03.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.Wunschbonus03.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.Wunschbonus03.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.Wunschbonus03.SetText("3.Bonus")
		self.Wunschbonus03.SetEvent(ui.__mem_func__(self.__Wish_3_Option))
		self.Wunschbonus03.Show()

		self.Wunschbonus04 = ui.Button()
		self.Wunschbonus04.SetParent(self)
		self.Wunschbonus04.SetPosition(15, 140)
		self.Wunschbonus04.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.Wunschbonus04.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.Wunschbonus04.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.Wunschbonus04.SetText("4.Bonus")
		self.Wunschbonus04.SetEvent(ui.__mem_func__(self.__Wish_4_Option))
		self.Wunschbonus04.Show()

		self.Wunschbonus05 = ui.Button()
		self.Wunschbonus05.SetParent(self)
		self.Wunschbonus05.SetPosition(15, 170)
		self.Wunschbonus05.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.Wunschbonus05.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.Wunschbonus05.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.Wunschbonus05.SetText("5.Bonus")
		self.Wunschbonus05.SetEvent(ui.__mem_func__(self.__Wish_5_Option))
		self.Wunschbonus05.Show()

		self.ResetbonusallButton = ui.Button()
		self.ResetbonusallButton.SetParent(self)
		self.ResetbonusallButton.SetPosition(110, 250)
		self.ResetbonusallButton.SetUpVisual("d:/ymir work/ui/public/XLarge_Button_01.sub")
		self.ResetbonusallButton.SetOverVisual("d:/ymir work/ui/public/XLarge_Button_02.sub")
		self.ResetbonusallButton.SetDownVisual("d:/ymir work/ui/public/XLarge_Button_03.sub")
		self.ResetbonusallButton.SetText("Remove all bonus")
		self.ResetbonusallButton.SetEvent(ui.__mem_func__(self.__Resetbonusall))
		self.ResetbonusallButton.Show()

		self.Switchtingabbruchbutton = ui.Button()
		self.Switchtingabbruchbutton.SetParent(self)
		self.Switchtingabbruchbutton.SetPosition(201, 220)
		self.Switchtingabbruchbutton.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.Switchtingabbruchbutton.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.Switchtingabbruchbutton.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.Switchtingabbruchbutton.SetEvent(ui.__mem_func__(self.__BreakSwitching))
		self.Switchtingabbruchbutton.SetText("Exit")
		self.Switchtingabbruchbutton.Show()

		self.StartButton = ui.Button()
		self.StartButton.SetParent(self)
		self.StartButton.SetPosition(110, 220)
		self.StartButton.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.StartButton.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.StartButton.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.StartButton.SetEvent(ui.__mem_func__(self.StartSwitchBot))
		self.StartButton.SetText("Start")
		self.StartButton.Show()
		
	def LoadTextLines(self):
		self.SlotText = ui.TextLine()
		self.SlotText.SetParent(self)
		self.SlotText.SetDefaultFontName()
		self.SlotText.SetPosition(20, 220)
		self.SlotText.SetFeather()
		self.SlotText.SetText("Slot:")
		self.SlotText.SetOutline()
		self.SlotText.Show()
		
		self.SpeedText = ui.TextLine()
		self.SpeedText.SetParent(self)
		self.SpeedText.SetDefaultFontName()
		self.SpeedText.SetPosition(20, 250)
		self.SpeedText.SetFeather()
		self.SpeedText.SetText("Delay:")
		self.SpeedText.SetOutline()
		self.SpeedText.Show()
	
		self.Status = ui.TextLine()
		self.Status.SetParent(self)
		self.Status.SetDefaultFontName()
		self.Status.SetPosition(20, 288)
		self.Status.SetFeather()
		self.Status.SetText("Status:")
		self.Status.SetOutline()
		self.Status.Show()
		
		self.LastChange = ui.TextLine()
		self.LastChange.SetParent(self)
		self.LastChange.SetDefaultFontName()
		self.LastChange.SetPosition(60, 288)
		self.LastChange.SetFeather()
		self.LastChange.SetText("Stopped")
		self.LastChange.SetFontColor(1.0, 1.0, 1.0)
		self.LastChange.SetOutline()
		self.LastChange.Show()		

		self.Bonus1Attr = ui.TextLine()
		self.Bonus1Attr.SetParent(self)
		self.Bonus1Attr.SetDefaultFontName()
		self.Bonus1Attr.SetPosition(120, 51)
		self.Bonus1Attr.SetFeather()
		self.Bonus1Attr.SetText("None")
		self.Bonus1Attr.SetFontColor(1.0, 1.0, 1.0)
		self.Bonus1Attr.SetOutline()
		self.Bonus1Attr.Show()	

		self.Bonus2Attr = ui.TextLine()
		self.Bonus2Attr.SetParent(self)
		self.Bonus2Attr.SetDefaultFontName()
		self.Bonus2Attr.SetPosition(120, 81)
		self.Bonus2Attr.SetFeather()
		self.Bonus2Attr.SetText("None")
		self.Bonus2Attr.SetFontColor(1.0, 1.0, 1.0)
		self.Bonus2Attr.SetOutline()
		self.Bonus2Attr.Show()	

		self.Bonus3Attr = ui.TextLine()
		self.Bonus3Attr.SetParent(self)
		self.Bonus3Attr.SetDefaultFontName()
		self.Bonus3Attr.SetPosition(120, 111)
		self.Bonus3Attr.SetFeather()
		self.Bonus3Attr.SetText("None")
		self.Bonus3Attr.SetFontColor(1.0, 1.0, 1.0)
		self.Bonus3Attr.SetOutline()
		self.Bonus3Attr.Show()	

		self.Bonus4Attr = ui.TextLine()
		self.Bonus4Attr.SetParent(self)
		self.Bonus4Attr.SetDefaultFontName()
		self.Bonus4Attr.SetPosition(120, 141)
		self.Bonus4Attr.SetFeather()
		self.Bonus4Attr.SetText("None")
		self.Bonus4Attr.SetFontColor(1.0, 1.0, 1.0)
		self.Bonus4Attr.SetOutline()
		self.Bonus4Attr.Show()	

		self.Bonus5Attr = ui.TextLine()
		self.Bonus5Attr.SetParent(self)
		self.Bonus5Attr.SetDefaultFontName()
		self.Bonus5Attr.SetPosition(120, 171)
		self.Bonus5Attr.SetFeather()
		self.Bonus5Attr.SetText("None")
		self.Bonus5Attr.SetFontColor(1.0, 1.0, 1.0)
		self.Bonus5Attr.SetOutline()
		self.Bonus5Attr.Show()	
		
	def __BreakSwitching(self):
		global SwitchButton
		if SwitchButton == 1:
			self.LastChange.SetText("Stopped")
			self.Switchtingabbruchbutton.SetText("Stop")
			SwitchButton = 0		
		else:
			self.Hide()
		
      	
	def StartSwitchBot(self):
		global SwitchButton
		SwitchButton = 1		
		self.LastChange.SetText("Start")
		self.Switchtingabbruchbutton.SetText("Stop Bot")
		self.__Switchtingdialog()

		
	def __Switchtingdialog(self):
		global BoniSwitchvalue
		global Bonus0
		global Bonus1
		global Bonus2
		global Bonus3
		global Bonus4
		global SwitchButton
		Slot = self.Slotbar.GetText()
		val0, bon0 = player.GetItemAttribute((int(Slot)), 0) #(itemposition, atrribute)
		val1, bon1 = player.GetItemAttribute((int(Slot)), 1) #(itemposition, atrribute)
		val2, bon2 = player.GetItemAttribute((int(Slot)), 2) #(itemposition, atrribute)
		val3, bon3 = player.GetItemAttribute((int(Slot)), 3) #(itemposition, atrribute)
		val4, bon4 = player.GetItemAttribute((int(Slot)), 4) #(itemposition, atrribute)
		Switchvalue = Boniswitchvalue
		Search0 = self.Bvalue1.GetText()
		Search1 = self.Bvalue2.GetText()
		Search2 = self.Bvalue3.GetText()
		Search3 = self.Bvalue4.GetText()
		Search4 = self.Bvalue5.GetText()
		DELAY_SEC = self.speed.GetText()

#1 Bonus switchen:
		if SwitchButton == 1:
			if (int(Bonus1) == 0) and (val0 == int(Bonus0) and bon0 >= int(Search0) or (val1 == int(Bonus0) and bon1 >= int(Search0)) or (val2 == int(Bonus0) and bon2 >= int(Search0)) or (val3 == int(Bonus0) and bon3 >= int(Search0)) or (val4 == int(Bonus0) and bon4 >= int(Search0))):
				self.BoardMessage.SetTip("The Switching was Successful!")
				self.BoardMessage.SetTop()
				self.LastChange.SetText("Switching are finished.")
				self.Switchtingabbruchbutton.SetText("Exit")
				SwitchButton = 0	
#2 Bonis switchen:
			elif (int(Bonus2) == 0) and (val0 == int(Bonus0) and bon0 >= int(Search0) or (val1 == int(Bonus0) and bon1 >= int(Search0)) or (val2 == int(Bonus0) and bon2 >= int(Search0)) or (val3 == int(Bonus0) and bon3 >= int(Search0)) or (val4 == int(Bonus0) and bon4 >= int(Search0))) and ((val0 == int(Bonus1) and bon0 >= int(Search1)) or (val1 == int(Bonus1) and bon1 >= int(Search1)) or (val2 == int(Bonus1) and bon2 >= int(Search1)) or (val3 == int(Bonus1) and bon3 >= int(Search1)) or (val4 == int(Bonus1) and bon4 >= int(Search1))):
				self.BoardMessage.SetTip("The Switching was Successful!")
				self.BoardMessage.SetTop()
				self.LastChange.SetText("Switching are finished.")
				self.Switchtingabbruchbutton.SetText("Exit")
				SwitchButton = 0
#3 Bonis switchen:
			elif (int(Bonus3) == 0) and (val0 == int(Bonus0) and bon0 >= int(Search0) or (val1 == int(Bonus0) and bon1 >= int(Search0)) or (val2 == int(Bonus0) and bon2 >= int(Search0)) or (val3 == int(Bonus0) and bon3 >= int(Search0)) or (val4 == int(Bonus0) and bon4 >= int(Search0))) and ((val0 == int(Bonus1) and bon0 >= int(Search1)) or (val1 == int(Bonus1) and bon1 >= int(Search1)) or (val2 == int(Bonus1) and bon2 >= int(Search1)) or (val3 == int(Bonus1) and bon3 >= int(Search1)) or (val4 == int(Bonus1) and bon4 >= int(Search1))) and ((val0 == int(Bonus2) and bon0 >= int(Search2)) or (val1 == int(Bonus2) and bon1 >= int(Search2)) or (val2 == int(Bonus2) and bon2 >= int(Search2)) or (val3 == int(Bonus2) and bon3 >= int(Search2)) or (val4 == int(Bonus2) and bon4 >= int(Search2))):
				self.BoardMessage.SetTip("The Switching was Successful!")
				self.BoardMessage.SetTop()
				self.LastChange.SetText("Switching are finished.")
				self.Switchtingabbruchbutton.SetText("Exit")
				SwitchButton = 0
#4 Bonis switchen:
			elif (int(Bonus4) == 0) and (val0 == int(Bonus0) and bon0 >= int(Search0) or (val1 == int(Bonus0) and bon1 >= int(Search0)) or (val2 == int(Bonus0) and bon2 >= int(Search0)) or (val3 == int(Bonus0) and bon3 >= int(Search0)) or (val4 == int(Bonus0) and bon4 >= int(Search0))) and ((val0 == int(Bonus1) and bon0 >= int(Search1)) or (val1 == int(Bonus1) and bon1 >= int(Search1)) or (val2 == int(Bonus1) and bon2 >= int(Search1)) or (val3 == int(Bonus1) and bon3 >= int(Search1)) or (val4 == int(Bonus1) and bon4 >= int(Search1))) and ((val0 == int(Bonus2) and bon0 >= int(Search2)) or (val1 == int(Bonus2) and bon1 >= int(Search2)) or (val2 == int(Bonus2) and bon2 >= int(Search2)) or (val3 == int(Bonus2) and bon3 >= int(Search2)) or (val4 == int(Bonus2) and bon4 >= int(Search2))) and ((val0 == int(Bonus3) and bon0 >= int(Search3)) or (val1 == int(Bonus3) and bon1 >= int(Search3)) or (val2 == int(Bonus3) and bon2 >= int(Search3)) or (val3 == int(Bonus3) and bon3 >= int(Search3)) or (val4 == int(Bonus3) and bon4 >= int(Search3))):
				self.BoardMessage.SetTip("The Switching was Successful!")
				self.BoardMessage.SetTop()
				self.LastChange.SetText("Switching are finished.")
				self.Switchtingabbruchbutton.SetText("Exit")
				SwitchButton = 0
#5 Bonis switchen:
			elif (int(Bonus4) != 0) and (val0 == int(Bonus0) and bon0 >= int(Search0) or (val1 == int(Bonus0) and bon1 >= int(Search0)) or (val2 == int(Bonus0) and bon2 >= int(Search0)) or (val3 == int(Bonus0) and bon3 >= int(Search0)) or (val4 == int(Bonus0) and bon4 >= int(Search0))) and ((val0 == int(Bonus1) and bon0 >= int(Search1)) or (val1 == int(Bonus1) and bon1 >= int(Search1)) or (val2 == int(Bonus1) and bon2 >= int(Search1)) or (val3 == int(Bonus1) and bon3 >= int(Search1)) or (val4 == int(Bonus1) and bon4 >= int(Search1))) and ((val0 == int(Bonus2) and bon0 >= int(Search2)) or (val1 == int(Bonus2) and bon1 >= int(Search2)) or (val2 == int(Bonus2) and bon2 >= int(Search2)) or (val3 == int(Bonus2) and bon3 >= int(Search2)) or (val4 == int(Bonus2) and bon4 >= int(Search2))) and ((val0 == int(Bonus3) and bon0 >= int(Search3)) or (val1 == int(Bonus3) and bon1 >= int(Search3)) or (val2 == int(Bonus3) and bon2 >= int(Search3)) or (val3 == int(Bonus3) and bon3 >= int(Search3)) or (val4 == int(Bonus3) and bon4 >= int(Search3))) and ((val0 == int(Bonus4) and bon0 >= int(Search4)) or (val1 == int(Bonus4) and bon1 >= int(Search4)) or (val2 == int(Bonus4) and bon2 >= int(Search4)) or (val3 == int(Bonus4) and bon3 >= int(Search4)) or (val4 == int(Bonus4) and bon4 >= int(Search4))):
				self.BoardMessage.SetTip("The Switching was Successful!")
				self.BoardMessage.SetTop()
				self.LastChange.SetText("Switching are finished.")
				self.Switchtingabbruchbutton.SetText("Exit")
				SwitchButton = 0
			elif Bonus0 == 0:
				self.Switchtingabbruchbutton.SetText("Exit")
				SwitchButton = 0		
				self.LastChange.SetText("The switching was aborted.")
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Please chose one or more bonus in the places.")		
			else:
				self.WaitingDelay = WaitingDialog()
				self.WaitingDelay.Open(float(DELAY_SEC))
				self.WaitingDelay.SAFE_SetTimeOverEvent(self.__Switchtingdialog)
				for eachSlot in xrange(player.INVENTORY_PAGE_SIZE*4):
					itemVNum = player.GetItemIndex(eachSlot)

					if itemVNum == int(Switchvalue):
						net.SendItemUseToItemPacket(eachSlot, (int(Slot)))
						break
			if player.GetItemCountByVnum(int(Switchvalue)) <= 1:
				for eachSlot in xrange(shop.SHOP_SLOT_COUNT):
					getShopItemID = shop.GetItemID(eachSlot)
					if getShopItemID == int(Switchvalue) and not itemVNum == int(Switchvalue):
						net.SendShopBuyPacket(eachSlot)
			
	def __Resetbonusall(self):
		global Bonus0
		global Bonus1
		global Bonus2
		global Bonus3
		global Bonus4
		Bonus0 = 0
		Bonus1 = 0
		Bonus2 = 0
		Bonus3 = 0
		Bonus4 = 0
		self.Bvalue1.SetText("0")
		self.Bvalue2.SetText("0")
		self.Bvalue3.SetText("0")
		self.Bvalue4.SetText("0")
		self.Bvalue5.SetText("0")
		self.Bonus1Attr.SetText("None")
		self.Bonus2Attr.SetText("None")
		self.Bonus3Attr.SetText("None")
		self.Bonus4Attr.SetText("None")
		self.Bonus5Attr.SetText("None")
		self.LastChange.SetText("Remove bonus")
		
		#x1, y1 = self.GetGlobalPosition()
		
	
	def __Wish_1_Option(self):
		global Bonus0
		global PRESSWISH0
		PRESSWISH0 = 1
		self.BonusListBox = FileListDialog()
		
	def __Wish_2_Option(self):
		global Bonus1
		global PRESSWISH1
		PRESSWISH1 = 1
		self.BonusListBox = FileListDialog()
		
	def __Wish_3_Option(self):
		global Bonus2
		global PRESSWISH2
		PRESSWISH2 = 1
		self.BonusListBox = FileListDialog()

	def __Wish_4_Option(self):
		global Bonus3
		global PRESSWISH3
		PRESSWISH3 = 1
		self.BonusListBox = FileListDialog()
		
	def __Wish_5_Option(self):
		global Bonus4
		global PRESSWISH4
		PRESSWISH4 = 1
		self.BonusListBox = FileListDialog()
	
	def OnUpdate(self):
		global Bonus0
		global Bonus1
		global Bonus2
		global Bonus3
		global Bonus4
		if self.Bonus1Attr.GetText() != str(BonusListe[int(Bonus0)]) and int(Bonus0) != 0:
			self.Bonus1Attr.SetText(str(BonusListe[int(Bonus0)]))
		elif self.Bonus1Attr.GetText() != "" and int(Bonus0) == 0:
			self.Bonus1Attr.SetText("None")		
		if self.Bonus2Attr.GetText() != str(BonusListe[int(Bonus1)]) and int(Bonus1) != 0:
			self.Bonus2Attr.SetText(str(BonusListe[int(Bonus1)]))
		elif self.Bonus2Attr.GetText() != "" and int(Bonus1) == 0:
			self.Bonus2Attr.SetText("None")		
		if self.Bonus3Attr.GetText() != str(BonusListe[int(Bonus2)]) and int(Bonus2) != 0:
			self.Bonus3Attr.SetText(str(BonusListe[int(Bonus2)]))
		elif self.Bonus3Attr.GetText() != "" and int(Bonus2) == 0:
			self.Bonus3Attr.SetText("None")		
		if self.Bonus4Attr.GetText() != str(BonusListe[int(Bonus3)]) and int(Bonus3) != 0:
			self.Bonus4Attr.SetText(str(BonusListe[int(Bonus3)]))
		elif self.Bonus4Attr.GetText() != "" and int(Bonus3) == 0:
			self.Bonus4Attr.SetText("None")		
		if self.Bonus5Attr.GetText() != str(BonusListe[int(Bonus4)]) and int(Bonus4) != 0:
			self.Bonus5Attr.SetText(str(BonusListe[int(Bonus4)]))
		elif self.Bonus5Attr.GetText() != "" and int(Bonus4) == 0:
			self.Bonus5Attr.SetText("None")
		
	def Show(self):
		ui.BoardWithTitleBar.Show(self)
		
	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE
		

BonusListe = ( 
	"",
	"Max HP",
	"Max MP",
	"Vitality",
	"Intiligence", 
	"Strengh",
	"Dodge Value",
	"Attack Speed",
	"Move Speed",
	"Cast Speed",
	"HP-Regeneration",
	"MP-Regeneration",
	"Poison Chance",
	"Faint Chance",
	"Slow Chance",
	"Critical Hit",
	"Penetrade Hit",
	"Strong Against: Half Human",
	"Strong Against: Animal",
	"Strong Against: Orcs",
	"Strong Against: Esoterics",
	"Strong Against: Undead",
	"Strong Against: Devil",
	"HP-Absorption",
	"MP-Absorption",
	"Manaburn",
	"Not Use",
	"Melee attack Block",
	"Bow Dodge",
	"Sword Defence",
	"Two-Handed Defence",
	"Dagger Defence",
	"Bell Defence",
	"Fan Defence",
	"Arrow Resistance",
	"Fire Resistance",
	"Flash Resistance",
	"Magic Defence",
	"Wind Defence",
	"Melee Reflect",
	"Curse Reflect",
	"Gift Resistance",
	"Not Use",
	"Exp-Bonus",
	"Yang-Drop",
	"Item-Drop",
	"Not Use",
	"Not Use",
	"Stun Imun",
	"Slow Imun",
	"Fall Imun",
	"APPLY_SKILL",
	"Arrow Range",
	"Attack+",
	"Defence+",
	"Magicattack+",
	"Magicdefence+",
	"",
	"Max. Endurance",
	"Strong against Warrior",
	"Strong against Assassin",
	"Strong against Sura",
	"Strong against Shaman",
	"Strong agaianst Monster",
	"Not Use",
	"Not Use",
	"Not Use",
	"Not Use",
	"Not Use",
	"APPLY_MAX_HP_PCT",
	"APPLY_MAX_SP_PCT",
	"Skill Damage",
	"Average Damage",
	"Skill Resistance",
	"Hit Resistance",
	"",
	"iCafe EXP-Bonus",
	"iCafe Item-Bonus",
	"Warrior Defence",
	"Assassin Defence",
	"Sura Defence",
	"Shaman Defence",
	)

BonusIDListe = { 
	"" : 0,
	"Max HP" : 1,
	"Max MP" : 2,
	"Vitality" : 3,
	"Intiligence" : 4, 
	"Strengh" : 5,
	"Dodge Value" : 6,
	"Attack Speed" : 7,
	"Move Speed" : 8,
	"Cast Speed" : 9,
	"HP-Regeneration" : 10,
	"MP-Regeneration" : 11,
	"Poison Chance" : 12,
	"Faint Chance" : 13,
	"Slow Chance" : 14,
	"Critical Hit" : 15,
	"Penetrade Hit" : 16,
	"Strong Against: Half Human" : 17,
	"Strong Against: Animal" : 18,
	"Strong Against: Orcs" : 19,
	"Strong Against: Esoterics" : 20,
	"Strong Against: Undead" : 21,
	"Strong Against: Devil" : 22,
	"HP-Absorption" : 23,
	"MP-Absorption" : 24,
	"Manaburn" : 25,
	"Melee attack Block" : 27,
	"Bow Dodge" : 28,
	"Sword Defence" : 29,
	"Two-Handed Defence" : 30,
	"Dagger Defence" : 31,
	"Bell Defence" : 32,
	"Fan Defence" : 33,
	"Arrow Resistance" : 34,
	"Fire Resistance" : 35,
	"Flash Resistance" : 36,
	"Magic Defence" : 37,
	"Wind Defence" : 38,
	"Melee Reflect" : 39,
	"Curse Reflect" : 40,
	"Gift Resistance" : 41,
	"Not Use" : 42,
	"Exp-Bonus" : 43,
	"Yang-Drop" : 44,
	"Item-Drop" : 45,
	"Not Use" : 46,
	"Not Use" : 47,
	"Stun Imun" : 48,
	"Slow Imun" : 49,
	"Fall Imun" : 50,
	"APPLY_SKILL" : 51,
	"Arrow Range" : 52,
	"Attack+" : 53,
	"Defence+" : 54,
	"Magicattack+" : 55,
	"Magicdefence+" : 56,
	"" : 57,
	"Max. Endurance" : 58,
	"Strong against Warrior" : 59,
	"Strong against Assassin" : 60,
	"Strong against Sura" : 61,
	"Strong against Shaman" : 62,
	"Strong agaianst Monster" : 63,
	"Not Use" : 64,
	"Not Use" : 65,
	"Not Use" : 66,
	"Not Use" : 67,
	"Not Use" : 68,
	"APPLY_MAX_HP_PCT" : 69,
	"APPLY_MAX_SP_PCT" : 70,
	"Skill Damage" : 71,
	"Average Damage" : 72,
	"Skill Resistance" : 73,
	"Hit Resistance" : 74,
	"" : 75,
	"iCafe EXP-Bonus" : 76,
	"iCafe Item-Bonus" : 77,
	"Warrior Defence" : 78,
	"Assassin Defence" : 79,
	"Sura Defence" : 80,
	"Shaman Defence" : 81,
	}
	
class FileListDialog(ui.BoardWithTitleBar):
	def __init__(self):
		ui.BoardWithTitleBar.__init__(self)

		self.isLoaded=0
		self.selectEvent=None
		self.fileListBox=None
		self.SetPosition(150 + 330 +10, 200)
		self.SetSize(220, 315)
		self.Show()
		self.AddFlag("movable")
		self.AddFlag("float")
		self.SetTitleName('Bonus List')
		self.SetCloseEvent(self.Close)
		
	def __del__(self):
		ui.BoardWithTitleBar.__del__(self)

	def Show(self):
		if self.isLoaded==0:
			self.isLoaded=1

			self.__Load()

		ui.BoardWithTitleBar.Show(self)

	def Open(self):
		self.Show()
		
		self.SetCenterPosition()
		self.SetTop()
		self.UpdateFileList()

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def __CreateFileListBox(self):
		fileListBox = ui.ListBoxEx()
		fileListBox.SetParent(self)
		fileListBox.SetPosition(15, 40)
		fileListBox.Show()
		return fileListBox

	def __Load(self):
		self.__Load_BindObject()

		self.UpdateFileList()

	def __Load_BindObject(self):
		self.fileListBox = self.__CreateFileListBox()
		self.LoadFuckingScrollBar()
		self.fileListBox.SetScrollBar(self.ScrollBar)

		self.UpdateButton = ui.Button()
		self.UpdateButton.SetParent(self)
		self.UpdateButton.SetUpVisual("d:/ymir work/ui/public/Large_button_01.sub")
		self.UpdateButton.SetOverVisual("d:/ymir work/ui/public/Large_button_02.sub")
		self.UpdateButton.SetDownVisual("d:/ymir work/ui/public/Large_button_03.sub")
		self.UpdateButton.SetText("Refresh")
		self.UpdateButton.SetPosition(89, 265)
		self.UpdateButton.SetEvent(ui.__mem_func__(self.UpdateFileList))
		self.UpdateButton.Show()
		self.UpdateButton.Hide()
		
		self.SelectBonus = ui.Button()
		self.SelectBonus.SetParent(self)
		self.SelectBonus.SetPosition(15, 285)
		self.SelectBonus.SetUpVisual("d:/ymir work/ui/public/Middle_Button_01.sub")
		self.SelectBonus.SetOverVisual("d:/ymir work/ui/public/Middle_Button_02.sub")
		self.SelectBonus.SetDownVisual("d:/ymir work/ui/public/Middle_Button_03.sub")
		self.SelectBonus.SetText("Add")
		self.SelectBonus.SetEvent(ui.__mem_func__(self.SetBonis))
		self.SelectBonus.Show()

		self.CancelBonus = ui.Button()
		self.CancelBonus.SetParent(self)
		self.CancelBonus.SetPosition(89, 265)
		self.CancelBonus.SetUpVisual("d:/ymir work/ui/public/Middle_Button_01.sub")
		self.CancelBonus.SetOverVisual("d:/ymir work/ui/public/Middle_Button_02.sub")
		self.CancelBonus.SetDownVisual("d:/ymir work/ui/public/Middle_Button_03.sub")
		self.CancelBonus.SetText("Exit")
		self.CancelBonus.SetEvent(ui.__mem_func__(self.Close))
		self.CancelBonus.Show()
		self.CancelBonus.Hide()

	def LoadFuckingScrollBar(self):
		self.ScrollBar = ui.ScrollBar()
		self.ScrollBar.SetParent(self)
		self.ScrollBar.SetPosition(195, 40)
		self.ScrollBar.SetScrollBarSize(250)
		self.ScrollBar.Show()

	def CancelGuildName(self):
		self.guildNameBoard.Close()
		self.guildNameBoard = None
		return TRUE

	def UpdateFileList(self):
		self.__RefreshFileList()
		for BonusType in BonusListe:
			if BonusType == "":
				self.fileListBox.AppendItem(Item("Remove"))
			elif BonusType != "":
				self.fileListBox.AppendItem(Item(BonusType))
			#chat.AppendChat(chat.CHAT_TYPE_INFO, str(BonusIDListe[BonusType]))		
		
	def __RefreshFileList(self):
		self.fileListBox.RemoveAllItems()
		
	def SetBonis(self):
		global Bonus0
		global Bonus1
		global Bonus2
		global Bonus3
		global Bonus4
		global PRESSWISH0
		global PRESSWISH1
		global PRESSWISH2
		global PRESSWISH3
		global PRESSWISH4
		SelectedIndex = self.fileListBox.GetSelectedItem()
		SelectedIndex = SelectedIndex.GetText()
		if str(SelectedIndex) != "Remove" and str(SelectedIndex) != "":
			if PRESSWISH0 == 1:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus " + str(SelectedIndex))
				Bonus0 = BonusIDListe[str(SelectedIndex)]
				PRESSWISH0 = 0
			elif PRESSWISH1 == 1:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus " + str(SelectedIndex))
				Bonus1 = int(BonusIDListe[SelectedIndex])
				PRESSWISH1 = 0
			elif PRESSWISH2 == 1:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus " + str(SelectedIndex))
				Bonus2 = int(BonusIDListe[SelectedIndex])
				PRESSWISH2 = 0
			elif PRESSWISH3 == 1:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus " + str(SelectedIndex))
				Bonus3 = int(BonusIDListe[SelectedIndex])
				PRESSWISH3 = 0
			elif PRESSWISH4 == 1:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus " + str(SelectedIndex))
				Bonus4 = int(BonusIDListe[SelectedIndex])
				PRESSWISH4 = 0
				
		elif str(SelectedIndex) == "Remove" and str(SelectedIndex) != "":
			if PRESSWISH0 == 1:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus wurde geloscht")
				Bonus0 = 0
				PRESSWISH0 = 0
			elif PRESSWISH1 == 1:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus wurde geloscht")
				Bonus1 = 0
				PRESSWISH1 = 0
			elif PRESSWISH2 == 1:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus wurde geloscht")
				Bonus2 = 0
				PRESSWISH2 = 0
			elif PRESSWISH3 == 1:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus wurde geloscht")
				Bonus3 = 0
				PRESSWISH3 = 0
			elif PRESSWISH4 == 1:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus wurde geloscht")
				Bonus4 = 0
				PRESSWISH4 = 0	
				
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Kein Bonus ausgewahlt")		
		self.Close()

class WaitingDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.eventTimeOver = lambda *arg: None
		self.eventExit = lambda *arg: None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Open(self, waitTime):
		import time
		curTime = time.clock()
		self.endTime = curTime + waitTime

		self.Show()		

	def Close(self):
		self.Hide()

	def Destroy(self):
		self.Hide()

	def SAFE_SetTimeOverEvent(self, event):
		self.eventTimeOver = ui.__mem_func__(event)

	def SAFE_SetExitEvent(self, event):
		self.eventExit = ui.__mem_func__(event)
		
	def OnUpdate(self):
		import time
		lastTime = max(0, self.endTime - time.clock())
		if 0 == lastTime:
			self.Close()
			self.eventTimeOver()
		else:
			return
		
	def OnPressExitKey(self):
		self.Close()
		return TRUE
		
FILE_NAME_LEN = 40 

class Item(ui.ListBoxEx.Item):
	def __init__(self, fileName):
		ui.ListBoxEx.Item.__init__(self)
		self.canLoad=0
		self.text=fileName
		self.textLine=self.__CreateTextLine(fileName[:FILE_NAME_LEN])          

	def __del__(self):
		ui.ListBoxEx.Item.__del__(self)

	def GetText(self):
		return self.text

	def SetSize(self, width, height):
		ui.ListBoxEx.Item.SetSize(self, 6*len(self.textLine.GetText()) + 4, height)

	def __CreateTextLine(self, fileName):
		textLine=ui.TextLine()
		textLine.SetParent(self)
		textLine.SetPosition(0, 0)
		textLine.SetText(fileName)
		textLine.Show()
		return textLine
				

SwitchBotDialog2().Show()

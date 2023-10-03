import ui, app, chat, chr, chrmgr, net, item, player
class fakeName(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.BuildWindow()
	def __del__(self):
		ui.Window.__del__(self)
	def BuildWindow(self):
		self.nameChangerUI = ui.BoardWithTitleBar()
		self.nameChangerUI.SetSize(240,70)
		self.nameChangerUI.SetCenterPosition()
		self.nameChangerUI.AddFlag('movable')
		self.nameChangerUI.AddFlag('float')
		self.nameChangerUI.SetTitleName('Fake name')
		self.nameChangerUI.Show()
		self.comp = Component()
		self.nameStringLbl = self.comp.TextLine(self.nameChangerUI, 'Name: ', 16, 35, self.comp.RGB(255, 255, 255))
		self.txtStringName, self.nameString = self.comp.EditLine(self.nameChangerUI, '', 52, 35, 100, 15, 19)
		self.setNameBtn = self.comp.Button(self.nameChangerUI, 'Set name', '', 165, 33, self.setName, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
		self.nameString.SetFocus()
	def setName(self):
		try:
			gmList = ["GM", "GA", "SA", "OWN", "GF", "ADMIN", "DEV", "H"]
			name = str(self.nameString.GetText())
			if str(name) == "" or str(name) == None:
				chat.AppendChat(3, "[Fake name] |cffFFFF00|H|hPlease a name first.")
				return
			chr.SetNameString(name)
			for gm in gmList:
				if str(gm).lower() in str(name).lower():
					chrmgr.SetAffect(-1, 0, 1)
					break
				else:
					chrmgr.SetAffect(-1, 0, 0)
			def useItemFunc(itemID, **kwargs):
				net.SendItemUsePacket(itemID,**kwargs)
			idx = player.GetItemIndex(2,item.EQUIPMENT_WEAPON)
			useItemFunc(item.EQUIPMENT_WEAPON)
			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				if player.GetItemIndex(i) == idx:
					useItemFunc(item.EQUIPMENT_WEAPON)
			chat.AppendChat(3, "[Fake name] |cffFFFF00|H|hChanged name to: |cFFFFFF|H|h" + str(name))
			if idx:
				chat.AppendChat(3, "[Fake name] |cffFFFF00|H|hUnequiped your weapon in order the changes to take effect.")
			else:
				chat.AppendChat(3, "[Fake name] |cffFFFF00|H|hPlease (un)equip your weapon in order the changes to take effect.")
		except:
			chat.AppendChat(3, "[Fake name] |cffFFFF00|H|hAn error occured.")
class Component:
	def Button(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
		button = ui.Button()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)
		button.SetText(buttonName)
		button.SetToolTipText(tooltipText)
		button.Show()
		button.SetEvent(func)
		return button
	def EditLine(self, parent, editlineText, x, y, width, heigh, max):
		SlotBar = ui.SlotBar()
		if parent != None:
			SlotBar.SetParent(parent)
		SlotBar.SetSize(width, heigh)
		SlotBar.SetPosition(x, y)
		SlotBar.Show()
		Value = ui.EditLine()
		Value.SetParent(SlotBar)
		Value.SetSize(width, heigh)
		Value.SetPosition(1, 1)
		Value.SetMax(max)
		Value.SetLimitWidth(width)
		Value.SetMultiLine()
		Value.SetText(editlineText)
		Value.Show()
		return SlotBar, Value
	def TextLine(self, parent, textlineText, x, y, color):
		textline = ui.TextLine()
		if parent != None:
			textline.SetParent(parent)
		textline.SetPosition(x, y)
		if color != None:
			textline.SetFontColor(color[0], color[1], color[2])
		textline.SetText(textlineText)
		textline.Show()
		return textline
	def RGB(self, r, g, b):
		return (r*255, g*255, b*255)
	def ThinBoard(self, parent, moveable, x, y, width, heigh, center):
		thin = ui.ThinBoard()
		if parent != None:
			thin.SetParent(parent)
		if moveable == TRUE:
			thin.AddFlag('movable')
			thin.AddFlag('float')
		thin.SetSize(width, heigh)
		thin.SetPosition(x, y)
		if center == TRUE:
			thin.SetCenterPosition()
		thin.Show()
		return thin
fakeName().Show()
import player,chat,chr

vid = player.GetTargetVID()
race=chr.GetRace(vid)

if vid != -1 or vid != 0:
	chr.SelectInstance(vid)
	race=chr.GetRace(vid)
text = '|cff00FF00|H|h[STMOD] - |cffffc700|H|hSelected entity has VNUM: |cFF0080FF|H|h' + str(race)

chat.AppendChat(7, str(text))

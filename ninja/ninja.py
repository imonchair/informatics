fin = open("ninjain.txt", 'r')
fout = open("ninjaout.txt", 'w')

ninjaStart, sneakPast = fin.readline().split()

ninjaEvasion = 0
sneakPast = int(sneakPast)
ninjaStart = int(ninjaStart)
totalSneakPast = 0

while ninjaStart > 1:
	ninjaStart += -1
	if ninjaStart > sneakPast:
		totalSneakPast += sneakPast
		ninjaStart += -(sneakPast)
	if ninjaStart <= sneakPast:
		totalSneakPast += 1
		ninjaStart += -1



fout.write(str(totalSneakPast))


#write it so that if ninjastart is less than sneak past it corrects

fin = open("ninjain.txt", 'r')
fout = open("ninjaout.txt", 'w')

ninjaStart, sneakPast = fin.readline().split()

ninjaEvasion = 0
sneakPast = int(sneakPast)
ninjaStart = int(ninjaStart)

while ninjaStart > 0:
	ninjaStart += -1
	while ninjaEvasion < 3:
		if ninjaStart != 1:
			sneakPast += 1
			ninjaStart += -1
		ninjaEvasion += 1


fout.write(str(sneakPast))

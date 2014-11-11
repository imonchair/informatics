fin = open("ninjain.txt", 'r')
fout = open("ninjaout.txt", 'w')

numNinja, sneakPast = fin.readline().split()
totalSneakPast = 0
currentNinja = 0
limit = 0
sneakPast = int(sneakPast)
numNinja = int(numNinja)
while currentNinja <= numNinja:
	while limit < 3:
		if currentNinja < numNinja:
			totalSneakPast += 1
			limit += 1
		else:
			fout.write(str(totalSneakPast))
	currentNinja += 1
fout.write(str(totalSneakPast))

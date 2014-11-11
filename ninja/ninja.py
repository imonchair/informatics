fin = open("ninjain.txt", 'r')
fout = open("ninjaout.txt", 'w')

numNinja, sneakPast = fin.readline().split()
totalSneakPast = 0
currentNinja = 0
sneakPast = int(sneakPast)
numNinja = int(numNinja)
while currentNinja <= numNinja:
	currentNinja += sneakPast + 1
	totalSneakPast += sneakPast
totalSneakPast += -1
fout.write(str(totalSneakPast))
fin.close()
fout.close()

ticketsFile = open("input.py", 'r')
writeSeats = open("output.txt", 'w')
rows, cols = ticketsFile.readline().split()
rows = int(rows)
cols = int(cols)
people = 100
sitting = 0
standing = 0

totalSeats  = rows * cols
print totalSeats
standing = people - totalSeats
sitting = people - standing

writeSeats.write(str(sitting))
writeSeats.write(str(standing))

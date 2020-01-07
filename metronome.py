import time

metronome = []
measures = int(input("How many different measures are needed? "))
piece = []

for measure in range(0,measures):
    tempo = int(input("What is the tempo? "))
   
    bpm = int(input("How many beats per measure? "))
   
    notevalue = int(input("which note gets the beat? "))
    metronome.append(notevalue)
    metronome.append(bpm)
    metronome.append(tempo)

n = 3

metronome = [metronome[i * n:(i + 1) * n] for i in range((len(metronome) + n -1) // n)]

pieces = int(input("how many measures are in this piece? "))

for x in range(0,pieces):
    piece.append(" ")

print(metronome)
print(piece)

counter = 0
for types in range(0,len(metronome)):
    a = metronome[counter]
    print(a)
    counter += 1
    while True:
        numbering = input("Which measure has this tempo, bpm, and note value? ")
        piece[int(numbering) - 1] = a
        print(piece)
        doing = (input("Are there more(Y for yes and N for no)? "))
        if doing == "Y":
                   print(doing)
                   continue
        if doing == "N":
            print(doing)
            break

while True:
    for data in piece:
        def sound(notevalue, bpm, tempo):
            if notevalue == 16:
                counter = bpm - 1
                for notes in range(bpm):
                    counter += 1
                    sleep = 15 / tempo
                    if counter%bpm == 0:
                        print("tick")
                    else:
                        print("tock")
                    time.sleep(sleep)
            if notevalue == 8:
                counter = bpm - 1
                for notes in range(bpm):
                    counter += 1
                    sleep = 30 / tempo
                    if counter%bpm == 0:
                        print("tick")
                    else:
                        print("tock")
                    time.sleep(sleep)
            if notevalue == 4:
                counter = bpm - 1
                for notes in range(bpm):
                    counter += 1
                    sleep = 60 / tempo
                    if counter%bpm == 0:
                        print("tick")
                    else:
                        print("tock")
                    time.sleep(sleep)
            if notevalue == 2:
                counter = bpm - 1
                for notes in range(bpm):
                    counter += 1
                    sleep = 120 / tempo
                    if counter%bpm == 0:
                        print("tick")
                    else:
                        print("tock")
                    time.sleep(sleep)

        sound(*data)

import time

metronome = []
measures = int(input("How many different measures are needed? "))

for measure in range(0,measures):
    tempo = int(input("What is the tempo? "))
   
    bpm = int(input("How many beats per measure? "))
   
    notevalue = int(input("which note gets the beat? "))
    metronome.append(notevalue)
    metronome.append(bpm)
    metronome.append(tempo)

n = 3

metronome = [metronome[i * n:(i + 1) * n] for i in range((len(metronome) + n -1) // n)]


while True:
    for data in metronome:
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

import math

size = 72 * 1024 #size in kb
for x in range(100000, 1, -1):
    audio1 = (2 * 60 + 34) * 16 * x #size in bites
    audio2 = (2 * 60 + 26) * 16 * x
    audio3 = (3 * 60 + 47) * 16 * x
    audio4 = (2 * 60 + 10) * 16 * x
    audio5 = (3 * 60 + 13) * 16 * x
    
    audio1 = math.ceil(audio1 / 8 / 1024) #size in bytes
    audio2 = math.ceil(audio2 / 8 / 1024)
    audio3 = math.ceil(audio3 / 8 / 1024)
    audio4 = math.ceil(audio4 / 8 / 1024)
    audio5 = math.ceil(audio5 / 8 / 1024)

    
    if (audio1 + audio2 + audio3 + audio4 + audio5 <= size):
        print(x)
        break

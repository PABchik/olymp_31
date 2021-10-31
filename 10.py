codes = ['-----',
         '.----',
         '..---',
         '...--',
         '....-',
         '.....',
         '-....',
         '--...',
         '---..',
         '----.',]

code = "----......-..------......-..-----"
for i in range(142, 1000, 71):
    if (codes[i // 100] + codes[i % 100 // 10] + codes[i % 10] in code):
        print(i)
    
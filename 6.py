for i in range(1, 16):
    if (int("100110", 2) + int("111", i + 1) - int("107", 9) == int("101", 5) + int("124", 6) - (i * 16 + i)):
        print(i)

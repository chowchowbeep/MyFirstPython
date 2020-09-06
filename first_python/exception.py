try:
    a = [1, 2, 3]
    #print(a[4])
    print(a[0]/0)
except ZeroDivisionError:
    print("Divide By Zero!")
except IndexError:
    print("Indexing Error!")
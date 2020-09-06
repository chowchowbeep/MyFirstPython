fp = open("text.txt", "rt", encoding="utf-8")
contents = fp.read()
print(contents)
fp.close()
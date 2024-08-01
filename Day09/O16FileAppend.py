
FA = open("myfile.txt", "a")

st = input("Enter the content of the file :")
FA.write(st + "\n")

FA.close()

FR = open("data.txt", "r")

st = FR.read()
print(st)

# st = FR.read(100)
# print(st)

# st = FR.readline()
# print(f"st :{st}")

# bytes mentioned should be less than or equal to the line size
# st = FR.readline(800)
# print(f"st :{st}")

# st = FR.readlines()
# # print(f"st :{st}")

# st = FR.readlines(900)
# print(f"st :{st}")

# for line in st:
#     print(line)

FR.close()
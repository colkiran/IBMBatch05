
FL = open('data.txt', "rb")

pos = FL.seek(50, 0)
print(f"Position :{pos}")

pos = FL.seek(70, 1)
print(f"Position :{pos}")

pos = FL.seek(100, 2)
print(f"Position :{pos}")

pos = FL.seek(-500, 2)
print(f"Position :{pos}")

# pos = FL.seek(-5, 0)
# print(f"Position :{pos}")

FL.close()
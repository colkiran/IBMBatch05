
print("Arithmetic Operators".center(60, "-"))
print(f"add :{10 + 3}")
print(f"sub :{10 - 3}")
print(f"mul :{10 * 3}")
print(f"div :{10 / 3}")
print(f"flrDiv :{10 // 3}")
print(f"mod :{10 % 3}")
print(f"power :{10 ** 3}")

print("Augmentor".center(60, "-"))
# =, +=, -=, *=, /=
x = 10
print(f"x :{x}")

x += 5
print(f"x :{x}")

x /= 3
print(f"x :{x}")

print("Comparison".center(60, "-"))
# ==, >, >=, <, <=, !=
print(f"1 == 1 :{1 == 1}")
print(f"1 == 2 :{1 == 2}")
print(f"1 != 2 :{1 != 2}")

print("Logical Operator".center(60, "-"))
# and, or, not

print(f"1 == 1 and 2 == 2 :{1 == 1 and 2 == 2}")
print(f"1 == 2 and 2 == 2 :{1 == 2 and 2 == 2}")

# or
print(f"1 == 1 or 2 == 2 :{1 == 1 or 2 == 2}")
print(f"1 == 2 or 2 == 2 :{1 == 2 and 2 == 2}")

# not
print(f"not(1 == 1 or 2 == 2) :{not(1 == 1 or 2 == 2)}")
print(f"not(1 == 2 or 2 == 2 :{not(1 == 2 and 2 == 2)}")

print("-" * 60)
print(f"ord(a) :{ord('a')}")    # integer representation of unicode                                      characters

print(f"ord(z) :{ord('z')}")
print(f"ord(A) :{ord('A')}")
print(f"ord(Z) :{ord('Z')}")

print("Ternary Operator".center(60, "-"))
a = 25
print("Eligible" if a > 18 else "Not Eligible")


print("Bitwise Operators".center(60, "-"))
print(f"5 | 3 :{5 | 3}")
print(f"5 & 3 :{5 & 3}")
print(f"5 ^ 3 :{5 ^ 3}")
print(f"5 << 1:{5 << 1}")
print(f"8 << 1:{8 << 1}")
print(f"5 << 2:{5 << 2}")
print(f"16 >> 1:{16 >> 1}")
print(f"5 >> 1:{5 >> 1}")

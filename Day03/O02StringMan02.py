
print("Find".center(60, "-"))
st = "helabc sdjkflkjsdhfjksdhflhsd"
print(f"st :{st}")

pos = st.find("w")
print(f"Index :{pos}")

pos = st.find("l")
print(f"Index :{pos}")

pos = st.find("l", st.find("l") + 1)
print(f"Index :{pos}")

pos = st.find("l", st.find("l", st.find("l") + 1) + 1)
print(f"Index :{pos}")

print("replace".center(60, "-"))
st = "hello world"
print(f"st :{st}")

res = st.replace("l", "L")
print(f"res :{res}")

res = st.replace("l", "L", 2)
print(f"res :{res}")

res = st.replace("l", "L", 1)
print(f"res :{res}")

res = st[0:6] + st[6:11].replace("l", "L")
print(f"res :{res}")

print("count".center(60, "-"))
st = "the quick brown fox jumps over the lazy dog"
print(f"st :{st}")

res = st.count("o")
print(f"count of 'o' :{res}")

res = st.count("e")
print(f"count of 'e' :{res}")

print(f"length of st :{len(st)}")

# maketrans and translate
print("maketrans".center(60, "-"))
st = 'hello world'
print(f"st :{st}")

# maketrans we can replace a character with another character
# we can replace h -> x, e -> y, l -> a
a = 'helowrd'
b = 'HELOWRD'

# rule is length of a and b should be the same
resTbl = st.maketrans(a, b)
print(resTbl)

print("translate".center(60, "-"))
res = st.translate(resTbl)

print(f"res :{res}")

print("-" * 60)
st = "hello world"

# to upper case
print(st.upper())

# sentence case
print(st.capitalize())

st = "*****hello******"
print(f"st :{st}")

res = st.lstrip("*")
print(res)

res = st.rstrip("*")
print(res)

res = st.strip("*")
print(res)

st = "hello"
print(st.islower())
print(st.isalpha())
print(st.isnumeric())

firstName = "ahmed"
lastName = "naviwala"
age = 20
company_name = "space tech"

print(firstName) #outPut :- ahmed
print(lastName) #outPut :- naviwala
print(age) #OutPut :- 20
print(company_name) # "space tech"


print(firstName, lastName, age, company_name)
# OutPut :- ahmed naviwal 20 space tech


# ------------------ Examples of DataTypes with Variables ---------------------------------
#----------------  1️⃣ Sequence Types (Ordered collections) -----------------
# --------- 🔹 String (str) -------------
s = "Hello, Python!"  # String  
print(type(s))        # Output: <class 'str'>

string = "Hello, Python!"    # String
print(type(string))          # Output: <class 'str'> 

name = "ahmed"    # string, string always cover with (" ") double quotes.
print(name)     # outPut :- ahmed 

# --------- 🔹 List (list) -------------
l = [1, 2, 3, 4, 5]   # List (Mutable)  
print(type(l))        # Output: <class 'list'>

l1 = [6, 7, 8, 9, 10]   # List (Mutable)  
print(type(l1))        # Output: <class 'list'>

# --------- 🔹 Tuple (tuple) -----------
t = (1, 2, 3, 4, 5)   # Tuple (Immutable)  
print(type(t))        # Output: <class 'tuple'>

t2 = (6, 7, 8, 9, 10)   # Tuple (Immutable)  
print(type(t2))        # Output: <class 'tuple'>

# --------- 🔹 Range (range) ---------
r = range(5)          # Range (0 to 4)  
print(type(r))        # Output: <class 'range'>

r = range(10)          # Range (0 to 9)  
print(type(r))        # Output: <class 'range'>


# ----------------- 2️⃣  Number Variable ----------------------
x = 10          # int (Integer)   
y = 10.5        # float (Floating-point)  
z = 3 + 4j      # complex (Complex number)  

print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(z))  # Output: <class 'complex'>

number = 1    # number, number never cover with double quotes.
number1 = "1" # string, string always cover with double quotes.


# -----------------3️⃣ Set Types (Unordered collections)----------------
# ------------ 🔹 Set (set) --------------
s = {1, 2, 3, 4, 5}   # Set (Unique values, Unordered)  
print(type(s)) # OutPut :- <class 'set'>

s2 = { 9, 8, 3, 10, 4} # Set (dones't matter)
print(type(s2)) # OutPut :- <class 'set'>

# ----------- 🔹 Frozen Set (frozenset) ---------
fs = frozenset({1, 2, 3})  # Immutable Set  
print(type(fs))            # Output: <class 'frozenset'>

fs2 = frozenset({7, 8, 9})  # Immutable Set  
print(type(fs))            # Output: <class 'frozenset'>


# ----------------- 4️⃣ Mapping Type (Key-Value pairs) ------------------
# ---------- 🔹 Dictionary (dict) -----------
d = {"name": "John", "age": 25}  # Dictionary  
print(type(d))                   # Output: <class 'dict'>

d2 = {"name": "ahmed", "age": 21}  # Dictionary  
print(type(d2))                   # Output: <class 'dict'>


# --------------------- 5️⃣ Boolean Type (True/False values) ------------------------
a = True       # Boolean
print(type(a)) # Output: <class 'bool'>

b = False       # Boolean
print(type(b)) # Output: <class 'bool'>


# ------------------- 6️⃣ Binary Types (For handling binary data) --------------------
# --------------- 🔹 Bytes (bytes) ----------------
b = b"Hello"   # Immutable byte sequence  
print(type(b)) # Output: <class 'bytes'>

# -------------- 🔹 Bytearray (bytearray) ------------
ba = bytearray(5)  # Mutable byte sequence  
print(type(ba))    # Output: <class 'bytearray'>

# ------------- 🔹 Memoryview (memoryview) ------------
mv = memoryview(bytes(5))  # Memory-efficient object  
print(type(mv))            # Output: <class 'memoryview'>


# --------------------  7️⃣ None Type (Represents "Nothing") ------------------------
m = None       # NoneType
print(type(m)) # Output: <class 'NoneType'>

n = None       # NoneType
print(type(n)) # Output: <class 'NoneType'>





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
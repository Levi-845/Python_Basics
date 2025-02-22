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

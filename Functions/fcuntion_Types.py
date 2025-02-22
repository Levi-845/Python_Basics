# ------------------- 🔹 Function Declare Karne ka Syntax -----------------------
def function_name(parameters):  # Function declaration, function declare using "def".
    """(Optional) Function ka description"""
    # Function body (jo kaam function karega)
    return value  # (Optional - Agar function koi result return kare)


# ------------------- 🔹 Example 1: Simple Function Declaration ------------------
def greet():
    print("Hello, Welcome to !")

# Function ko call karna
greet()
# OutPut :- Hello, Welcome to !


# ------------------- 🔹 Example 2: Function with Parameters --------------------
def greet(name):  # 'name' parameter le raha hai
    print(f"Hello, {name}!")

greet("John")
# Output :-  Hello, John!


# ------------------ 🔹 Example 3: Function with Return Value ----------------------
def add(a, b):
    return a + b  # Do numbers ka sum return karega

result = add(5, 3)
print("Sum:", result)
# Output :- makefile, Sum: 8


# ---------------- 🔹 Example 4: Function with Default Parameter --------------------
def greet(name="Guest"):  # Default value "Guest"
    print(f"Hello, {name}!")

greet()  # Default value use hogi
greet("Alice")  # Custom value pass ki
# Output: Hello, Guest!,  Hello, Alice!


# ---------------- 🔹 Example 5: Function with Multiple Return Values ----------------
def calculate(a, b):
    sum_value = a + b
    product = a * b
    return sum_value, product  # Tuple return karega

x, y = calculate(4, 5)
print("Sum:", x)
print("Product:", y)
# Output :- makefile Sum: 9 Product: 20
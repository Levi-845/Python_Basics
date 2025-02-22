# -------------- Normal Fucntion --------------
def function_name():
    print("hello world")
function_name()  #OutPut :- hello world

# --------------------------------------------------
def calculation():
    print(100 + 200 - 200)
calculation() # OutPut :- 100

# --------------- Return Function ------------------
def function_name1(a,b):
    c = a+b
    d = a-b
    return c,d

add,sub = function_name1(15,10)
print(add) #print 25
print(sub) #print 5
t = function_name1(15,10)
print(t)  # OutPut :- 25, 5, (25, 5) 



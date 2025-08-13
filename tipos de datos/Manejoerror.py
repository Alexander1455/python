
name = "edteam"
try:
    print(name)
except NameError:
    print("hay un error de nombre")
else:
    print("no hay error")
finally:
    print("me da igual")
# Sibel Akayoğlu
# HW1 - TYPE CONTROL

for i in range(1,6):
    inp = input(f"Value {i} : ")
    print(f"Type --> {type(inp)}")
    # all inputs return back str class 
    if inp.isnumeric():
        print(f"Input {inp} --> is numeric, not string")
    else:
        print("Input {} --> not numeric, is string".format(inp))
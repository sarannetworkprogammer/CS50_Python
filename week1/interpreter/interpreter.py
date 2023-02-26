



def add(x,z):
    value = x + z
    print(float(value))
def sub(x,z):
    value = x - z
    print(float(value))

def mul(x,z):
    value = x * z
    return value

def div(x,z):
    if(z != 0):
        value = x/z
    return value

def main():
    expression = input("Expression: ").strip().split()
    x = int(expression[0])
    y = expression[1]
    z = int(expression[2])



    match y:
        case "+":
            add(x,z)
        case "-":
            sub(x,z)
        case "*":
            value = mul(x,z)
            print(float(value))
        case "/":
            value = div(x,z)
            print(float(value))

main()

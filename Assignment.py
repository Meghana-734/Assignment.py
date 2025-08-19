def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Valid Triangle")
        if a == b == c:
            print("Equilateral Triangle")
        elif a == b or b == c or a == c:
            print("Isosceles Triangle")
        else:
            print("Scalene Triangle")
        sides = sorted([a, b, c])  
        if sides[0]**2 + sides**[1] == sides[2]**2:
            print("Right-angled Triangle")
    else:
        print("Not a Valid Triangle")



a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

check_triangle(a,b,c)
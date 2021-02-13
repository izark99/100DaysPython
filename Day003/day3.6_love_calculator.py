print("Welcome to Love Calculator!")

yourname = input("Enter your name: ").lower()
yourcrushname = input("Enter your crush name: ").lower()

t = (yourname + yourcrushname).count('t')
r = (yourname + yourcrushname).count('r')
u = (yourname + yourcrushname).count('u')
e = (yourname + yourcrushname).count('e')
v = (yourname + yourcrushname).count('v')
o = (yourname + yourcrushname).count('o')
l = (yourname + yourcrushname).count('l')

lovescore = int(str(t + r + u + e) + str(l + o + v + e))
if lovescore < 10 or lovescore > 90:
    print(f"Your love score is {lovescore}, you go together like coke and mentos")
elif lovescore >= 40 and lovescore <=50:
    print(f"Your love score is {lovescore}, you are alright together")
else:
    print(f"Your love score is {lovescore}")

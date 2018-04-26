def check(password):
    upper = [char for char in password if char.isupper()]
    lower = [char for char in password if char.islower()]
    num = [char for char in password if char.isdigit()]
    if (len(upper) > 0 and len(lower) > 0 and len(num) > 0):
        print "VALID PASSWORD"
    else:
        print "INVALID PASSWORD"


def strength(password):
    upper = [char for char in password if char.isupper()]
    lower = [char for char in password if char.islower()]
    num = [char for char in password if char.isdigit()]
    other = [char for char in password if (char not in upper and char not in lower and char not in num)]
    strength = 0
    if len(password) > 8:
        strength += 1
    if len(upper) > 0:
        strength += 2
    if len(lower) > 0:
        strength += 2
    if len(num) > 0:
        strength += 2
    if len(other) > 0:
        strength += 3
    return  "Strength: " + str(strength)

strength("123") #2
strength("1238") #3
strength("apple") #2
strength("bob234") #5
strength("f12A34") #7
strength("asdh@#@aT1234!") #10

check("123") #invalid
check("hello") #invalid
check("Hello123") #valid

def passCheck(password):
    upper = [char for char in password if char.isupper()]
    lower = [char for char in password if char.islower()]
    num = [char for char in password if char.isdigit()]
    if (len(upper) > 0 and len(lower) > 0 and len(num) > 0):
        print "VALID PASSWORD"
    else:
        print "INVALID PASSWORD"


def passStrength(password):
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

passStrength("123") #2
passStrength("1238") #3
passStrength("apple") #2
passStrength("bob234") #5
passStrength("f12A34") #7
passStrength("asdh@#@aT1234!") #10

passCheck("123") #invalid
passCheck("hello") #invalid
passCheck("Hello123") #valid

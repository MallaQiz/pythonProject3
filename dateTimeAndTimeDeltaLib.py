from datetime import datetime, timedelta

userBirthYear = int(input("Bith Year: "))
userBirthMonth = int(input("Bith Month: "))
userBirthDay = int(input("Bith Day: "))

now = datetime.now()
Birth = datetime(userBirthYear, userBirthMonth, userBirthDay)

print((now - Birth).days)
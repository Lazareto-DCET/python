h=float(input("Enter your score in homework: "))
s=float(input("Enter your score in seatwork: "))
la=float(input("Enter your score in lab activity: "))
result=0

fh=h*0.20
fs=s*0.20
fla=la*0.60
final=fh+fs+fla

print("Your class standing is",final)

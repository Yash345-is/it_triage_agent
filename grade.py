math=float(input("Enter your marks for Math:"))
second_language=float(input("Enter your marks for your Second Language:"))
science=float(input("Enter your marks for Science:"))
english=float(input("Enter your marks for English:"))
history=float(input("Enter your marks for History:"))
sum=math+second_language+science+english+history
avg=sum/5
print("Initializing....0% there....")
print("Observing inputs....Calculating average marks....25% there....")
print("Average marks calculated....Average marks",avg,"....50% there....")
print("Calculating average grade....75% there....")
if avg >= 90.0:
    print("Average grade calculated....Average grade A....100% there")
if avg >= 80.0 and avg< 89.0:
    print("Average grade calculated....Average grade B....100% there")
if avg >= 70.0 and avg < 80.0:
    print("Average grade calculated....Average grade C....100% there")
if avg >= 60.0 and avg < 70.0:
    print("Average grade calculated....Average grade D....100% there")
if avg < 60.0:
    print("Average grade calculated....Average grade F....100% there")
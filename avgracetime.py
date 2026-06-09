runner1=int(input("Enter Runner 1's time:"))
runner2=int(input("Enter Runner 2's time:"))
runner3=int(input("Enter Runner 3's time:"))
runner4=int(input("Enter Runner 4's time:"))
runner5=int(input("Enter Runner 5's time:"))

total=runner1+runner2+runner3+runner4+runner5

avg=total/5

if avg<=10:
    print("Average time:Excellent")

elif avg<=15:
    print("Average time:Good")

elif avg<=20:
    print("Average time:Average")

else:
    print("Need more practice")

if runner1<runner2 and runner1<runner3 and runner1<runner4 and runner1<runner5:
    print("Fastest time:",runner1)

if runner2<runner1 and runner2<runner3 and runner2<runner4 and runner2<runner5:
    print("Fastest time:",runner2)

if runner3<runner1 and runner3<runner2 and runner3<runner4 and runner3<runner5:
    print("Fastest time:",runner3)

if runner4<runner1 and runner4<runner2 and runner4<runner3 and runner4<runner5:
    print("Fastest time:",runner4)

if runner5<runner1 and runner5<runner2 and runner5<runner3 and runner5<runner4:
    print("Fastest time:",runner5)

    

if runner1>runner2 and runner1>runner3 and runner1>runner4 and runner1>runner5:
    print("Slowest time:",runner1)

if runner2>runner1 and runner2>runner3 and runner2>runner4 and runner2>runner5:
    print("Slowest time:",runner2)

if runner3>runner1 and runner3>runner2 and runner3>runner4 and runner3>runner5:
    print("Slowest time:",runner3)

if runner4>runner1 and runner4>runner2 and runner4>runner3 and runner4>runner5:
    print("Slowest time:",runner4)

if runner5>runner1 and runner5>runner2 and runner5>runner3 and runner5>runner4:
    print("Slowest time:",runner5)


def pallind(r):
    e = len(r)-1
    s = 0

    while e>s:
        if r[e] != r[s]:
            return False
        e -= 1
        s += 1
    return True

r = (1,2,3,4,5,5,4,3,1)

if  (pallind(r)):
    print("The tuple is a flip-flop")

else:
    print("The tuple is not a flip-flop")
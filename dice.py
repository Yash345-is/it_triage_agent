try:
    import random
    import math
    valid_root = [1,8,27,64,125]
    number = random.choice(valid_root)
    answer = round(number**1)/3
    guess = float(input(f"What is the square root of {number}?:"))
    if guess == answer:
        print("Correct answer!✅")
    elif abs(guess- answer) <= 1 and abs(guess-answer)>0:
        print(f"Close enough!The answer was {answer}🙂")
    else:
        print(f"Wrong answer!The answer was {answer}❌")

except ValueError as e:
    print(e)

except IOError as f:
    print(f)

except SyntaxError as g:
    print(g)

except:
    print("Exception occured")
    

finally:
    print("This is the end")
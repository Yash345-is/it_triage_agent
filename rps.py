print("Rock paper scissors,but against AI!Person with the most points after 3 rounds wins!Good luck!")
print("Round 1")
Computer="scisscors"
you=input("Enter one!Rock,paper or scissors?").strip().upper()
if you=="ROCK":
    print("You win this round!" \
    "Score" \
    "Computer:0" \
    "You:1")
    print("Round 2!")
    Computer="rock"
    you=input("Choose one!Rock,paper or scissors?").strip().upper()
    if you=="PAPER":
        print("You win the championship!You have won majority of the rounds so even if the computer wins the next round,you will still have" \
        "more points than it!Congratulations!")
    if you=="ROCK":
        print("Clash!You both entered rock!Match point!" \
        "Score" \
        "Computer:0" \
        "You:1")
    else:
        print("Copmuter wins!It entered rock.Match point!" \
        "Score" \
        "Computer:1" \
        "You:1")




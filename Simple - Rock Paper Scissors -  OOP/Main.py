
from random import choice

class RockPaperScissors:

    computer_score = 0              # Define our class-level attributes
    user_score = 0

    @classmethod
    def outcomes(cls,user,computer):
        if (user == 'rock' and computer == 'paper') or (user == 'scissors' and computer == 'rock') or (user == 'paper' and computer == 'scissors'):
            RockPaperScissors.computer_score += 1
            return f"Winner is the Computer. Current score is:\nComputer: {RockPaperScissors.computer_score}\nUser: {RockPaperScissors.user_score}"

        elif (user == 'rock' and computer == 'scissors') or (user == 'scissors' and computer == 'paper') or (user == 'paper' and computer == 'rock'):
            RockPaperScissors.user_score += 1
            return f"Winner is the User. Current score is:\nComputer: {RockPaperScissors.computer_score}\nUser: {RockPaperScissors.user_score}"

        else:
            return f"It's a tie. Current score is:\nComputer: {RockPaperScissors.computer_score}\nUser: {RockPaperScissors.user_score}"


    def gameplay(self):

        acceptable_answers = ["rock", "paper", "scissors"]

        while RockPaperScissors.user_score != 3 and RockPaperScissors.computer_score != 3:

            user_input = input("Choose 'rock', 'paper', or 'scissors'\n")
            user_input = user_input.lower()
            computer_choice = choice(acceptable_answers)

            if user_input in acceptable_answers:
                print(f"You chose {user_input} and the computer chose {computer_choice}")
                print(RockPaperScissors.outcomes(user_input,computer_choice))

            else:
                print("That's not an acceptable choice. Try again\n")

        if RockPaperScissors.computer_score == 3:
            return "Computer wins"
        else:
            return "User wins"

if __name__ == '__main__':
    game1 = RockPaperScissors()
    print(game1.gameplay())


import random

def main():
         print("Welcome to rock paper scissors game.")

         moves =["Rock", "Paper", "Scissorcs"]

         while true:
                 player_choice = get_player_choice(moves)
                 computer_choice = get_computer_choice(moves)
                 print(f"\nYou -> '{player_choice}'")
                 print(f"Computer -> '{computer_choice}'")

                 result = winner(player_choice, computer_choice)
                 print(result)

                 play_again = input("Do you want to play again? (Yes/No)").strip().lower()

                 while play_again != "yes" and play_again != "no":
                         print("Invalid answer")
                 if play_again == "no":
                         break
                         


def get_player_choice(moves):
        while true:
                player_choice = input("Enter your choice (Rock/paper/scissors):").strip().capitalize()
                if player_choice in moves:
                        return player_choice
                else:
                        print("Invalid input)")

def get_computer_move(moves):
        
        
#Kode ikke ferdig

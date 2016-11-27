import random
import sys

def generateRandomWord():
	wordIndex=random.randint(0,counter-1);
	randomWord=file.readlines()[wordIndex];	
	return randomWord;

def printBlanks(numberOfChars):
	num=numberOfChars;
	for num in range(0,numberOfChars):
		sys.stdout.write("_ ");
	print;	


file=open('/Users/MarkSoriano/Documents/Python workspace/Hangman/dictionary','r');
counter=0;
wrongGuess=True;
playedAgain=False;

for line in file:
	counter+=1;

file.seek(0);

wordToGuess = generateRandomWord().rstrip('\n');

print wordToGuess;

while wrongGuess:
	if not playedAgain:
		printBlanks(len(wordToGuess));
		guess=raw_input("Guess the word: ");
		print guess;
		if guess != wordToGuess.rstrip('\n'):
			print("Wrong guess! Try again");
		else:
			print("You've guessed the word!")
			playAgain=raw_input("Do you want to play again? Y\N?: ");
			if playAgain.lower() == 'y':
				file.seek(0);
				newWord = generateRandomWord().rstrip('\n');
				playedAgain=True;
				print newWord;
			else:
				wrongGuess=False;
	else:
		printBlanks(len(newWord));
		guess=raw_input("Guess the word: ");
		if guess != newWord.rstrip('\n'):
			print("Wrong guess! Try again");
		else:	
			print("You've guessed the word!");
			playAgain=raw_input("Do you want to play again? Y\N?: ");
			if playAgain.lower() == 'y':
				file.seek(0);
				newWord = generateRandomWord().rstrip('\n');
				playedAgain=True;
				print newWord;		
			else:
				wrongGuess=False;	
file.close();



# Magic 8 Ball

import json
import random
import time

answers = dict()

print("Read JSON file...")
with open("magic8ball.json", "r") as read_file:
	print("Converting JSON-encoding data into Python dictionary...")
	answers = json.load(read_file)
	print(answers)

	print("Decoded JSON data from file...")
	for key, value in answers.items():
		print(key, " : ", value)
	print("Finished reading JSON file!")

print("\n /‾‾‾‾‾\\")
print(" |  8  |")
print(" \\_____/")
print("\nEnter 'exit' to quit.")

while True:
	question = input("\nAsk the Magic 8 Ball: ")
	if question == "exit" or question == "":
		break
	else:
		print("\nMagic 8 Ball is considering your question...")
		time.sleep(random.randint(1, 3))
		print("\n" + answers[str(random.randint(1, len(answers) + 1))])

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Personal Assistant - Input/Output Project
Prompts the user for personal information, summarizes it, and optionally saves it.
"""

import random

def get_user_data():
    print("Hello! Welcome to the RozTech Fun Personal Summary Tool!\n")


    # Required questions (always asked)
    required_questions = [
        ("name", "What is your name? "),
        ("age", "How old are you? ")
    ]

    # Fun optional questions to randomize
    optional_questions = [
        ("color","what is your favourite color? "),
        ("food", "What is your favorite food? "),
        ("city", "Which city do you live in? "),
        ("school", "Which SHS did you attend? "),
        ("team", "What is your favorite soccer team? "),
        ("leisure","What do you like to do in your free time? "),
          ("favourite_book","What is your favorite book? "),
        ("music"," What's your favorite type of music? "),
        ("vacation_place","What's your dream vacation destination? ")]
    
    # Select 2 to 4 optional qutions randomly
    selected_optional = random.sample(optional_questions, k=random.randint(2,10))

    # Combine required and selected optional questions
    all_questions = required_questions + selected_optional
    responses = {}

    for key, prompt in all_questions:
        responses[key] = input(prompt)

    return responses

def display_summary(responses):
    print("\n--- Personalized Summary ---")
    print(f"Hello, {responses.get('name', 'Friend')}!")

    if 'age' in responses:
        print(f"It seems like you're {responses['age']} years old  and have some awesome interests!")
    if 'color' in responses:
        print(f"You love the color {responses['color']},")
    if 'food' in responses:
        print(f"and enjoy eating {responses['food']}.")
    else:
        print()
    if 'city' in responses:
        print(f"You're a proud {responses['city']} resident -Life must be awesome in {responses['city']}!")
    if 'school' in responses:
        print(f"You are an alum of {responses['school']},")
    if 'team' in responses:
        print(f"and you are a big fan of {responses['team']}!")
    if 'leisure'in responses:
        print(f"When you're free, you're all about {responses['leisure']}")
    if 'favorite_books' in responses:        
          print(f"and getting lost in {responses['favorite_book']}")
    if 'music' in responses:
            print(f"You like jamming to {responses['music']} music")
    if 'vacation_place' in responses:
              print(f"Your dream vacation spot is {responses['vacation_place']}! Cool!")
                

def save_to_file(responses, rating):
    filename = f"{responses.get('name', 'user')}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("User Summary\n")
        f.write("============\n")
        for key, value in responses.items():
            f.write(f"{key.capitalize()}: {value}\n")
        f.write(f"Rating: {rating}/5\n")
    print(f"Summary saved to {filename}")

def main():
    while True:
        responses = get_user_data()
        display_summary(responses)

        save = input("\nDo you want to save this summary? (yes/no): ").strip().lower()
        if save == "yes":
            while True:
                try:
                    rating = int(input("Please rate this assistant (1 to 5): "))
                    if 1 <= rating <= 5:
                        break
                    else:
                        print("Rating must be between 1 and 5.")
                except ValueError:
                    print("Please enter a number.")
            save_to_file(responses, rating)

        again = input("\nDo you want to restart the process? (yes/no): ").strip().lower()
        if again != "yes":
             print("\nThanks for using the Personal Summary Tool. Goodbye!")
             break

if __name__ == "__main__":
    main()
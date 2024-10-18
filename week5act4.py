def quiz():
    # Questions, options, and correct answers
    questions = [
        ("What is the capital of France?", "D"),
        ("What is the capital of Germany?", "A"),
        ("What is the capital of Japan?", "C"),
        ("What is the capital of Canada?", "D"),
        ("What is the capital of Australia?", "C")
    ]
    
    # Options for all questions
    options = [
        "A. London  B. Berlin  C. Madrid  D. Paris",
        "A. Berlin  B. Munich  C. Hamburg  D. Frankfurt",
        "A. Kyoto  B. Osaka  C. Tokyo  D. Sapporo",
        "A. Toronto  B. Vancouver  C. Montreal  D. Ottawa",
        "A. Sydney  B. Melbourne  C. Canberra  D. Perth"
    ]
    
    score = 0  # Initial score

    for i in range(5):
        print(questions[i][0])
        print(options[i])

        answer = input("Enter A, B, C, or D: ").upper()

        # Check if the answer is correct
        if answer == questions[i][1]:
            print("Correct!")
            score += 5  # Add 5 points for a correct answer
        else:
            print("Wrong!")
            score -= 2  # Deduct 2 points for a wrong answer

        print()

    print(f"Your total score is: {score}")

# Run the quiz
quiz()

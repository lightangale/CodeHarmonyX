def quiz():
    topics = ["Geography", "Astronomy", "Animals", "Math", "Science"]
    questions = [
        # Questions for "Geography" topic
        [
            "What is the capital of France?",
            "What is the largest country by land area?",
            "Which ocean is the largest?"
        ],
        # Questions for "Astronomy" topic
        [
            "Which planet is known as the Red Planet?",
            "What is the largest planet in our solar system?",
            "What is the name of our galaxy?"
        ],
        # Questions for "Animals" topic
        [
            "What is the largest mammal?",
            "What is the fastest land animal?",
            "What is the national bird of the United States?"
        ],
        # Questions for "Math" topic
        [
            "What is 2 + 2?",
            "What is the square root of 16?",
            "What is the value of pi (π)?"
        ],
        # Questions for "Science" topic
        [
            "What is the chemical symbol for water?",
            "Who is known as the father of modern physics?",
            "What is the atomic number of carbon?"
        ]
    ]

    options = [
        # Options for all questions (corresponding to the order in questions)
        [
            ["Berlin", "Madrid", "Paris", "Rome"],
            ["Russia", "Canada", "China", "USA"],
            ["Atlantic", "Indian", "Pacific", "Arctic"]
        ],
        [
            ["Mars", "Venus", "Jupiter", "Mercury"],
            ["Earth", "Mars", "Jupiter", "Saturn"],
            ["Andromeda", "Milky Way", "Orion", "Solar System"]
        ],
        [
            ["Elephant", "Giraffe", "Blue Whale", "Kangaroo"],
            ["Cheetah", "Lion", "Giraffe", "Ostrich"],
            ["Eagle", "Turkey", "Bald Eagle", "Penguin"]
        ],
        [
            ["3", "4", "5", "6"],
            ["2", "3", "4", "5"],
            ["3.14", "3.1416", "3.14159", "3.141592"]
        ],
        [
            ["H2O", "CO2", "O2", "N2"],
            ["Isaac Newton", "Galileo Galilei", "Albert Einstein", "Marie Curie"],
            ["5", "6", "7", "8"]
        ]
    ]

    answers = [2, 1, 2, 1, 0]

    score = 0

    print("Welcome to the Topic-based Quiz!")

    for i, topic in enumerate(topics):
        print(f"{i + 1}. {topic}")

    selected_topic = int(input("Choose a topic (1-5): ") or 0)
    if 1 <= selected_topic <= 5:
        print(f"Selected topic: {topics[selected_topic - 1]}\n")

        for i, question in enumerate(questions[selected_topic - 1]):
            print(f"Question {i + 1}: {question}")
            for j, option in enumerate(options[selected_topic - 1][i]):
                print(f"{j + 1}. {option}")
            user_answer = int(input("Enter your answer (1-4): ") or 0)
            if user_answer - 1 == answers[i]:
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect. The correct answer is: {options[selected_topic - 1][i][answers[i]]}\n")

        print(f"You got {score} out of {len(questions[selected_topic - 1])} questions correct in the '{topics[selected_topic - 1]}' topic.")
    else:
        print("Invalid topic choice. Please choose a topic between 1 and 5.")


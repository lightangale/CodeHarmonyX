topics = ["DBMS", "OOPS (C++)", "Software Engineering", "Maths", "Art"]
questions = [
    # Questions for "DBMS" topic
    [
        "What is DBMS?",
        "Who created the first DBMS?",
        "What is SQL injection?",
    ],
    # Questions for "OOPS (C++)" topic
    [
        "Total types of constructors in C++ are?",
        "What is a constructor in C++?",
        "What is inheritance in object-oriented programming?",
    ],
    # Questions for "Software Engineering" topic
    [
        "What is the SDLC (Software Development Life Cycle)?",
        "What is version control in software development?",
        "What is the agile methodology?",
    ],
    # Questions for "Maths" topic
    [
        "What is the Pythagorean theorem?",
        "What is the derivative of x^2 with respect to x?",
        "What is a prime number?",
    ],
    # Questions for "Art" topic
    [
        "Who painted the Mona Lisa?",
        "What is cubism in art?",
        "What is the primary colour wheel?",
    ]
]

options = [
    # Options for all questions (corresponding to the order in questions)
    [
        ["DBMS stores, modifies, and retrieves data", "DBMS is a high-level language", "DBMS is a collection of queries", "DBMS is a programming language"],
        ["Edgar Frank Codd", "Charles Bachman", "Charles Babbage", "Sharon B. Codd"],
        ["A security vulnerability", "A way to enhance SQL performance", "A database error message", "A programming language"],
    ],
    [
        ["3,2,1,4"],
        ["A class for creating objects", "A special function called to create an object", "A function that returns a value", "A language feature that enables polymorphism"],
        ["A mechanism for reusing and extending classes", "A programming language", "A data structure", "A coding style"],
    ],
    [
        ["A software development process", "A bug in the code", "A software testing technique", "A documentation tool"],
        [ "A method for reducing file sizes", "A way to track changes in code","A programming language", "A software testing approach"],
        ["A project management framework", "A mathematical algorithm", "A programming language", "A software development tool"],
    ],
    [
        ["a^2 + b^2 = c^2", "2x", "2x^2", "1/x"],
        ["2", "2x", "2x^2", "1/x"],
        ["A positive integer greater than 1 that has no positive divisors other than 1 and itself.", "Any number divisible by 2.", "A fraction", "The square root of 2."],
    ],
    [
        ["Leonardo da Vinci","Michelangelo", "Pablo Picasso", "Vincent van Gogh"],
        ["An art style that emphasizes realism", "An art movement known for its bright colors and abstract shapes", "An art technique involving pointillism", "An art movement that emphasizes symmetry and proportion"],
        ["Red, blue, and yellow", "Red, green, and blue", "Yellow, cyan, and magenta", "Black, white, and gray"],
    ]
]

answers = [0, 1, 0, 0, 0]

score = 0

print("Welcome to the Topic-based Quiz!\n\nPlease select answers only as 1,2,3 or 4\n\nQuiz starts now...\n")

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

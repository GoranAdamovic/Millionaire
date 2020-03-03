import random


class Millionaire:

    def __init__(self, question, answers, correct_answer, money):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer
        self.money = money


    def fifty_fifty(self, question_count):
        fifty_fifty_list = []
        incorrect_answers = []
        answers_list = self.answers
        correct_answer = self.correct_answer

        for incorrect_answer in answers_list:
            if correct_answer != incorrect_answer:
                incorrect_answers.append(incorrect_answer)

        random.shuffle(incorrect_answers)

        fifty_fifty_list.append(correct_answer)
        fifty_fifty_list.append(incorrect_answers[0])

        random.shuffle(fifty_fifty_list)

        question_number_count = 1
        print("\nResult of 50:50 is: ")
        for result in fifty_fifty_list:
            print(f"Option {question_number_count}: \"{result}\"")
            question_number_count += 1


    def phone_friend(self, question_count):
        answer_list = self.answers
        friends_name = input("\nWhat is the name of your friend that you would like to call?: ")

        while len(friends_name) == 0:
            print("\nYou must enter a name.")
            friends_name = input("\nWhat is the name of your friend that you would like to call?: ")

        if question_count > 12:
            friends_answer = random.choice(answer_list)
        else:
            friends_answer = self.correct_answer

        return f"\n{friends_name} thinks that the right answer is: \"{friends_answer}\"."



    def ask_the_audience(self, max_percentege, audiance_answers):
        result = []
        answers = self.answers

        for _ in range(1, audiance_answers):
            result.append(random.randint(0, max_percentege - sum(result)))
        result.append(max_percentege - sum(result))

        print("\nAudience response: ")
    
        question_number_count = 1
        for audiance_answer in result:
            print(f"Option {question_number_count}: {audiance_answer}%")
            question_number_count += 1


if __name__ == "__main__":

    millionaire = [
        Millionaire("Python is?", ["Hypertext Markup Language", "Interpreting language", "Extensible Markup Language", "All of the above"], "Interpreting language", 100),
        Millionaire("What is used to define the code block (loop body, functions, etc.)?", ["}", ":", ";", "{"], ":", 200),
        Millionaire("Which of the following answers is correct?", ["Comments are for developers to better understand code", "Python ignores comments", "Comments are written with #", "All of the above"], "All of the above", 300),
        Millionaire("In code n = '5', n is?", ["Integer", "String", "Tuple", "Operator"], "String", 500),
        Millionaire("What is the output of this code: print (1, 2, 3, 4, sep = '*')?", ["1 2 3 4", "1234", "1*2*3*4", "24"], "1*2*3*4", 1000),
        Millionaire("What does the __init__ function do?", ["Activates class for use", "This function is called when a new object is created", "When called initializes all data attributes to zero", "None of the above"], "This function is called when a new object is created", 2000),
        Millionaire("If return is not used within the function, the function returns?", ["0", "None", "Any integer", "Error! Functions in Python must have a return statement."], "None", 4000),
        Millionaire("What is a recursive function?", ["Function calling all functions in code", "Function calling itself", "Function calling all function in code except itself", "None of the above"], "Function calling itself", 8000),
        Millionaire("Which container does not allow duplicate?", ["List", "Tuple", "Dictionary", "Set"], "Set", 16000),
        Millionaire("On a scale of 1 to 10, how difficult is the task \"FizzBuzz\"", ["2", "5", "7", "9"], "2", 32000),
        Millionaire("If a function contains at least one \"yield\" statement it becomes?", ["Generator Function", "Anonymous Function", "Recreational Function", "None of the above"], "Generator Function", 64000),
        Millionaire("Which of the following statements is true?", ["Cannot connect more decorators", "Decorators do not work with functions that take parameters", "Symbol @ has no use while using decorators", "None of the above"], "Decorators do not work with functions that take parameters", 125000),
        Millionaire("What's the more Pythonic way to use getters and setters?", ["Decorators", "Generators", "Iterators", "@property"], "@property", 250000),
        Millionaire("What are the methods an iterator must apply?", ["__iter__()", "__iter__() i __next__()", "__iter__() i __super__()", "__iter__() i __flow__()"], "__iter__() i __super__()", 500000),
        Millionaire("Using a manager package, how can you put components in a container in the same order?", ["Component.pack(side=\"LEFT\")", "Component.pack(\"Left\")", "Component.pack(side=LEFT)", "Component.pack(Left-side)"], "Component.pack(side=LEFT)", 1000000)
    ]

    # Introduction with the user
    hyphen = "-" * 80
    correct_answered = 0
    question_count = 0

    fifty_fifty_count = 1
    phone_friend_count = 1
    audiance_count = 1

    while True:
        print(f"{hyphen}\nWelcome to the game \"Who Wants to Be a Millionaire?\"\n"
              f"The questions will consist solely of the python programming language\n")

        user_response = input(f"If you want to play a game type: Yes\n"
                              f"If you dont want to play a game type: No\n"
                              f"\nEnter your answer: ")

        if user_response == "no" or user_response == "No" or user_response == "NO":
            exit(1)

        elif user_response != "yes" and user_response != "Yes" and user_response != "YES":
            print(f"\nYou must type \"Yes\" or \"No\".")
        else:
            break

    # Printing questions and answers

    for element in millionaire:
        question_count += 1
        print(f"{hyphen}\nQuestion number {question_count}: {element.question}\n")
        print("Offered answers:\n")
        offered_answers = element.answers

        answer_number = 0 
        while answer_number < len(offered_answers): # The answers are in the list and "answer_number" is iterator.
            print(f"{str(answer_number + 1)}: {offered_answers[answer_number]}")
            answer_number += 1

        # If 50:50 is used, the audience needs to respond to 2 offered answers instead of 4
        counter_if_fifty_fifty_is_used = 0
        counter_if_ask_the_audiance_is_used = 0

        # Phonelines

        while fifty_fifty_count == 1 or phone_friend_count == 1 or audiance_count == 1:
            help_phone_lines = input("\nPress \"5\" to use available Help. Otherwise press anything: ")

            if help_phone_lines == "5":
                print(hyphen)
                if fifty_fifty_count == 1:
                    print("Press \"6\" to use \"50:50\". Otherwise press anything: ")
                if phone_friend_count == 1:
                    print("\nPress \"7\" to use \"Phone a Friend\". Otherwise press anything: ")
                if audiance_count == 1:
                    print("\nPress \"8\" to use  \"Ask the Audiance\". Otherwise press anything: ")
                print(hyphen)

                phone_lines = input("\nEnter number of phoneline that you want to choose: ")

                # 50:50
                if phone_lines == "6":
                    element.fifty_fifty(question_count)
                    fifty_fifty_count -= 1
                    counter_if_fifty_fifty_is_used += 1
                    print(f"\n*Reminder that you need to enter answer number from original question and not \"50:50\"")

                # Phone a Friend
                elif phone_lines == "7":
                    print(element.phone_friend(question_count))
                    phone_friend_count -= 1

                # Audiance help
                elif phone_lines == "8":
                    counter_if_ask_the_audiance_is_used += 1

                    # If 50:50 is used, the audience needs to respond to 2 offered answers instead of 4
                    if counter_if_fifty_fifty_is_used == counter_if_ask_the_audiance_is_used:
                        element.ask_the_audience(100, 2)
                        audiance_count -= 1
                        print("\n*Reminder that you need to enter answer number from original question and not \"Ask the Audiance\"")
                    else:
                        element.ask_the_audience(100, 4)
                        audiance_count -= 1

                # Incorrect phoneline input
                while phone_lines != "6" and phone_lines != "7" and phone_lines != "8":
                    print("\nAnswer must be a valid number")
                    phone_lines = input("\nEnter number of help that you want to choose: ")

                    # Repeating phoneline input code
                    # 50:50
                    if phone_lines == "6":
                        element.fifty_fifty(question_count)
                        fifty_fifty_count -= 1
                        counter_if_fifty_fifty_is_used += 1
                        print(f"\n*Reminder that you need to enter answer number from original question and not \"50:50\"")

                    # Phone a Friend
                    elif phone_lines == "7":
                        print(element.phone_friend(question_count))
                        phone_friend_count -= 1

                    # Audiance help
                    elif phone_lines == "8":
                        counter_if_ask_the_audiance_is_used += 1
                        if counter_if_fifty_fifty_is_used == counter_if_ask_the_audiance_is_used:
                            element.ask_the_audience(100, 2)
                            audiance_count -= 1
                            print("\n*Reminder that you need to enter answer number from original question and not \"Ask the Audiance\"")
                        else:
                            element.ask_the_audience(100, 4)
                            audiance_count -= 1

                else:
                    continue
            else:
                break

        # User's answer
        user_answer = input("\nEnter the correct answer number: ")  # The original type is a string due to a later "isdigit" check

        # Checking if the answer is number
        while not user_answer.isdigit():
            print("Answer must be from 1 to 4.")
            user_answer = input("\nEnter the correct answer number: ")
        user_answer = int(user_answer)

        # Checking if the answer is not from 1 to 4
        while user_answer < 1 or user_answer > len(offered_answers):

            print("Answer must be from 1 to 4.")
            # Checking if the answer is string
            try:
                user_answer = int(input("\nEnter the correct answer number: "))
            except:
                print("")

        # Checking if the answer is correct

        if offered_answers[user_answer - 1] == element.correct_answer:
            if question_count == 5 or question_count == 10 or question_count == 15:
                pass
            else:
                print(f"\nCongratulations, \"{element.correct_answer}\" was correct answer.")
                print(f"Curent correct answers: {correct_answered + 1}/15")
                print(f"Current amount earned: {element.money:,}$")
                correct_answered += 1

            # Guaranteed money check
            if question_count == 5 or question_count == 10 or question_count == 15:
                print(f"\nCongratulations, \"{element.correct_answer}\" was correct answer.")
                print(f"Curent correct answers: {correct_answered + 1}/15")
                print(f"You have earned check for {element.money:,}$")
                print(f"{element.money:,}$ is guaranteed money that you earned.\n")
                correct_answered += 1

            # If user wants to quit with earned money
            if question_count > 0 and question_count != 5 and question_count != 10 and question_count != 15:
                user_quit = input("\nPress \"0\" if you want to quit game with earned money. Otherwise press anything to continue: ")
                if user_quit == "0":
                    print(f"\nYou have successfully exited the game.")
                    print(f"Correct answers: {correct_answered}/15")
                    print(f"The amount earned: {element.money}$\n")
                    exit(0)

        # Checking if the answer is incorrect
        else:
            print("\nYour answer is incorrect.")
            print(f"Correct answers: {correct_answered}/15")
            print(f"The correct answer was: \"{element.correct_answer}\"")

            # Function is not to repeat our code 
            def incorrect_answer(earned_money):
                print(f"The sum of money won: {earned_money:,}$\n")
                exit(1)


            if 0 <= correct_answered < 5:
                incorrect_answer(0)
            elif 5 <= correct_answered < 10:
                incorrect_answer(1000)
            elif 10 <= correct_answered < 15:
                incorrect_answer(32000)
                
            exit(1)

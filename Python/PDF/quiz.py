import time
import random
import os
def sound():
    if os.name=="nt":
        import winsound
        winsound.beep(1000,200)
def loud_high_score():
    try:
        with open("highscore.txt","r")as file:
            return int(file.read())
    except:
        return 0
def save_high_score(score):
    high=loud_high_score()
    if score > high:
        with open("highscore.txt","w") as file:
            file.write(str(score))
        print("🏆 New High Score!")


def run_quiz(Questions,time_limit=10):

    score = 0
    start_time=time.time()
    for q in Questions:
        print("\n" + q["Question"])  # ✅ Fixed typo: "/n" → "\n"
        for option in q["Option"]:   # ✅ Use consistent key: "Option" not "option"
            print(option)
        elapsed=time.time()-start_time
        if elapsed>time_limit*len(Questions):
            print("⏰ Time's up!")
            break
        answer = input("Your Answer (A/B/C/D): ").strip().upper()
        if answer == q["Answer"]:    # ✅ Use consistent key: "Answer"
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {q['Answer']}")
    print(f"\n🎯 Final Score: {score}/{len(Questions)}")
    save_high_score(score)

quiz_questions = [
    {
        "Question": "What is capital of Pakistan?",
        "Option": ["A. Lahore", "B. Multan", "C. Karachi", "D. Islamabad"],
        "Answer": "D"
    },
    {
        "Question": "Which Language is used for web App",
        "Option": ["A. JAVA", "B. JAVASCRIPT", "C. Python", "D. C++"],
        "Answer": "B"
    }
]
random.shuffle(quiz_questions)
run_quiz(quiz_questions)
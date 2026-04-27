from planner import plan
from tools import get_topic_data, get_all_topics
from formatter import format_output
from memory import save, get_history

def run_agent():
    topic = input("Enter a topic: ")

    print("\n🤖 Agent is analyzing the topic...")

    plan_data = plan(topic)
    data = get_topic_data(plan_data["topic"])

    # ❌ Topic not found handling
    if not data:
        print("❌ Topic not found.")
        print("Try these:", ", ".join(get_all_topics()))
        return

    print("📚 Generating study material...\n")

    result = format_output(topic, data)

    # 💾 Save to memory
    save(topic)

    # 📁 Save output to file
    with open("output/sample.txt", "w", encoding="utf-8") as f:
        f.write(result)

    # 📢 Show result
    print(result)

    # 🧠 Quiz Mode
    choice = input("\nDo you want to take a quiz? (yes/no): ")

    if choice.lower() == "yes":
        score = 0
        questions = data["questions"]
        answers = data["answers"]

        for i in range(len(questions)):
            user_ans = input(f"\n{questions[i]}\nYour answer: ").lower().strip()

            if user_ans == answers[i]:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {answers[i]}")

        print(f"\n🎯 Your Score: {score}/{len(questions)}")

    # 🧾 Show memory
    history = get_history()
    if history:
        print("\n🧾 Topics you've studied:")
        for t in history:
            print(f"- {t}")

if __name__ == "__main__":
    run_agent()
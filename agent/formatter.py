def format_output(topic, data):
    if not data:
        return "Topic not found."

    output = f"\n📘 Topic: {topic.title()}\n\n"
    output += f"📖 Definition:\n{data['definition']}\n\n"

    output += "🔑 Key Points:\n"
    for point in data["key_points"]:
        output += f"- {point}\n"

    output += f"\n🧠 Summary:\n{data['summary']}\n\n"

    output += "❓ Questions:\n"
    for q in data["questions"]:
        output += f"- {q}\n"

    return output
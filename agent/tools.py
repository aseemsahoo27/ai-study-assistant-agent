import json

def load_data():
    with open("data/topics.json", "r") as f:
        return json.load(f)

def get_topic_data(topic):
    data = load_data()
    return data.get(topic, None)

def get_all_topics():
    data = load_data()
    return list(data.keys())
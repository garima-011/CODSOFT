"""
CODSOFT - Artificial Intelligence Internship
Task 1: Rule-Based Chatbot

A simple chatbot that uses pattern matching (regular expressions) to
understand user input and respond with predefined rules. This is a
classic example of a rule-based conversational agent.
"""

import re
import random
from datetime import datetime


class RuleBasedChatBot:
    def __init__(self, name="CodBot"):
        self.name = name
        # Each rule is a (pattern, list_of_possible_responses) pair.
        # We use regex so the bot can match many phrasings, not just
        # exact strings.
        self.rules = [
            (r".*\b(hi|hello|hey|hii+|heya)\b.*",
             ["Hello! How can I help you today?",
              "Hi there! What's on your mind?",
              "Hey! Good to see you."]),

            (r".*\bhow are you\b.*",
             ["I'm just a program, but I'm running smoothly! How about you?",
              "Doing great, thanks for asking!"]),

            (r".*\b(your name|who are you)\b.*",
             [f"I'm {self.name}, a rule-based chatbot built for the CodSoft AI internship."]),

            (r".*\bmy name is (\w+).*",
             ["Nice to meet you, {0}!"]),

            (r".*\b(what.?s the time|current time)\b.*",
             ["dynamic_time"]),  # handled specially below

            (r".*\b(date|today.?s date)\b.*",
             ["dynamic_date"]),

            (r".*\b(joke|funny)\b.*",
             ["Why do programmers prefer dark mode? Because light attracts bugs!",
              "I told my computer I needed a break, and now it won't stop sending me Kit-Kats.",
              "Why was the math book sad? It had too many problems."]),

            (r".*\b(help|what can you do)\b.*",
             ["I can chat with you, tell jokes, share the time/date, "
              "and respond to simple greetings. Try asking me something!"]),

            (r".*\b(thank you|thanks)\b.*",
             ["You're welcome!", "Anytime!", "Glad I could help."]),

            (r".*\b(bye|goodbye|see you|exit|quit)\b.*",
             ["exit_chat"]),  # handled specially below
        ]

        self.default_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "Hmm, I don't have a rule for that yet. Try asking something else!",
            "Sorry, can you say that differently?",
        ]

    def get_response(self, user_input):
        text = user_input.strip().lower()

        for pattern, responses in self.rules:
            match = re.match(pattern, text)
            if match:
                response = random.choice(responses)

                # Special dynamic handling
                if response == "dynamic_time":
                    return f"The current time is {datetime.now().strftime('%I:%M %p')}."
                if response == "dynamic_date":
                    return f"Today's date is {datetime.now().strftime('%B %d, %Y')}."
                if response == "exit_chat":
                    return "exit_chat"

                # Fill in captured groups (e.g. user's name)
                if match.groups():
                    return response.format(*match.groups())
                return response

        return random.choice(self.default_responses)

    def chat(self):
        print(f"{self.name}: Hi! I'm {self.name}, your rule-based chatbot. "
              f"Type 'bye' to exit.\n")

        while True:
            user_input = input("You: ")
            if not user_input.strip():
                continue

            response = self.get_response(user_input)

            if response == "exit_chat":
                print(f"{self.name}: Goodbye! Have a great day. \U0001F44B")
                break

            print(f"{self.name}: {response}")


if __name__ == "__main__":
    bot = RuleBasedChatBot()
    bot.chat()

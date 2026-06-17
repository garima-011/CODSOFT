# Task 1 - Rule-Based Chatbot

A simple chatbot built for the CodSoft Artificial Intelligence Internship.
It uses **regular expression pattern matching** to understand user input
and respond with predefined rules — no machine learning involved, just
clean logic-based conversation flow.

## Features
- Greeting detection (hi, hello, hey...)
- Remembers and uses your name if you tell it
- Tells the current time/date
- Tells programmer jokes
- Help command
- Graceful exit on "bye"/"quit"
- Falls back to a polite "I don't understand" message for unknown input

## How to run
```bash
python chatbot.py
```

Then just type messages at the `You:` prompt. Type `bye`, `exit`, or `quit`
to end the conversation.

## Example
```
CodBot: Hi! I'm CodBot, your rule-based chatbot. Type 'bye' to exit.

You: hello
CodBot: Hi there! What's on your mind?
You: my name is Aman
CodBot: Nice to meet you, aman!
You: tell me a joke
CodBot: Why do programmers prefer dark mode? Because light attracts bugs!
You: bye
CodBot: Goodbye! Have a great day. 👋
```

## Concepts demonstrated
- Pattern matching with Python's `re` module
- Basic NLP concept: intent recognition via keyword/pattern rules
- Conversational loop design

---
Built as part of the **#codsoft** Artificial Intelligence Internship.

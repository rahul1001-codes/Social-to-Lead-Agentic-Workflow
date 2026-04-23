from intent import detect_intent
from rag import get_pricing
from tools import mock_lead_capture

class Agent:
    def __init__(self):
        self.state = {
            "intent": None,
            "name": None,
            "email": None,
            "platform": None,
            "lead_stage": 0
        }

    def respond(self, user_input):
        intent = detect_intent(user_input)

        # Greeting
        if intent == "greeting":
            return "Hey! 👋 How can I help you with AutoStream?"

        # Pricing (RAG)
        elif intent == "pricing":
            return get_pricing()

        # High Intent Flow
        elif intent == "high_intent":
            self.state["intent"] = "high_intent"
            self.state["lead_stage"] = 1
            return "Awesome! Let's get you started. What's your name?"

        # Lead Collection Flow
        if self.state["intent"] == "high_intent":

            if self.state["lead_stage"] == 1:
                self.state["name"] = user_input
                self.state["lead_stage"] = 2
                return "Great! What's your email?"

            elif self.state["lead_stage"] == 2:
                self.state["email"] = user_input
                self.state["lead_stage"] = 3
                return "Which platform do you create content on?"

            elif self.state["lead_stage"] == 3:
                self.state["platform"] = user_input

                # Call tool ONLY after all data collected
                mock_lead_capture(
                    self.state["name"],
                    self.state["email"],
                    self.state["platform"]
                )

                self.state["lead_stage"] = 0
                return "You're all set! 🚀 We'll reach out soon."

        return "I'm not sure I understand. Can you clarify?"
    


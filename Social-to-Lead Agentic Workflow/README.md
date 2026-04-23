# AutoStream AI Agent

## How to Run
1. Clone repo
2. Install dependencies:
   pip install -r requirements.txt
3. Run:
   python main.py

## Architecture
This project uses a modular agent-based architecture. Intent detection is handled via rule-based classification for simplicity and reliability. RAG (Retrieval-Augmented Generation) is implemented using a local JSON knowledge base to ensure accurate responses for pricing and policies without hallucination.

State management is implemented using a Python dictionary inside the Agent class, allowing memory across multiple conversation turns. This ensures proper tracking of user intent and lead collection stages.

Tool execution is handled via a controlled pipeline where the lead capture function is only triggered after all required inputs (name, email, platform) are collected.

LangGraph was not used here for simplicity, but the same logic can be extended into graph-based flows for production systems.

## WhatsApp Integration
Use WhatsApp Business API with webhooks:
- Receive user messages via webhook
- Pass message to agent
- Return response via API
- Store user state in DB (Redis/Firebase)


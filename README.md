# SupportGPT – AI Customer Support Assistant 🤖

## Overview
SupportGPT is an AI-powered customer support assistant designed to automate and enhance customer interactions using LLMs.

The application provides a chat-based interface where users can ask questions and receive intelligent, human-like responses in real time.

## Features
- Chat-based UI with conversation history
- Real-time AI-generated responses using Gemini API
- Clean and responsive interface
- Multi-line response handling with proper formatting
- Error handling and retry logic for API rate limits

## Tech Stack
- Python
- FastAPI
- Gemini API (Google Generative AI)
- HTML/CSS

## How It Works
User input is sent to the FastAPI backend, which processes the request using the Gemini API. The generated response is then displayed in a chat-style interface.

## Setup
1. Clone the repository
2. Add your API key in `.env`
3. Install dependencies:
   pip install -r requirements.txt
4. Run:
  uvicorn main:app --reload


## Future Improvements
- Add conversation memory with context awareness
- Deploy the application for public access
- Integrate document-based querying (RAG)
- Improve UI with modern frontend frameworks

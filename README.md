# ⚽ Soccer AI Explainer

## AI-Powered Soccer Tactical Analysis Assistant

Soccer AI Explainer is an AI-powered application that analyzes soccer match descriptions and provides tactical explanations using Large Language Models.

This project was developed during the **IBM AI Innovation Challenge 2026** and explores how generative AI can help users better understand soccer tactics, formations, and strategic decisions.

---

## Project Overview

Soccer tactics can be difficult to understand for many fans. While viewers can watch matches, they may not understand:

- Why teams change formations
- How tactical adjustments influence the game
- Why certain player movements create advantages
- How coaches make strategic decisions

Soccer AI Explainer uses AI to transform complex match descriptions into simple and understandable tactical explanations.

---

# Features

## ⚽ Match Tactical Analysis

Users can provide a soccer match scenario and receive AI-generated tactical explanations.

Example input:

```
The team changed from a 4-3-3 formation to a 3-5-2 system after halftime to increase attacking pressure.
```

The AI explains:

- Formation changes
- Tactical adjustments
- Player roles
- Strategic impact

---

## 🤖 AI-Powered Analysis

The application uses Large Language Models to generate:

- Tactical summaries
- Match explanations
- Strategic insights

---

## 🌐 Web Application

The project contains:

- React frontend interface
- FastAPI backend service
- AI analysis workflow

---

# System Architecture

```
User

  ↓

React Frontend

  ↓

FastAPI Backend

  ↓

AI Language Model

  ↓

Tactical Explanation
```

---

# Technology Stack

## Backend

- Python
- FastAPI
- Uvicorn

## Frontend

- React
- JavaScript

## AI Technologies

- IBM Granite (planned integration)
- Large Language Models
- Prompt Engineering

---

# Project Structure

```
soccer-ai-explainer/

│
├── backend/
│   └── main.py
│
├── frontend/
│   └── React Application
│
├── data/
│   └── sample_match.txt
│
├── requirements.txt
│
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/soccer-ai-explainer.git
```

## Backend Setup

Navigate to backend folder:

```bash
cd backend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run FastAPI server:

```bash
uvicorn main:app --reload
```

---

## Frontend Setup

Navigate to frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run React application:

```bash
npm run dev
```

---

# IBM AI Innovation Challenge

This project was created as part of the **IBM AI Innovation Challenge 2026**.

The goal was to explore how AI can assist users in understanding complex information.

Soccer AI Explainer demonstrates how generative AI can be applied to sports analysis by converting match descriptions into meaningful tactical explanations.

---

# AI Workflow

```
Match Description

        ↓

Prompt Processing

        ↓

AI Model Analysis

        ↓

Tactical Explanation

        ↓

User Interface
```

---

# Future Improvements

Future versions may include:

- Real IBM Granite API integration
- Real-time match analysis
- Player position visualization
- Formation recognition
- Computer vision based player tracking
- Live game tactical assistant
- Voice-based soccer analysis

---

# Author

**Edmond Qiu**

Computer Science Student  
Concordia University

---

# License

MIT License

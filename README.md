# Sequential Agentic AI 🚀

A multi-agent **Sequential Chaining AI framework** that transforms a user’s project idea into a complete development pipeline:

**Research → Planning → Code Generation → Debugging → Documentation**

Built using **LLMs + Agentic AI + Streamlit**, this project demonstrates how multiple specialized AI agents can work together step-by-step to automate the software development lifecycle.

---

## 🌐 Live Demo

**Deployment Link:**  
[https://sequential-agentic-ai.streamlit.app/](https://sequential-agentic-ai.streamlit.app/)

---

## 📌 Project Workflow

```text
User Input
   ↓
Research Agent
   ↓
Planning Agent
   ↓
Coding Agent
   ↓
Execution Engine
   ↓
Debugging Agent (if errors occur)
   ↓
Documentation Agent
```

Each agent’s output becomes the next agent’s input, making this a **Sequential Chaining Architecture**.

---

## ✨ Features

- Multi-agent architecture
- Sequential chaining workflow
- Automatic project research
- Step-by-step planning generation
- Full Python code generation
- Automatic code execution
- Error detection and correction
- README/documentation generation
- Download generated code
- Download README file
- Interactive premium Streamlit UI
- Real-time processing
- Hybrid execution-debugging system

---

## 🤖 Agents Overview

### 1. Research Agent

Analyzes the user’s idea and determines:

- Problem type
- Best algorithms
- Preprocessing steps
- Evaluation metrics

Example:

```text
Input: Build a spam classifier

Output:
- Classification problem
- Logistic Regression / SVM
- TF-IDF preprocessing
- Accuracy / F1-score
```

---

### 2. Planning Agent

Converts research into structured development steps.

Example:

```text
1. Load dataset
2. Clean data
3. Train model
4. Evaluate performance
```

---

### 3. Coding Agent

Generates raw Python code based on the plan.

Produces:

```text
train.py
```

---

### 4. Execution Engine

Runs the generated code directly using Python.

This improves debugging accuracy because large code blocks are executed directly instead of being passed as tool arguments.

---

### 5. Debugging Agent

Only activates if execution fails.

It receives:

- Full generated code
- Full error traceback

Then returns corrected code.

---

### 6. Documentation Agent

Generates:

```text
README.md
```

with project explanation and usage instructions.

---

## 🛠 Tech Stack

- Python
- Streamlit
- Agno
- Groq API
- Agentic AI
- Sequential Chaining
- Subprocess
- Tempfile

---

## 🎯 Why This Project?

This project demonstrates:

- Agent orchestration
- Sequential chaining logic
- Tool integration
- Real-world LLM workflows
- Automated code lifecycle generation
- Hybrid execution + AI debugging

Strong for:

- Resume building
- Internships
- Agentic AI portfolio
- LLM engineering

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/AKR-Anmol-Kumar-Rai/sequential-agentic-ai.git
cd sequential-agentic-ai
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

Or for deployment, use Streamlit Secrets.

---

## ▶ Run Locally

```bash
streamlit run main.py
```

---

## ☁ Deployment

Deployed using:

- Streamlit Cloud

Add secrets:

```toml
GROQ_API_KEY="your_actual_api_key"
```

---

## ⚠ Known Limitations

- Sometimes the app may crash if the LLM provider reaches its **rate limit**.
- Token quota limits may stop processing temporarily.
- Large generated code may occasionally be incomplete depending on model constraints.
- Execution depends on installed Python dependencies.

This is normal behavior for API-based LLM systems.

---

## 🚀 Future Improvements

- Multi-LLM support
- Better retry handling
- Automatic dependency detection
- Docker support
- Better code validation
- Agent memory support
- Database integration

---

## 👨‍💻 Author

**Anmol Kumar Rai**

GitHub:  
:contentReference[oaicite:0]{index=0}

---

## 📜 License

MIT License

---

This project showcases the practical implementation of **Agentic AI + Sequential Chaining** for automating software development workflows.

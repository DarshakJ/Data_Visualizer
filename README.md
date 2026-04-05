# AI-Powered Auto Dashboard Generator

A lightweight, privacy-first analytics system that turns natural language questions into SQL queries and visual dashboards—without requiring users to interact with complex databases or BI tools.

---

## 🚀 Overview

This project explores a streamlined approach to data analytics using small LLMs and agent-based architecture.

**Goal:**
Enable non-technical users (sales teams, management, etc.) to simply ask questions and instantly receive meaningful insights in the form of charts and dashboards.

No SQL. No dashboards to configure. Just ask.

---

## 🎯 Key Features

* 🔎 Natural language → SQL query generation
* 📊 Automatic graph & dashboard creation
* 🧠 Agent-based modular architecture
* 🔒 Fully on-prem deployment (via Ollama)
* ⚡ Lightweight models (Llama 3.2, Qwen 2.5 3B)
* 🖥️ Streamlit UI for quick visualization

---

## 🏗️ Architecture

The system is built around a simple but effective agent workflow:

### 1. Query Producer (Agent)

* Understands user input
* Uses database schema as context
* Generates optimized SQL queries
* Executes queries via tool calling
* Returns structured results

### 2. Format Checker (Agent)

* Takes raw query output
* Cleans and structures data
* Converts into graph-ready format
* Ensures compatibility with visualization layer

### 3. Frontend (Streamlit)

* Displays results as charts and dashboards
* Provides a simple interface for user queries

---

## ⚙️ Tech Stack

* **LLMs:** Llama 3.2, Qwen 2.5 3B
* **Runtime:** Ollama (for local inference)
* **Agent Framework:** Google ADK
* **Frontend:** Streamlit
* **Database:** Any SQL-compatible database

---

## 🔄 Workflow

1. User enters a natural language query
2. Query Producer generates SQL using schema context
3. SQL query is executed on the database
4. Results are passed to Format Checker
5. Output is structured for visualization
6. Streamlit renders graphs/dashboard

---

## 🧩 Example Use Case

> “Show me monthly sales by region for the last 6 months”

System flow:

* Converts to SQL query
* Executes against database
* Formats output
* Displays a chart (e.g., line or bar graph)

---

## ⚠️ Challenges

* Tool calling reliability with small LLMs
* SQL accuracy with limited context windows
* Maintaining consistent output formatting for visualization
* Balancing performance vs model size

---

## 🔒 Design Principles

* **Privacy-first:** All data remains on-prem
* **Lightweight:** Works with smaller models
* **Modular:** Agent-based design for flexibility
* **User-first:** No technical knowledge required

---

## 📌 Future Improvements

* Better tool-calling reliability for small models
* Schema-aware memory optimization
* Smarter visualization selection
* Multi-database support
* Caching & query optimization

---

## 🤝 Contributing

This is an early-stage project exploring practical limits of small LLMs in structured data workflows. Contributions, ideas, and feedback are welcome.

---

## 💬 Feedback

If you’ve built something similar or experimented with agent-based data systems, feel free to share your insights—especially around:

* Tool calling with smaller models
* Improving SQL generation accuracy
* Visualization automation

---

## 📄 License

MIT License (or your preferred license)

---

**Status:** 🚧 Work in Progress


### Run
- streamlit run app.py --server.port 8081
- adk api_server

### Architecture
<img width="585" height="317" alt="image" src="https://github.com/user-attachments/assets/187fe39f-42df-4fc2-a242-7487dc185c51" />

## Agent Data flow  
### STATE
<img width="412" height="457" alt="image" src="https://github.com/user-attachments/assets/d482ec8e-d153-476a-9798-5733aeecfb8d" />

### Agent 1 : Query_Producer Request
<img width="1280" height="389" alt="image" src="https://github.com/user-attachments/assets/79abc61e-92ff-45cf-90fc-61b2ed5da0c2" />

### Agent 1 : Query_Producer Response
<img width="1280" height="367" alt="image" src="https://github.com/user-attachments/assets/57771ade-9ccb-4d54-bce8-d564c7fc420e" />

### Agent 2 : Validator_and_formatter Request
<img width="1280" height="418" alt="image" src="https://github.com/user-attachments/assets/c8860faf-3e7a-4e29-9c2a-8f89c036a2dd" />

### Agent 2 : Validator_and_formatter Response
<img width="1280" height="365" alt="image" src="https://github.com/user-attachments/assets/1251b05a-d1f7-4aec-93df-d5909d2be0bd" />

### Evaluation:
<img width="419" height="227" alt="image" src="https://github.com/user-attachments/assets/78a297e8-6de0-4026-950c-7a3b38d09110" />



## Outputs
### Title based Area graph
![Title_wise_area](https://github.com/user-attachments/assets/f8536e43-6faf-46a0-b02d-0b1cb17d4083)

### Termination based table
![Table_termination](https://github.com/user-attachments/assets/61880f81-f605-45a7-8d59-6d39e2bee83c)

### State based graph line
![ine](https://github.com/user-attachments/assets/1559f4c6-4bca-4982-af58-ae939b326358)

### Gender based graph pie
![Gender_pie](https://github.com/user-attachments/assets/19a1655d-e371-4aca-84f5-d064411d4383)

### Department based bar graph
![Department_bar](https://github.com/user-attachments/assets/6bccbec5-9760-4730-848a-d99732d82aca)

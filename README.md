# 🧠 Q&A Chatbot with Ollama and Streamlit 🚀  

A **Q&A Chatbot** powered by **Ollama LLM**, **LangChain**, and **Streamlit**, allowing users to ask questions and receive AI-generated responses in real time.

---

## 🌟 Features
✅ **Interactive UI** – Simple and intuitive chat interface powered by **Streamlit**  
✅ **Ollama LLM Integration** – Get responses from advanced language models  
✅ **Customizable Settings** – Adjust model parameters such as **temperature** and **max tokens**  
✅ **LangChain for Prompt Management** – Efficient pipeline for handling user queries  
✅ **Fast & Lightweight** – Minimal setup and easy deployment  

---

## 🛠️ Installation & Setup

### 🔹 1. Clone the Repository
```bash
git clone https://github.com/your-username/qa-chatbot-ollama.git
cd qa-chatbot-ollama

```




### 🔹  2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 🔹   3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔹   4. Set Up Environment Variables
Create a .env file in the root directory and add the following:
```bash
LANGCHAIN_API_KEY=your_langchain_api_key

```
Replace your_langchain_api_key with your actual LangChain API key.
### 🔹   5. Run the Application
```bash
streamlit run app.py


```
Then, open the Streamlit app in your browser to start using the chatbot.


###  📁 Project Structure
```bash
📂 qa-chatbot-ollama
│-- 📜 app.py                  # Main Streamlit application
│-- 📜 requirements.txt        # Required dependencies
│-- 📜 .env                    # Environment variables (ignored in .gitignore)
│-- 📜 README.md               # Project documentation


```
Then, open the Streamlit app in your browser to start using the chatbot.

### 🎯 How to Use
1️⃣ Open the Streamlit web app
2️⃣ Enter your question in the input box
3️⃣ Select a model and adjust temperature & max tokens
4️⃣ Click Submit and view the AI-generated response



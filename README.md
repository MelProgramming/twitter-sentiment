# Twitter Sentiment Analysis

A Python project that collects recent tweets about any topic and analyzes their sentiment using **Text Blob**. This project is structured like a real-world application, split into multiple modules for clariy and scalability.

---

## 📌 Features
- Fetches recent tweets using the free Twitter API **Tweepy (Twitter API v2)**
- Performs sentiment analysis (positive/neutral/negative)
- Cleans and preprocesses tweet text
- Exports results to a **CSV file**
- Modular folder structure (easy to extend and maintain)
- Ready for resume & portfolio use

---

## 📂 Project Structure
```
twitter-sentiment/
│── data/                   # Stores CSV output files
│── src/
│   ├── twitter_client.py           # Handles Twitter API communication
│   ├── twitter_sentiment.py        # TextBlob sentiment analysis
│   ├── utils.py                    # Text cleaning utilities
│   └── main.py                     # Program entry point
│── .gitignore
│── requirements.txt        # Dependencies
│── README.md
```

---

## 🚀 Setup instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/twitter-sentiment.git
cd twitter-sentiment
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your Twitter API Bearer Token
Create a `.env` file in the project root:

```bash
TWITTER_BEARER_TOKEN="your_bearer_token_here"
```

### 4. Run the project
```bash
python src/main.py
```

---

## 🧪 Example Output (CSV)
A sample row looks like:

```
tweet_id, text, polarity, sentiment
1234567890, "I love Python!", 0.70, positive
```

---

## 🔧 Future Enhancements
- Add sentiment visualizations (matplotlib)
- Dashboard using Streamlit
- Automatic topic detection (NLP)
- Save results to a SQLite database
- Deploy as an API (FastAPI)

  ---
  
## 📝 License

This project is open-source under the MIT License.

---

## 🤝 Contributing 
Pull requests are welcome!
If you'd like to contribute or suggest improvements, feel free to open an issue.


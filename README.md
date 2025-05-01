# 🧪 TestPilot – Lightweight QA Automation and Reporting Tool

**TestPilot** is a lightweight, extensible QA automation and reporting tool designed to streamline test case execution, automate result collection, and visualize test analytics via a responsive dashboard.

---

## 🚀 Features

- ✅ Automated execution of UI or functional test scripts
- 📊 Real-time dashboard with Pie and Line charts for test analytics
- 📄 Downloadable PDF test reports with full test summaries
- 🧠 Optional AI integration for generating test suggestions (OpenAI / Hugging Face compatible)
- 🗂️ SQLite-based local result storage
- 🔄 Simple scheduler for periodic test runs
- 🧰 Fully containerized and easily deployable

---

## 📁 Project Structure

```bash
TestPilot/
├── dashboard_app.py         # Flask dashboard web app
├── run_tests.py             # Main test runner script
├── sample_test_script.py    # Sample test case script
├── utils/
│   └── logger.py            # Logging utility
├── db/
│   └── test_results.db      # SQLite database storing results
├── templates/               # HTML templates for rendering
├── static/                  # Bootstrap/JS/CSS files
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```


## ⚙️ Setup & Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/TestPilot.git
cd TestPilot
```
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```
```bash
# Install dependencies
pip install -r requirements.txt
```


## 🧪 Running the Tests

```bash
# Run the test script and store results in the database:
python run_tests.py
```

## 📊 Launch Dashboard

```bash
# Start the dashboard to view charts and download the report:
python dashboard_app.py
```

## 📥 Download PDF Report
Click the Download Test Report PDF button on the dashboard to generate a full summary report of your test run.

## 🧠 Optional AI Integration
Want to generate test cases using AI?
- Replace OpenAI API with Hugging Face endpoint in run_tests.py
- Add your token as HUGGINGFACE_API_KEY

## 🛠️ Technologies Used
- Python 3.9+
- Flask
- SQLite
- Plotly
- Pandas
- FPDF
- BeautifulSoup / Requests (for scraping)
- Selenium (optional for UI tests)

## 🔒 Security & Data
All test results are stored locally. No data is shared externally unless configured.


## 🙌 Acknowledgments
Thanks to the open-source Python and Flask communities for their continued support.

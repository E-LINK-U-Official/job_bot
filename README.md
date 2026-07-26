# Automated Web Data Extraction & Filtering Pipeline

A real-time, modular Python framework engineered to deploy automated Chrome browser sessions, extract live job board layout structures via Selenium, and execute local semantic text parsing.

## 🛠️ System Architecture

The ecosystem is split into three independent, production-grade engines:
1. **`main.py` & `scraper.py` (Open-Source Multi-Platform Aggregator)**: Spawns automated Chrome sessions to extract, parse, and clean hundreds of live remote data vacancies from open registries (RemoteOK, WeWorkRemotely) simultaneously into unique historical Excel databases (`jobs_[timestamp].xlsx`).
2. **`linkedin_bot.py` (Dedicated Corporate Tracker)**: An isolated automation module built specifically to bypass LinkedIn's modern layout gates using secure session cookie injection (`li_at`), allowing direct access to verified enterprise postings.
3. **`ai_agent.py` (Local Compliance Matrix)**: A fast string-processing shield that acts as an eligibility gate, automatically dropping third-party spam agencies and non-qualified senior requirements.

## 📦 Tech Stack
* **Language**: Python 3
* **Automation**: Selenium WebDriver (Chrome Engine)
* **Data Logistics**: Pandas & OpenPyXL
* **Security Sandboxing**: `python-dotenv` (Protects session credentials locally)

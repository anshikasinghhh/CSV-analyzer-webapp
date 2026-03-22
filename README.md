📊 CSV Analyzer Web App
🚀 Overview

The CSV Analyzer Web App is a full-stack data analysis platform that allows users to upload CSV files, explore datasets, generate interactive visualizations, and make machine learning predictions. It combines statistical analysis, ML, and a responsive UI for seamless data exploration.

✨ Features
📂 Upload CSV files for analysis
📊 View dataset preview and summary statistics
📈 Interactive charts (histogram, scatter, bar, box plots)
🤖 Predict outcomes using Linear Regression
📱 Fully responsive and user-friendly interface
🛠️ Tech Stack
🔹 Backend
Flask (Python web framework)
Werkzeug (WSGI server)
Python 3.10
🔹 Data Processing & ML
Pandas (data manipulation)
NumPy (numerical computing)
Scikit-learn (Linear Regression model)
Matplotlib (basic plotting support)
🔹 Visualization
Plotly.js (interactive charts)
🔹 Frontend
HTML5
CSS3 (custom responsive design)
JavaScript (DOM manipulation)
Jinja2 (templating engine)
Font Awesome (icons)
🧩 System Architecture
Component	Technology
Server	Flask + Werkzeug
Data Source	CSV files (handled via Pandas)
ML Model	Scikit-learn (Linear Regression)
Visualization	Plotly.js
UI	Custom CSS + JavaScript
⚙️ Installation & Setup
1. Clone Repository
git clone https://github.com/anshikasinghhh/CSV-analyzer-webapp.git
cd csv-analyzer
2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Run Application
python app.py
5. Open in Browser
http://127.0.0.1:5000/
📌 How to Use
Upload your CSV file
Explore dataset preview and statistics
Generate interactive visualizations
Apply prediction model
Analyze insights
📊 Example Use Case

Users can upload datasets like:

Sales data → analyze trends & forecast revenue
Student data → predict performance
Business metrics → evaluate growth patterns
🔮 Future Enhancements
Multiple ML models (classification, clustering)
File export (CSV/PDF reports)
Cloud deployment (AWS, Render)
Authentication & user dashboards
🤝 Contributing

Contributions are welcome! Fork the repository and submit a pull request.

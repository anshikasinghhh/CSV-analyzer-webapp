from flask import Flask, render_template, request, session, send_file
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LinearRegression
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random key

# Global variable to store dataframe (for simplicity)
df = None

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Upload route
@app.route('/upload', methods=['POST'])
def upload():
    global df
    file = request.files['file']
    if file:
        df = pd.read_csv(file)
        df.to_csv('uploaded.csv', index=False)  # Save to file
        session['uploaded'] = True
        return render_template('data.html', data=df.to_html(), stats=df.describe().to_html())
    return "No file uploaded"

# Data view
@app.route('/data')
def data():
    global df
    if df is None and os.path.exists('uploaded.csv'):
        df = pd.read_csv('uploaded.csv')
    if df is not None:
        return render_template('data.html', data=df.to_html(), stats=df.describe().to_html())
    return "No data uploaded"

# Visualize
@app.route('/visualize')
def visualize():
    global df
    if df is None and os.path.exists('uploaded.csv'):
        df = pd.read_csv('uploaded.csv')
    if df is not None:
        plots = []
        
        for col in df.columns:
            if df[col].dtype in ['int64', 'float64']:
                # Histogram for numeric
                fig = px.histogram(df, x=col, title=f'Histogram of {col}')
                plots.append(fig.to_html(full_html=False))
                # Box plot
                fig = px.box(df, y=col, title=f'Box Plot of {col}')
                plots.append(fig.to_html(full_html=False))
            elif df[col].dtype == 'object':
                # Bar chart for categorical
                value_counts = df[col].value_counts()
                fig = px.bar(x=value_counts.index, y=value_counts.values, title=f'Bar Chart of {col}')
                plots.append(fig.to_html(full_html=False))
        
        # Scatter plot if at least two numeric columns
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) >= 2:
            fig = px.scatter(df, x=numeric_cols[0], y=numeric_cols[1], title=f'Scatter Plot: {numeric_cols[0]} vs {numeric_cols[1]}')
            plots.append(fig.to_html(full_html=False))
        
        if not plots:
            plots = ["<p>No suitable data for visualization.</p>"]
        
        return render_template('visualize.html', plots=''.join(plots))
    return "No data uploaded"

# Predict
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    global df
    if df is None and os.path.exists('uploaded.csv'):
        df = pd.read_csv('uploaded.csv')
    if df is not None:
        if request.method == 'POST':
            target = request.form['target']
            features = request.form.getlist('features')
            if target in df.columns and all(f in df.columns for f in features):
                X = df[features]
                y = df[target]
                model = LinearRegression()
                model.fit(X, y)
                predictions = model.predict(X)
                df['predictions'] = predictions
                return render_template('predict.html', predictions=predictions[:10])  # Show first 10
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        return render_template('predict_form.html', columns=numeric_cols)
    return "No data uploaded"

# Download
@app.route('/download')
def download():
    global df
    if df is None and os.path.exists('uploaded.csv'):
        df = pd.read_csv('uploaded.csv')
    if df is not None:
        df.to_csv('results.csv', index=False)
        return send_file('results.csv', as_attachment=True)
    return "No data"

# Run app
if __name__ == '__main__':
    app.run(debug=True)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
from flask import Flask, render_template_string, send_file, request
import sqlite3
import pandas as pd
import plotly.express as px
from fpdf import FPDF
import io

app = Flask(__name__)

@app.route('/')
def dashboard():
    conn = sqlite3.connect('db/test_results.db')
    df = pd.read_sql_query("SELECT * FROM results", conn)
    conn.close()

    pie_fig = px.pie(df, names='status', title='Test Results Summary')
    pie_chart = pie_fig.to_html(full_html=False)

    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.date
    line_fig = px.line(df.groupby('date').size().reset_index(name='count'), x='date', y='count', title='Tests per Day')
    line_chart = line_fig.to_html(full_html=False)

    return render_template_string("""
    <html>
    <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
        <title>TestPilot Dashboard</title>
    </head>
    <body class="p-5">
        <h2 class="mb-4">TestPilot QA Dashboard</h2>
        <div class="mb-3">
            <a href="/download" class="btn btn-success">Download Test Report PDF</a>
        </div>
        <div class="row">
            <div class="col-md-6">{{ pie_chart | safe }}</div>
            <div class="col-md-6">{{ line_chart | safe }}</div>
        </div>
    </body>
    </html>
    """, pie_chart=pie_chart, line_chart=line_chart)

@app.route('/download')
def download_report():
    conn = sqlite3.connect('db/test_results.db')
    df = pd.read_sql_query("SELECT * FROM results", conn)
    conn.close()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="TestPilot - Test Report", ln=True, align='C')
    pdf.ln(10)
    for idx, row in df.iterrows():
        pdf.cell(200, 10, txt=f"{row['timestamp']} - {row['test_name']}: {row['status']}", ln=True)

    buffer = io.BytesIO()
    pdf.output(buffer)
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="TestPilot_Report.pdf")

if __name__ == '__main__':
    app.run(debug=True)

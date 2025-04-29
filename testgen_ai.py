from bs4 import BeautifulSoup
import requests

HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/bigcode/starcoder"
HUGGINGFACE_API_KEY = "YOUR_HUGGINGFACE_API_KEY_HERE"

def query_huggingface(prompt):
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {"inputs": prompt}
    response = requests.post(HUGGINGFACE_API_URL, headers=headers, json=payload)
    return response.json()[0]['generated_text']

def generate_test_from_html(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    prompt = f"""
    You are a senior QA automation engineer. 
    Generate Python Selenium test case code based on the given HTML page.
    HTML: {str(soup)[:3000]}
    """
    result = query_huggingface(prompt)
    print("\nGenerated Test Code:\n")
    print(result)

if __name__ == "__main__":
    generate_test_from_html("https://the-internet.herokuapp.com/login")

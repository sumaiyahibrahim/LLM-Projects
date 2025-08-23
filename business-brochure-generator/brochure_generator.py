import requests

def generate_brochure(company_name, website_text):
    prompt = f"""
    Create a professional brochure for the company '{company_name}' using the info below:
    
    Website Content:
    {website_text}

    Brochure should include:
    - About Us
    - Mission & Vision
    - Services or Products
    - Why Choose Us
    - Careers or Join Us
    """

    # OpenRouter API (you can swap with local LLaMA too)
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/mistral-7b-instruct",  
        "messages": [{"role": "user", "content": prompt}]
    }

    res = requests.post(url, headers=headers, json=data)
    return res.json()['choices'][0]['message']['content']
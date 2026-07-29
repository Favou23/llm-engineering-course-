import os
import json
from dotenv import load_dotenv
from IPython.display import Markdown, display, update_display
from scraper import fetch_website_links, fetch_website_contents
from openai import OpenAI

# Initialize and constants
load_dotenv()
OLLAMA_BASE_URL = "http://localhost:11434/v1"
api_key = os.getenv("OLLAMA_API_KEY")

if api_key and api_key.startswith("sk-proj-") and len(api_key) > 10:
    print("API key looks good so far")
else:
    print("There might be a problem with your API key? Please visit the troubleshooting notebook!")

MODEL = "qwen2.5:0.5b"
openai = OpenAI(base_url=OLLAMA_BASE_URL, api_key=api_key)

link_system_prompt = """You are an expert website analyst. Your task is to identify the pages that are most useful for creating a company brochure."""

def get_links_user_prompt(company_name, url):
    landing_page = fetch_website_contents(url)
    links = fetch_website_links(url)

    user_prompt = f"""
You are looking at a company called: {company_name}
The landing page URL is: {url}

Landing page content:
{landing_page}

Links found on the landing page:
{links}

Your task is to decide which links are relevant for creating a short brochure about the company.
Return only a JSON object with this structure:
{{"links": [{{"type": "about page", "url": "https://example.com/about"}}]}}"""
    return user_prompt[:5_000]

def select_relevant_links(url, company_name="the company"):
    print(f"Selecting relevant links for {url} by calling {MODEL}")
    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": link_system_prompt},
            {"role": "user", "content": get_links_user_prompt(company_name, url)},
        ],
        response_format={"type": "json_object"},
    )
    result = response.choices[0].message.content
    links = json.loads(result)
    print(f"Found {len(links.get('links', []))} relevant links")
    return links

def fetch_page_and_all_relevant_links(url, company_name="the company"):
    contents = fetch_website_contents(url)
    relevant_links = select_relevant_links(url, company_name)

    result = f"## Landing Page:\n\n{contents}\n\n## Relevant Links:\n"
    for link in relevant_links.get("links", []):
        link_type = link.get("type", "related page")
        link_url = link.get("url", "")
        result += f"\n\n### {link_type}\n"
        if link_url:
            result += fetch_website_contents(link_url)
        else:
            result += "[No URL provided]"

    return result

brochure_system_prompt = """
You are an assistant that analyzes the contents of several relevant pages from a company website
and creates a short brochure about the company for prospective customers, investors and recruits.
Respond in markdown without code blocks.
Include details of company culture, customers and careers/jobs if you have the information.
"""

def get_brochure_user_prompt(company_name, url):
    user_prompt = f"""
You are looking at a company called: {company_name}
Here are the contents of its landing page and other relevant pages;
use this information to build a short brochure of the company in markdown without code blocks.\n\n
"""
    user_prompt += fetch_page_and_all_relevant_links(url, company_name)
    user_prompt = user_prompt[:5_000]
    return user_prompt

def create_brochure(company_name, url):
    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": brochure_system_prompt},
            {"role": "user", "content": get_brochure_user_prompt(company_name, url)},
        ],
    )
    result = response.choices[0].message.content
    display(Markdown(result))

def stream_brochure(company_name, url):
    stream = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": brochure_system_prompt},
            {"role": "user", "content": get_brochure_user_prompt(company_name, url)},
        ],
        stream=True,
    )

    response = ""
    display_handle = display(Markdown(""), display_id=True)
    for chunk in stream:
        response += chunk.choices[0].delta.content or ""
        update_display(Markdown(response), display_id=display_handle.display_id)

if __name__ == "__main__":
    select_relevant_links("https://edwarddonner.com", company_name="Edward Donner")
    create_brochure("HuggingFace", "https://huggingface.co")

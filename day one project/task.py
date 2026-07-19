"""in this little project, i will build a website sumarizer.
what it does is that it takes a url, red the content of the website and then passed 
through an lmm and then the summary of the website is passed out as an output"""

## first of all i want to define a function that chains the message to the llm 


website_content = """a function that has already scraped the data of a web 
using the desired url as a parameter"""

def message_for_the_llm(website_content):
    [
        {"role":"system", "content":"youre a professioinal software engineer"},
        {"role":"user", "content": "summarize the content of this website and tell if theres any useful information about software engineering" + website_content}
    ]
    return





content_of_the_website = """    (scraped).....a function that already scraped a webpage by taking in the 
url of the desired webpage as a parameter"""

"""for example:
scraped  =scrape_web_content(url)"""

"""where scrape_web_content(), is the scrapinf function defined in another file """
def scrape_web_content(url):
    return(...)


def message_for_llm(content_of_the_website):
    return[
        {"role": "system", "content":"youre a professioinal software engineer"},
        {"role": "user", "content":"summarize the content of thiswebpage and also tell if the total content is software engiineering relates" + content_of_the_website}
    ]
    

def summarize(url):
    website = scrape_web_content(url)
    response = openai.chat.completions.create(
        model = "gpt-4o-mini", messages = message_for_llm(website)
    )
    return response.choices[0].message.content
    
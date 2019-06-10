import urllib.request, json
from .models import Quote

api_key = None

def configure_request(app):
    global api_key
    api_key = app.config['QUOTES_API_KEY']

def get_random_quote():
    
    with urllib.request.urlopen(api_key) as url:
        raw_data = url.read()
        quote_json = json.loads(raw_data)
        response_result = None
        if quote_json:
            qoute_item = quote_json
            response_result = process_data(qoute_item)
    return response_result

def process_data(quotes_list):
    
    final_quote = []
    quote = quotes_list['quote']
    author = quotes_list['author']
    new_quote = Quote(quote, author)
    print('PROCESSED QUOTE',new_quote)
    final_quote.append(new_quote)
    return final_quote
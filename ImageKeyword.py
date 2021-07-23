import requests
from credentials import client_id, secret

def ImageKeywordGenerator(img_path, minimum_score=0.40):
    
    with open(img_path, 'rb') as img:
        data = {'data': img}
        keywords = requests.post('https://api.everypixel.com/v1/keywords', files=data, 
                                    auth=(client_id, secret)).json()

    keyword_score, status = list(keywords.values())
    only_keywords = []

    if status == 'ok':
        for keywords in keyword_score:
            if keywords['score'] > minimum_score:
                only_keywords.append(keywords['keyword'])
    
    return only_keywords

print(ImageKeywordGenerator("img.jpg", minimum_score=0.80))

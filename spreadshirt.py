import requests
import json

class Spreadshirt:
    def __init__(self, api_key, shop_id):
        self.header={
            "Authorization": 'SprdAuth apiKey="' + api_key + '"', 
            "User-Agent": 'ShopApiExampleIntegration-1.0'
        }
        self.url = 'https://api.spreadshirt.net/api/v1/shops/' + shop_id + '/'
        self.mediaType = 'json'

    def get_sellables(self, page):
        r = requests.get( 
            self.url + 'sellables/?mediaType=' + self.mediaType + '&page=' + str(page), 
            headers=self.header
        )
        return json.loads(r.text)

    def get_sellable(self, sellable_id, idea_id, appearance_id):
        r = requests.get( 
            self.url + 'sellables/' + sellable_id + '/?ideaId=' + idea_id + '&appearanceId=' + appearance_id + '&mediaType=' + self.mediaType , 
            headers=self.header
        )
        return json.loads(r.text)

    def get_departments(self):
        r = requests.get( 
            self.url + 'productTypeDepartments?mediaType=' + self.mediaType + '&fullData=true', 
            headers=self.header
        )
        return json.loads(r.text)

# -*- coding: utf-8 -*-

import requests




def find_pet_by_tag(tag):
    params = {'tags': tag}
    headers = {
        'Accept': 'application/xml'
        # 'Accept': 'application/json'
    }
    url = 'http://petstore.swagger.io/v2/pet/findByTags'
    url_1 = 'https://petstore.swagger.io/v2/pet/1'
    url_2 = 'http://vk.com/feed'
    r = requests.get(url_2, params=params, headers=headers)
    print(r.status_code, r.headers)
    print(r.content)

    # s = 'http://petstore.swagger.io/v2/pet/89?tags=string&filter=sad'


if __name__ == '__main__':
    #get_habrahabr()
    find_pet_by_tag('string')
import json

arr = []

with open('badwords_list.txt', encoding='utf-8') as r:
    for i in r:
        n = i.lower().split('\n')[0]
        if n != '':
            arr.append(n)

with open('badwords.json', 'w', encoding='utf-8') as e:
    json.dump(arr, e)
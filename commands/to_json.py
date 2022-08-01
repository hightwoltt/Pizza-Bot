import json

arr = []

with open('badwords_list.txt', encoding='utf-8') as r:
    for badword in r:
        badword = badword.lower().split('\n')[0]
        if badword != '':
            arr.append(badword)

with open('badwords.json', 'w', encoding='utf-8') as e:
    json.dump(arr, e)
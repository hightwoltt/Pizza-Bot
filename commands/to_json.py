import json

arr = []

# Function that reads a list of obscene words
with open('badwords_list.txt', encoding='utf-8') as r:
    for badword in r:
        badword = badword.lower().split('\n')[0]
        if badword != '':
            arr.append(badword)
            
# Create obscene words JSON
with open('badwords.json', 'w', encoding='utf-8') as e:
    json.dump(arr, e)
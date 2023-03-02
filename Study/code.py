import json
import csv

dict_total = dict()
dict1 = dict(name=None, surname=None, best_score=None, date_and_time=None, email=None)
list1 = []
with open('exam_results.csv', 'r', encoding='utf-8') as f:
    for name, surname, score, date, email in csv.reader(f):
        dict_temp = dict(name=name, surname=surname, best_score=score, date_and_time=date, email=email)
        list1.append(dict1 | dict_temp)

print(list1)
with open('best_scores.json', 'w', encoding='utf-8') as f1:
    f1.write(json.dumps(list1, indent=3))

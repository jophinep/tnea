import json
import re
from uuid import uuid4

with open("raw_colleges.txt") as f:
    data = f.readlines()

with open("raw_all_colleges.txt") as f:
    all_data = f.readlines()

franks = json.load(open("formatted_ranks.json"))
codes = json.load(open("new_codes.json"))

collname = ""
colleges = []
courses = []
new_ranks = []
dummy_ranks = {
    "OC": 999999999999,
    "BC": 999999999999,
    "BCM": 999999999999,
    "MBC": 999999999999,
    "SC": 999999999999,
    "SCA": 999999999999,
    "ST": 999999999999
}

for j in data:
    i = j.strip()
    coll_pattern = r"^\d{4} .+$"
    if collname:
        collname += i
        if i[-6:].isnumeric():
            colleges.append(collname.split(' ', 1))
            collname = ""
        continue
    if re.match(coll_pattern, i):
        collname = i
        if i[-6:].isnumeric():
            colleges.append(collname.split(' ', 1))
            collname = ""

rcourse = False
coll_course = []
for j in data:
    i = j.strip()
    if i.startswith("Valid Upto"):
        rcourse = True
        continue
    if i.startswith("Hostel Facilities"):
        courses.append(coll_course)
        coll_course = []
        rcourse = False
        continue
    if rcourse:
        d = i.split()
        try:
            coll_course.append([d[1], d[2]])
        except IndexError:
            print(i)
            raise


print(len(colleges))
print(len(courses))


for i in range(len(colleges)):
    for j in courses[i]:
        try:
            rank = {
                "_id": str(uuid4()).replace('-', ''),
                "coc": colleges[i][0].zfill(4),
                "con": colleges[i][1],
                "brc": j[0],
                "brn": codes.get(j[0], ""),
                **dummy_ranks
            }
            rank = franks[colleges[i][0]][j[0]]
        except KeyError:
            pass
        new_ranks.append(rank)

json.dump(new_ranks, open("new_ranks.json", "w"), indent=4)

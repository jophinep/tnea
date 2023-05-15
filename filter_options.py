import csv
import json

cutoff = json.load(open("new_cutoff.json"))
ranks = json.load(open("ranks.json"))
rank_index = {f'{r["coc"]}{r["brc"]}': r for r in ranks}
courses = json.load(open("new_courses.json"))
my_cutoff = 0

options = []
headers = ["College Code", "College Name", "District", "Branch Code", "Branch Name", "Cutoff OC", "Cutoff MBC", "Rank OC", "Rank MBC"]
with open("colleges.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    for c in cutoff:
        brc = c['brc']
        oc = c['OC']
        mbc = c['MBC']
        if brc in courses.keys() and ((oc and oc > my_cutoff) or (mbc and mbc > my_cutoff)):
            option = {
                "College Code": c["coc"],
                "College Name": c["con"],
                "District": c["District"],
                "Branch Code": c["brc"],
                "Branch Name": c["brn"],
                "Cutoff OC": c["OC"],
                "Cutoff MBC": c["MBC"],
                "Rank OC": rank_index[f'{c["coc"]}{c["brc"]}']["OC"],
                "Rank MBC": rank_index[f'{c["coc"]}{c["brc"]}']["MBC"]
            }
            options.append(option)
            writer.writerow(option)

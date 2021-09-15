import csv
import json

ranks = json.load(open("new_ranks.json"))
courses = json.load(open("new_courses.json"))
my_rank = 68000

options = []
headers = ["College Code", "College Name", "District", "Branch Code", "Branch Name", "OC", "MBC"]
with open("colleges.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    for rank in ranks:
        brc = rank['brc']
        oc = rank['OC']
        mbc = rank['MBC']
        if brc in courses.keys() and ((oc and oc > my_rank) or (mbc and mbc > my_rank)):
            option = {
                "College Code": rank["coc"],
                "College Name": rank["con"],
                "District": rank["District"],
                "Branch Code": rank["brc"],
                "Branch Name": rank["brn"],
                "OC": rank["OC"],
                "MBC": rank["MBC"],
            }
            options.append(option)
            writer.writerow(option)

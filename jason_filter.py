import json

fields_to_keep = ["_id", "coc", "con", "brc", "brn", "OC", "BC", "BCM", "MBC", "SC", "SCA", "ST"]

input_file = "ranks_2023.json"
with open(input_file, "r") as f:
    data = json.load(f)

filtered_data = [
    {key: entry[key] for key in fields_to_keep if key in entry}
    for entry in data
]

output_file = "output.json"
with open(output_file, "w") as f:
    json.dump(filtered_data, f, indent=4)

print(f"Filtered data  {output_file}")

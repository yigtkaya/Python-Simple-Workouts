import json
file_name = input("Json file name: ")
with open(file_name, "r+") as f:
    data = json.load(f)

    for person in data:
        for k in person:
            if person[k] == "":
                person[k] = None
    f.seek(0)
    json.dump(data, f)
    f.truncate()
    
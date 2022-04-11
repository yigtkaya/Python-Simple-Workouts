import pandas as pd
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from dateutil.parser import parser

## variables
format = "%d-%m-%Y"  ## datetime format // string format
df = pd.read_feather("problem-2.ftr")
datesFromFtr = df.values
count = 0
string_date_list = []

# changing ndarray to normal str
for j in datesFromFtr:
    string_date_list.append(", ".join(j))


# is str a date?
def isDate(date_text):
    try:
        res = bool(parser().parse(date_text))
        return res
    except ValueError:
        return False


# update the str to wanted form

def update(dates, last_date_index):
    for i in range(len(dates)):
        if isDate(dates[i]):
            last_date_index += 1
        else:

            if dates[i] == "Vandaag":
                temp = datetime.today()
                dates[i] = temp.strftime(format)

            elif "weken" in dates[i]:
                week = dates[i].split(" ")
                weeks_count = int(week[0])
                temp = datetime.strptime(dates[last_date_index - 1], format)
                temp -= relativedelta(weeks=weeks_count)
                dates[i] = temp.strftime(format)
            else:
                months = dates[i].split(" ")
                months_count = int(months[0].replace("+", ""))
                temp = datetime.strptime(dates[last_date_index - 1], format)
                temp -= relativedelta(months=months_count)
                dates[i] = temp.strftime(format)


# write to file
def writeToFile(date_array, file_name):
    with open(file_name, "w") as f:
        for d in date_array:
            f.write(f'{str(d)}\n')


def convertToDateObj(arr):
    for a in arr:
        a = datetime.strptime(a, format)
    return arr


update(string_date_list, count)
writeToFile(convertToDateObj(string_date_list), "problem-2-updated.ftr")

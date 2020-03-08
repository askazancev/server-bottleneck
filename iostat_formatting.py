# Server-bottleneck
#
# Script for formatting data from iostat command output to csv format.
# May be useful with linux-based performance analysis
#
# Author: Aleksei Kazancev
# email: aleksei.kazancev@mail.ru

# How to use
# Firstly you should get raw data from server via cmd: iostat -x 1 > raw_data.log
# Put the raw_data.log in same folder with script
# Execute and check the result at raw_data_formatted.csv
# Open raw_data_formatted.csv in Excel or Google Tab, build diagrams and analysis its.

import re

# regex for searching data by pattern
digits_p = re.compile("([0-9]+,[0-9]+)")
disk_p = re.compile("sd[a-z]|nvm[\\S]+")
description_p = re.compile("(?<= )[a-zA-Z%_/-]+")

flag_first_sec = True
flag_new_cpu = False
delimiter = ";"
data = []

with open("raw_data.log") as file:
    for i, line in enumerate(file):
        matched = []
        # Filling first line for description of columns
        if flag_first_sec:
            if re.match("avg-cpu", line):
                matched.append("num")
                for match in re.finditer(description_p, line):
                    matched.append(match.group())
                s = delimiter.join(matched)
                data.append(s)
            if re.match("Device", line):
                flag_first_sec = False
                k = 0
                for j, dLine in enumerate(open('raw_data.log')):
                    matched = []
                    dName = re.search(disk_p, dLine)
                    if dName is not None:
                        for match in re.finditer(description_p, line):
                            matched.append(dName.group() + "-" + match.group())
                        s = delimiter.join(matched)
                        data[0] += delimiter + s
                        k += 1
                    elif k != 0:
                        break
        if re.match("avg-cpu", line):
            flag_new_cpu = True
            continue
        if flag_new_cpu:
            # append a number of second as first symbol of line
            matched.append(str(len(data)))
            for match in re.finditer(digits_p, line):
                matched.append(match.group())
            s = delimiter.join(matched)
            data.append(s)
            flag_new_cpu = False
        if re.match(disk_p, line):
            for match in re.finditer(digits_p, line):
                matched.append(match.group())
            s = delimiter.join(matched)
            data[len(data) - 1] += delimiter + s

with open("raw_data_formatted.csv", "w") as f:
    for line in data:
        f.write("%s\n" % line)
    print("Done! %d lines were prepared." %(len(data)-1))

# Напишите программу для печати всех уникальных значений в словаре.
# [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
# {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# ->  {'S005', 'S002', 'S007', 'S001', 'S009'}

startDictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
                   {"VII": " S005 "}, {" V ": " S009 "}, {" VIII ": " S007 "}]


listValues = set()
for i in startDictionary:
    for j in i.values():
        listValues.add(j)
print(listValues)

records = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']

wrong_records =[]
correct_records = []
corrected_records = []

for record in records:
#   print(record)
    split_record = record.split(' ')
#   print(split_record)
    if split_record[0].islower() or split_record[1].islower():
        wrong_records.append(record)
        corrected_records.append(split_record[0].capitalize() + ' ' + split_record[1].capitalize())
    else:
        correct_records.append(record)
        corrected_records.append(record)

print(wrong_records)
print(correct_records)
print(corrected_records)





#records = []
#for first_name in 'pepa', 'Jiří', 'Ivo', 'jan':
#    for last_name in list['novák', 'Sládek', 'navrátil', 'Poledník']
#    records.append(first_name + last_name)
#print(records)

#for name in zaznamy:
 #   wrong_name = name.islower() or 
    
    
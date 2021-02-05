import csv

def vcfWriter(name, email, phone, category):
    vcfLines = []
    vcfLines.append('BEGIN:VCARD')
    vcfLines.append('VERSION:4.0')
    vcfLines.append('FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:%s' %  name)
    vcfLines.append('EMAIL:%s' % email)
    vcfLines.append('TEL:%s' % phone)
    vcfLines.append('CATEGORIES:%s' % category)
    vcfLines.append('END:VCARD')
    vcfString = '\n'.join(vcfLines) + '\n'
    print("Creating vCard with these information:\n{}".format(vcfString))
    return vcfString.encode("utf-8")

# Change this ti the path of your CSV file
contacts_file_path = "C:\\Users\\argha\\Desktop\\Create-Arabic-vCard\\Create-Arabic-vCard\\contacts.csv"

# Chage this to where you would like to save your vCards output
output_path = "C:\\Users\\argha\\Desktop\\Create-Arabic-vCard\\Create-Arabic-vCard\\contacts_files\\"
    # Get data from the CSV file
with open(contacts_file_path, "r", encoding='utf-8') as csvFile:
    csvReader = csv.reader(csvFile)
    csvData = list(csvReader)

    # Iterate over the lines of the CSV table
    for row in range(len(csvData)):
        if row == 0:
            continue # Skip the first row (headers)
        else:
            # Get contact data from current row
            # (Tweak the column indexes to fit your data)
            name = csvData[row][0]
            email = csvData[row][1]
            phone = csvData[row][2]
            category = csvData[row][3]

            # Write the corresponding vCard string to a .vcf file:
            outputFile = open(output_path + name + '.vcf', 'wb')
            outputFile.write(vcfWriter(name, email,  phone, category))
            outputFile.close()

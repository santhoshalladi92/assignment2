import csv
reader = csv.reader(open('a2.csv', 'r'), delimiter=',')
f = open('a2.xml', 'w')
f.write('<?xml version="1.0" encoding="UTF-8"?>' + "\n")
f.write('<students>'  + "\n")

flag = 0
for row in reader:
    if flag == 0:
        flag = 1
    else:
        f.write('<student>'  + "\n")
        f.write('<yearOfJoining>'+row[0]+'</yearOfJoining>'  + "\n")
        f.write('<CollID>'+row[1]+'</CollID>'  + "\n")
        f.write('<GradType>'+row[2]+'</GradType>'  + "\n")
        f.write('<name>' + "\n")
        f.write('<fName>'+row[3]+'</fName>' + "\n")
        f.write('<lName>'+row[4]+'</lName>' + "\n")

        f.write('</name>' + "\n")
        f.write('<GuardianName>'+row[5]+'</GuardianName>' + "\n")

        f.write('<dob>'+row[6]+'</dob>' + "\n" )

        f.write('<branch>' + "\n")
        f.write('<branch1>'+row[7]+'</branch1>' + "\n")
        f.write('<branch2>'+row[8]+'</branch2>' + "\n")
        f.write('</branch>' + "\n")

        f.write('<contact>' + "\n")
        f.write('<personalContact>'+row[9]+'</personalContact>' + "\n")
        f.write('<parentContact>'+row[10]+'</parentContact>' + "\n")
        f.write('</contact>' + "\n")

        f.write('<mail>' + "\n")
        f.write('<officialMail>'+row[11]+'</officialMail>' + "\n")
        f.write('<otherMail>'+row[12]+'</otherMail>' + "\n")
        f.write('</mail>' + "\n")
        f.write('<hostelRoom>'+row[13]+ '</hostelRoom>' + "\n")
        f.write('<address>' + "\n")
        count=0
        word=''
        for charac in row[14]:
            if charac==',':
                f.write('<line')
                f.write(str(count))
                f.write('>'+word+'</line')
                f.write(str(count))
                f.write('>' + "\n")
                count= count+1
                word=''
            else:
                word= word+charac
        f.write('<line')
        f.write(str(count))
        f.write('>'+word+'</line')
        f.write(str(count))
        f.write('>' + "\n")
        f.write('</address>' + "\n")
        f.write('<cgpa>'+row[15]+'</cgpa>' + "\n")
        f.write('<courses>' + "\n")
       # count=0
        word=''
        for charac in row[16]:
            if charac==',':
                f.write('<course')
               # f.write(str(count))
                f.write('>'+word+'</course')
               # f.write(str(count))
                f.write('>' + "\n")
              #  count= count+1
                word=''
            else:
                word= word+charac
        f.write('<course')
       # f.write(str(count))
        f.write('>'+word+'</course')
       # f.write(str(count))
        f.write('>' + "\n")
        f.write('</courses>' + "\n")
        f.write('</student>' + "\n\n")
f.write('</students>')
f.close()


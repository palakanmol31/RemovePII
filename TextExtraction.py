##### to extract the data and tag them, then calculate the total count .
### u need to download standford ner tool for this
### @palakanmol

import glob
import re
import os
import pycountry

person = 0
orga = 0
location = 0
credit = 0
phone = 0
zip = 0
email = 0
ssn = 0
country = 0

def check_creditCard(tag):
    parts = re.split(' |-', tag)

    if len(parts) == 1:
        if len(parts[0]) != 16:
            # print 'Credit card does not consist of 16 digits.'
            return False
    elif len(parts) == 4:
        if not all(len(part) == 4 for part in parts):
            # print 'Credit card does not consist of 4 blocks of 4 digits each.'
            return False
    else:
        # print 'Credit card consists of an invalid number of blocks.'
        return False

    if not all(part.isdigit() for part in parts):
        # print 'Credit card does not only contain digits.'
        return False

    return True
pass


def check_tag(tag):
   # print "IN CHECK"
    global credit,email,ssn,phone,country
    if check_creditCard(tag) == True :
       # print "IN CREDIT CARD"
        credit = credit + 1
        return 'CREDIT CARD'

    elif check_email(tag) == True :
        email = email + 1
        return 'EMAIL'

    elif check_ssn(tag) == True :
        ssn += 1
        return 'NATIONAL IDENTITY NUMBER'

    elif check_phone(tag) == True :
        phone = phone + 1
        return 'PHONE NUMBER'

    elif check_country(tag) == True :
        country = country + 1
        return 'ZIP CODE'

    else :
        return '0'


pass

def check_email(email):
    #email = raw_input("enter the mail address::")
    match = re.search(r'[\w.-]+@[\w.-]+.\w+', email)
    if match:
        return True
    else:
        return False
pass


def check_ssn(ssn):
    #ssn = raw_input("enter the ssn::")
    match = re.search('^\d{3}-?\d{2}-?\d{4}$|^XXX-XX-XXXX$', ssn)

    if match:
        return True
    else:
        return False

pass

def check_country (tag) :
    country = set()
    for x in pycountry.countries:
        country.add(x.name)

    #print country

    return tag in country

def check_phone(phone):

    match = re.search('^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$', phone)

    if match:
        return True
    else:
        return False

pass

def main() :
    directory = 'Data/Output'
    if not os.path.exists(directory):
        os.makedirs(directory)
    global person,location,orga

    from nltk.tag import StanfordNERTagger
    stanford_ner_dir = 'stanford-ner-2016-10-31/'
    eng_model_filename= stanford_ner_dir + 'classifiers/english.all.3class.distsim.crf.ser.gz'
    my_path_to_jar= stanford_ner_dir + 'stanford-ner.jar'

    st = StanfordNERTagger(model_filename=eng_model_filename, path_to_jar=my_path_to_jar)
    txt_list = glob.glob("Data/Enron_txt/*.txt")
    #file_path ='Data/Enron_txt/folder_report_dasovich-j_All Documents.txt'
    for file_path in txt_list:
        print file_path
        result = st.tag(open(file_path,'r').read().replace('\n',' ').split())
        result= st.tag(open(file_path,'r').read().replace(',',' ').split())
        file = open('Data/Output/'+os.path.basename(file_path).split(".")[0]+'_output.txt',"w")

        for x in result :
            #try :
                a = x[0]
                b = x[1]
                if b == 'PERSON' :
                    person = person + 1
                elif b == 'LOCATION' :
                    location = location + 1
                elif b == 'ORGANIZATION':
                    orga = orga +  1
                elif b == 'O' :
                     b = check_tag(x[0])
                file.write(a + '  ' + b + '\n')
        file.close()


main()
count_file = open('Data/count.txt',"w")
count_file.write('Person - ' + str(person)+ '\n')
count_file.write('Location - ' + str(location)+ '\n')
count_file.write('Organization - ' + str(orga)+ '\n')
count_file.write('Credit_Card  - ' + str(credit)+ '\n')
count_file.write('Email - ' + str(email)+ '\n')
count_file.write('National Identity Number - ' + str(ssn)+ '\n')
count_file.write('Phone - ' + str(phone) + '\n')
count_file.write('Country - ' + str(country) + '\n')
count_file.close()






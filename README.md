# RemovePII
## Algorithm
The code is implemented using 3 parts. Firstly we will pass it through a function to get raw
extracted data from PST files. Next we will used information extraction to convert raw data into
words. After getting words we will assign them to different classes they belong to.

## Dataset Used
The dataset used by us is EDRM Enron Email Data Set https://archive.org/details/edrm.enron.email.data.set.v2.xml . This dataset consists of :
1. 1.3 million email messages and attachments from former Enron staff.
2. 168 Microsoft Outlook .PST files
3. Almost 40 GB of data

## Results
Towards the end of the algorithm following are the PII’s that we are able to extract from a raw text
document:
1. Name
2. Location
3. Organization
4. Credit-card number
5. National Identity Number
6. Email
7. Phone Number
8. Country Name

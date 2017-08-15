# To convert pst data to text file
## Tested this file on Enron Dataset ... To download data : https://enrondata.readthedocs.io/en/latest/
#### @palakanmol
##
###########################
import os
import glob
import pypff
import unicodecsv as csv



def folderTraverse(base,filename) :
    #print base
    for folder in base.sub_folders:
        if folder.number_of_sub_folders:
            folderTraverse(folder,filename)  # Call new folder to traverse
        checkForMessages(folder,filename)


def checkForMessages(folder,filename):


      #logging.debug("Processing Folder: " + folder.name)
      message_list = []
      for message in folder.sub_messages:
            message_dict = processMessage(message)

            message_list.append(message_dict)
      folderReport(message_list, folder.name,filename)



def processMessage(message):
    return {
     "subject": message.subject,
     "sender": message.sender_name,
     "header": message.transport_headers,
      "body": message.plain_text_body,
    # "creation_time": message.creation_time,
    #"submit_time": message.client_submit_time,
    #"delivery_time": message.delivery_time,
    #"attachment_count": message.number_of_attachments, }
    }



def makePath(file_name):
    output_directory = "Data/Enron_txt"
    return os.path.abspath(os.path.join(output_directory, file_name))
    pass


def folderReport(message_list, folder_name,filename):

    #if not len(message_list):
     #   logging.warning("Empty message not processed")
      #  return
   
    fout_path = makePath("folder_report_" + filename + "_" + folder_name + ".txt")

    fout = open(fout_path, 'wb')
    header = ['subject','sender','header','body']

    csv_fout = csv.DictWriter(fout, fieldnames=header, extrasaction='ignore')
    csv_fout.writeheader()
    csv_fout.writerows(message_list)

    fout.close()


#fn = os.path.join(os.path.dirname(__file__), '/Data/EnronDataOrg_AED_Mailbox-PSTs_20090122/*.pst')
directory = 'Data/Enron_txt'
if not os.path.exists(directory):
    os.makedirs(directory)
pst_list = glob.glob("Data/Enron/*.pst")
for pst_file in pst_list :
    pst_name = os.path.split(pst_file)[1].split('.')[0]
    print pst_name
    opst = pypff.open(pst_file)
    root = opst.get_root_folder()
    folderTraverse(root,pst_name)





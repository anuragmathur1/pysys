#View the full MyBackup class in /home/user/pylabs/mybackup.py

#Review the check_zipfile() and check_directory() methods. Understand what they do and what they return.

#Create your own backup script using the MyBackup Class that:

#Takes the backup directory and zipfile name as arguments when you call it (Hint: use sys.argv[]) .
#Checks to see if the directory exits using the check_directory() method and exits if it does not.
#Checks to see if the zipfile already exists using the check_zipfile() method.
#Logs messages for script status.
#Prints the filenames added to the zipfile to the log.
#Solution script found in /home/user/pylabs/solution.py

import sys
from mybackup import MyBackup
import zipfile
import os
import logging
import glob

backup_dir = sys.argv[1]
zipfile_name = sys.argv[2]

logging.basicConfig(filename = "mybkup.log",
                    format = '%(asctime)s- %(levelname)s: %(message)s',
                    level = logging.DEBUG)

logging.info("Creating the Nackup Object !!")
bkupobj = MyBackup()

logging.info("Checking if the backup directory %s  exists" % backup_dir)
if not bkupobj.check_directory(backup_dir):
    logging.error("Backup Directory %s does not exist. Exiting!! " % backup_dir)
    sys.exit()
else:
    bkupobj.dir_to_backup = backup_dir
    logging.info("Backup Directory %s exists. Moving on !!" % backup_dir)

if not bkupobj.check_zipfile(zipfile_name):
    logging.error("Zip file %s does not exist" % zipfile_name )
    logging.info("Creatin the new file now !! ")
    
logging.info("Backing up the directory !!")

for name in glob.glob(bkupobj.dir_to_backup):
    logging.info("Backing up the following file : %s" % zipfile_name)
bkupobj.zip_directory()


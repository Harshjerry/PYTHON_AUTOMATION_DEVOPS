import os 
from collections import Counter
import datetime
import smtplib

#read log from  a  directory
# extract error and warning messages

#count occcurences of each error and warning
log_directory = "./logs"
error_counter=Counter()
warning=0
error=0
files_in_log_directory = os.listdir(log_directory)
for file in files_in_log_directory:
    file_path = os.path.join(log_directory, file)
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
           line=line.strip()
           if "ERROR" in line:
               error += 1
               msg = line.split("ERROR")[-1].strip()
               error_counter[msg] += 1
               
           elif "WARNING" in line:
               warning += 1 


#sav   summary report of errors and warning in a file 
report_name="report.txt"
with open(report_name, "w") as report_file:
    report_file.write(f"Log Analysis Report - {datetime.datetime.now()}\n")
    report_file.write(f"Total Errors: {error}\n")
    report_file.write(f"Total Warnings: {warning}\n\n")
    report_file.write("Error Details:\n")
    for error_msg, count in error_counter.items():
        report_file.write(f"{error_msg}: {count} occurrences\n")
# send email alert if any critical error is found in the log'

# if error >threshold:
#     sender_email = "harshdeep1043@gmail.com"
#     receiver_email = "devjerry04@gmail.com"
#     subject = "Critical Error Alert"
#     body = f"Critical error detected in logs. Total Errors: {error}"
#     email_message = f"Subject: {subject}\n\n{body}"
#     with smtplib.SMTP("smtp.gmail.com", 587) as server:
#         server.starttls()
#         server.login(sender_email, "your_password")
#         server.sendmail(sender_email, receiver_email, email_message)



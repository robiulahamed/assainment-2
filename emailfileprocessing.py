import re
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

   



try:
    with open('email.txt','r') as email_file:
        email_list = email_file.readlines()
        valid_emails = []
        invalid_emails = []

        for i in  email_list:
            i=email.strip()
            if is_valid_email(i):
                valid_emails.append(i)
            else:
                invalid_emails.append(i)


        with open('valid_emails .txt','w') as valid_file: 
            for i in valid_emails:
                valid_file.write(i + '/n')

        with open('invalid_emals.txt','w') as invalid_file:
            for i in invalid_emails:
                invalid_file.write( i + '/n')

    print("emaols validated and written to files succcessfully. ")   
except FileNotFoundError:
    print("Error: The input file 'email.txt' does not exist.")

except PermissionError:
    print("Error: Permission denied to open the input file.")

except Exception as e:
    print("An error occurred:", str(e))    


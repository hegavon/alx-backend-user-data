Project: Handling Personal Data
Overview
This project demonstrates how to handle personal data securely and efficiently in Python. The tasks cover various aspects of data handling, including obfuscation of sensitive information in logs, creating custom log formatters, setting up secure database connections, and encrypting passwords. The goal is to ensure that sensitive data is protected at all stages of processing.

Learning Objectives
By the end of this project, you should be able to:

Identify examples of Personally Identifiable Information (PII).
Implement a log filter that obfuscates PII fields.
Encrypt passwords and validate their correctness.
Authenticate to a database using environment variables.
Requirements
All scripts should be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
All files should end with a new line.
The first line of all scripts should be #!/usr/bin/env python3.
A README.md file at the root of the project directory is mandatory.
Code should follow the pycodestyle style (version 2.5).
All files must be executable.
All modules should have documentation.
All classes should have documentation.
All functions should have documentation and type annotations.
Tasks
0. Regex-ing
Task: Write a function called filter_datum that returns an obfuscated log message.

Arguments:

fields: list of strings representing fields to obfuscate.
redaction: string to replace field values.
message: log line string.
separator: character separating fields in the log line.
Requirements:

Use re.sub to perform the substitution with a single regex.
Example Usage:

python
Copy code
fields = ["password", "date_of_birth"]
messages = [
    "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;",
    "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"
]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))
Output:

scss
Copy code
name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;
name=bob;email=bob@dylan.com;password=xxx;date_of_birth=xxx;
1. Log Formatter
Task: Update the RedactingFormatter class to obfuscate specified fields in log records.

Requirements:
Accept a list of fields in the constructor.
Use filter_datum to obfuscate values in log records.
Example Usage:

python
Copy code
message = "name=Bob;email=bob@dylan.com;ssn=000-123-0000;password=bobby2019;"
log_record = logging.LogRecord("my_logger", logging.INFO, None, None, message, None, None)
formatter = RedactingFormatter(fields=("email", "ssn", "password"))
print(formatter.format(log_record))
Output:

css
Copy code
[HOLBERTON] my_logger INFO 2019-11-19 18:24:25,105: name=Bob; email=***; ssn=***; password=***;
2. Create Logger
Task: Implement get_logger to return a configured logging.Logger object.

Requirements:
Logger named "user_data".
Logs up to logging.INFO level.
Uses RedactingFormatter with PII fields.
Example Usage:

python
Copy code
logger = get_logger()
logger.info("User data log message.")
3. Connect to Secure Database
Task: Implement get_db to connect to a secure database using environment variables.

Environment Variables:
PERSONAL_DATA_DB_USERNAME
PERSONAL_DATA_DB_PASSWORD
PERSONAL_DATA_DB_HOST
PERSONAL_DATA_DB_NAME
Example Usage:

python
Copy code
db = get_db()
cursor = db.cursor()
cursor.execute("SELECT COUNT(*) FROM users;")
for row in cursor:
    print(row[0])
cursor.close()
db.close()
4. Read and Filter Data
Task: Implement a main function to retrieve and display filtered user data from the database.

Filtered Fields:
name
email
phone
ssn
password
Example Usage:

python
Copy code
if __name__ == "__main__":
    main()
5. Encrypting Passwords
Task: Implement hash_password to hash and salt passwords using bcrypt.

Example Usage:

python
Copy code
password = "MyAmazingPassw0rd"
hashed_password = hash_password(password)
print(hashed_password)
Output:

swift
Copy code
b'$2b$12$Fnjf6ew.oPZtVksngJjh1.vYCnxRjPm2yt18kw6AuprMRpmhJVxJO'
6. Check Valid Password
Task: Implement is_valid to validate passwords against hashed passwords using bcrypt.

Example Usage:

python
Copy code
hashed_password = hash_password("MyAmazingPassw0rd")
is_valid_password = is_valid(hashed_password, "MyAmazingPassw0rd")
print(is_valid_password)
Output:

graphql
Copy code
True
Repository Structure
css
Copy code
alx-backend-user-data/
├── 0x00-personal_data/
│   ├── filtered_logger.py
│   ├── encrypt_password.py
│   ├── main.py
│   ├── user_data.csv
│   ├── README.md
How to Run
Clone the repository:
bash
Copy code
git clone <repository_url>
cd alx-backend-user-data/0x00-personal_data/
Make scripts executable:
bash
Copy code
chmod +x filtered_logger.py
chmod +x encrypt_password.py
chmod +x main.py
Set up the database:
bash
Copy code
cat main.sql | mysql -uroot -p
Run the main script:
bash
Copy code
./main.py

Conclusion
This project emphasizes the importance of protecting personal data through various methods such as data obfuscation, secure logging, environment variable management for database credentials, and password encryption. Following these practices ensures that sensitive information is handled responsibly and securely.
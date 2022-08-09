# Project topic: Hospital management system

## Project description:

There are eight types of users in this system: manager, doctor, patient, nurse, receptionist, pharmacy, accountant, laboratory
Each of these users will play an important role in the hospital management system.

### Admin user:

- This user is the most important user of the system.
- There is only one administrator in the system.
- The administrator can create user accounts for seven other users. It can also be according to the needs, delete the user account.
- The manager can control all the activities of the hospital, everything that happens in the hospital, is observable by the manager

### Registeration:

All users except the administrator must login to the system through the initial registration step.

The registration process for users has a form that includes the following sections and must be filled by users.

- Username: The user will be prompted to enter their full name.
- Password: This field is for secure account.
- Contact number: Asks the user for the numbers that are available.
- Email ID: This address is used to confirm users' membership in the system. When the process of registration was done correctly, an email with a unique ID for the user (can be related to the doctor, the patient, etc.) are sent to him (I didn't develope this email verification part)

### Login:

Each type of user must enter his unique ID, which was sent to him by email, along with his password. If both password and ID match the information, system will allow the user to log in

Forgot password section: If a user forgets his or her ID or password, it is enough to enter the email with which he registered in the system in the forgotten password section, then the system will send that email, password and user ID.

### Modifying profile information (edit):

It is not possible to receive all user's information during registration. Therefore, there is a section called information correction
that user will be able to fill some other important information that is important for some future communications.

This information includes: residential address, zip code, year of birth, age, gender, height and weight.

### Receptionist:

- This user keeps the time taken by the patients.
- Schedule of each doctor for users is visible. 
- The management of the time table is the responsibility of the receptionist.

### Accountants:

All hospital payment information and invoices are managed by the accountant.

### Pharmacy:

- All medicines and their information are managed by the pharmacy in the hospital.
- It can filter drugs based on their expiration date.
- When the patient submits the prescription, the pharmacy can provide the appropriate medicine for the mentioned patient to give


### Patient:

- The patient can make an appointment according to the doctor's timetable displayed by the receptionist
- The doctor confirmed the time and the patient will be notified via email.
- The patient can see his doctor's prescription through this system.
- If there are serious issues related to the patient, a bed will be assigned to that patient immediately. The patient can
See the information about the assigned bed.
- The patient can also send a private message to his doctor.

### Nurse:

A nurse is a doctor's assistant. The nurse helps the doctors in performing the operation. He takes the diagnostic report and gives it to the doctor.

### Laboratory:

Whenever a doctor issues a test for a patient, the laboratory performs these tests for the patient.
He keeps the prescription for the patient and passes it to the nurse.

### Doctor:

- The doctor is able to confirm or cancel appointments.
- If the doctor wants, he can cancel the appointment, which will be sent to the user via email.
- The doctor can see the history of medications that the patient has used.
- The doctor can communicate with the patient as a private message.

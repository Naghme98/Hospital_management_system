import mysql.connector

class Manager:

    def __init__(self):
        self.conn =mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Hospital")
        self.cursor = self.conn.cursor()

    def insert_user(self, name, password, phoneNumber, eemail, roleId, medicalCode, degree, delete):
        sql_u = "INSERT INTO user (name, password, phoneNumber, email, roleId) VALUES(%s, %s, %s, %s, %s)"
        val_u = (name, password, phoneNumber, eemail, roleId)
        self.cursor.execute(sql_u, val_u)
        user_id = self.cursor.lastrowid
        print("ddjdjdjdj    ",roleId)
        if roleId == 2:
            sql = "INSERT INTO patient (patientID) VALUES(%s)"
            val = (user_id)
            self.cursor.execute(sql, val)

        elif roleId == 3:
            sql = "INSERT INTO doctor (doctorID, medicalCode) VALUES (%s, %s)"
            val = (user_id, medicalCode)
            self.cursor.execute(sql, val)

        elif roleId == 4:
            sql = "INSERT INTO nurse (nurseID, medicalCode) VALUES(%s, %s)"
            val = (user_id, medicalCode)
            self.cursor.execute(sql, val)

        elif roleId == 5:
            sql = "INSERT INTO accountant (accountantID, degree) VALUES (%s, %s)"
            val = (user_id, degree)
            self.cursor.execute(sql, val)

        elif roleId == 6:
            sql = "INSERT INTO pharmacy (pharmacyID, medicalCode) VALUES (%s, %s)"
            val = (user_id, medicalCode)
            self.cursor.execute(sql, val)
        elif roleId == 7:
            sql = "INSERT INTO reception (receptionID) VALUES(%s)"
            val = (user_id,)
            self.cursor.execute(sql, val)
        elif roleId == 8:
            sql = "INSERT INTO laboratory (laboratoryID, medicalCode) VALUES (%s, %s)"
            val = (user_id, medicalCode)
            self.cursor.execute(sql, val)

        if delete:
            Manager().delete_from_waiting_list(eemail)
        self.conn.commit()

    def insert_user2(self, name, password, phoneNumber, eemail, roleId, medicalCode, degree, delete):
        sql_u = "INSERT INTO user (name, password, phoneNumber, email, roleId) VALUES(%s, %s, %s, %s, %s)"
        val_u = (name, password, phoneNumber, eemail, roleId)
        self.cursor.execute(sql_u, val_u)
        user_id = self.cursor.lastrowid
        print("ddjdjdjdj    ",roleId)
        if roleId == '2':
            sql = "INSERT INTO patient (patientID) VALUES(%s)"
            val = (user_id)
            self.cursor.execute(sql, val)

        elif roleId == '3':
            sql = "INSERT INTO doctor (doctorID, medicalCode) VALUES (%s, %s)"
            val = (user_id, medicalCode)
            self.cursor.execute(sql, val)

        elif roleId == '4':
            sql = "INSERT INTO nurse (nurseID, medicalCode) VALUES(%s, %s)"
            val = (user_id, medicalCode)
            self.cursor.execute(sql, val)

        elif roleId == '5':
            sql = "INSERT INTO accountant (accountantID, degree) VALUES (%s, %s)"
            val = (user_id, degree)
            self.cursor.execute(sql, val)

        elif roleId == '6':
            sql = "INSERT INTO pharmacy (pharmacyID, medicalCode) VALUES (%s, %s)"
            val = (user_id, medicalCode)
            self.cursor.execute(sql, val)
        elif roleId == '7':
            sql = "INSERT INTO reception (receptionID) VALUES(%s)"
            val = (user_id,)
            self.cursor.execute(sql, val)
        elif roleId == '8':
            sql = "INSERT INTO laboratory (laboratoryID, medicalCode) VALUES (%s, %s)"
            val = (user_id, medicalCode)
            self.cursor.execute(sql, val)

        if delete:
            Manager().delete_from_waiting_list(eemail)
        self.conn.commit()

    def delete_from_waiting_list(self, email):
        self.cursor.execute("DELETE FROM waitingList WHERE email = %s ", (email,))
        self.conn.commit()

    def delete_user_list(self, user_id):
        self.cursor.execute("DELETE FROM user WHERE userID = %s ", (user_id,))
        self.conn.commit()


    def show_waiting_list(self):
        self.cursor.execute("SELECT * FROM waitingList")
        waiting_list = self.cursor.fetchall()
        return waiting_list

    def show_users(self):
        self.cursor.execute("SELECT * FROM user  ")
        all_user = self.cursor.fetchall()
        return all_user

    # --------------------------------------------------------------------------------

    def show_patient(self):
        sql = "SELECT user.name, user.phoneNumber, user.email, user.userID, user.roleId \
                FROM user, patient \
                WHERE user.userID = patient.patientID"
        self.cursor.execute(sql)
        all_patient = self.cursor.fetchall()
        return all_patient

    def show_certain_patient(self, rowNumber):
        print("----------")
        self.cursor.execute("SELECT user.name, user.phoneNumber, user.email, user.userID, user.roleId \
                             FROM user, patient\
                             WHERE user.userID = patient.patientID")
        all_patient = self.cursor.fetchall()
        return all_patient[int(rowNumber) - 1]

    def show_prescription(self):
        self.cursor.execute("SELECT dr.name AS DoctorName, pt.name AS PatientName, dr.date AS date\
                            FROM (SELECT user.name, prescription.prescKey, prescription.date \
                                  FROM user , prescription WHERE prescription.doctorID = user.userID)dr JOIN\
                                 (SELECT user.name, prescription.prescKey \
                                  FROM user, prescription \
                                  WHERE prescription.patientID = user.userID) pt \
                            ON pt.prescKey = dr.prescKey")
        all_prescription = self.cursor.fetchall()
        return all_prescription

    def show_waiting_request_list(self):
        self.cursor.execute("SELECT dr.name AS DoctorName, pt.name AS PatientName, dr.visitTime AS date\
                                    FROM (SELECT user.name, waitingrequestvisitdoc.doctorID, waitingrequestvisitdoc.patientID, waitingrequestvisitdoc.visitTime \
                                          FROM user, waitingrequestvisitdoc \
                                          WHERE waitingrequestvisitdoc.doctorID = user.userID)dr JOIN\
                                         (SELECT user.name, waitingrequestvisitdoc.doctorID, waitingrequestvisitdoc.patientID, waitingrequestvisitdoc.visitTime \
                                          FROM user, waitingrequestvisitdoc \
                                          WHERE waitingrequestvisitdoc.patientID = user.userID) pt \
                                    ON pt.doctorID = dr.doctorID AND pt.patientID = dr.patientID AND pt.visitTime = dr.visitTime")
        all_waiting = self.cursor.fetchall()
        return all_waiting

    def show_inuse_beds(self):
        self.cursor.execute("SELECT dr.name AS DoctorName, pt.name AS PatientName, dr.bedID AS bed_ID, dr.section AS section\
                                            FROM (SELECT user.name, hospitalbed.bedID, hospitalbed.section \
                                                  FROM user, hospitalbed \
                                                  WHERE hospitalbed.doctorID = user.userID) dr JOIN\
                                                 (SELECT user.name, hospitalbed.bedID, hospitalbed.section \
                                                  FROM user, hospitalbed \
                                                  WHERE hospitalbed.patientID = user.userID) pt \
                                            ON pt.bedID = dr.bedID AND pt.section = dr.section")
        all_beds = self.cursor.fetchall()
        return all_beds

    def show_doctor(self):
        self.cursor.execute("SELECT user.name, user.phoneNumber, user.email, doctor.medicalCode \
                            FROM user, doctor \
                            WHERE user.userID = doctor.doctorID  ")
        all_doctor = self.cursor.fetchall()
        return all_doctor

    def show_nurse(self):
        self.cursor.execute("SELECT user.name, user.phoneNumber, user.email, nurse.medicalCode\
                             FROM user, nurse \
                             WHERE user.userID = nurse.nurseID  ")
        all_nurse = self.cursor.fetchall()
        return all_nurse

    def show_labratory(self):
        self.cursor.execute("SELECT user.name, user.phoneNumber, user.email, laboratory.medicalCode \
                             FROM user, laboratory \
                             WHERE user.userID = laboratory.laboratoryID  ")
        all_labratory = self.cursor.fetchall()
        return all_labratory

    def show_pharmacy(self):
        self.cursor.execute("SELECT user.name, user.phoneNumber, user.email, pharmacy.medicalCode \
                            FROM user, pharmacy \
                            WHERE user.userID = pharmacy.pharmacyID")
        all_pharmacy = self.cursor.fetchall()
        return all_pharmacy

    def show_accountant(self):
        self.cursor.execute("SELECT user.name, user.phoneNumber, user.email, accountant.degree \
                             FROM user, accountant \
                             WHERE user.userID = accountant.accountantID")
        all_accountant = self.cursor.fetchall()
        return all_accountant

    def show_drugs(self):
        self.cursor.execute("SELECT * FROM drug")
        all_drug = self.cursor.fetchall()
        return all_drug

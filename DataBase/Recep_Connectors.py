import mysql.connector
class Recep_Connectors:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="Hospital")
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def show_waiting_request_list(self):
        self.cursor.execute("SELECT dr.doctor,dr.doctorID,pt.patient, pt.patientID, dr.visitTime \
                    FROM (SELECT user.name AS doctor, waitingRequestVisitDoc.patientID, waitingRequestVisitDoc.doctorID, waitingRequestVisitDoc.visitTime\
                    FROM user , waitingrequestvisitdoc \
                    WHERE user.userID = waitingRequestVisitDoc.doctorID) dr JOIN \
                    (SELECT user.name AS patient, waitingRequestVisitDoc.doctorID, waitingRequestVisitDoc.patientID, waitingRequestVisitDoc.visitTime\
                    FROM user , waitingrequestvisitdoc \
                    WHERE user.userID = waitingRequestVisitDoc.patientID) pt\
                    ON dr.doctorID = pt.doctorID AND dr.patientID = pt.patientID AND dr.visitTime = pt.visitTime")


        waiting_list = self.cursor.fetchall()
        return waiting_list

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # noinspection SqlResolve
    def number_of_patients(self, user_id, time):
        sql = "SELECT COUNT(patientID) FROM reserved  WHERE reserved.doctorID = %s AND reserved.visitTime = %s"
        self.cursor.execute(sql, (user_id,time))
        counter = self.cursor.fetchall()

        return counter

    def show_patientCount_of_doctors(self, user_id, time):
        sql = "SELECT patientCount FROM availableTimesD  WHERE availableTimesD.doctorID = %s AND availableTimesD.visitTime = %s"
        self.cursor.execute(sql, (user_id, time))
        patientCount = self.cursor.fetchall()
        return patientCount

    def insert_to_reserve(self, patient):
        sql = "INSERT INTO reserved (patientID, doctorID, visitTime) VALUES (%s, %s, %s)"
        val = (patient[3], patient[1], patient[4])
        self.cursor.execute(sql, val)
        self.conn.commit()

    def delete_from_waiting_list(self, patient):
        sql = "DELETE FROM waitingrequestvisitdoc WHERE patientID = %s AND doctorID = %s AND visitTime = %s"
        self.cursor.execute(sql, (patient[3], patient[1], patient[4]))
        self.conn.commit()
#=======================================================================================================================
    def reserved_patient(self):

        sql = "SELECT dr.name AS doctor,dr.doctorID, pt.name AS patient, dr.patientID,  dr.visitTime \
               FROM (SELECT user.name AS name, reserved.patientID, reserved.doctorID, reserved.visitTime \
                     FROM user , reserved\
                     WHERE user.userID = reserved.patientID) pt JOIN\
                    (SELECT user.name AS name, reserved.doctorID, reserved.patientID, reserved.visitTime\
                     FROM user ,reserved\
                     WHERE user.userID = reserved.doctorID) dr\
               ON dr.doctorID = pt.doctorID AND dr.patientID = pt.patientID AND dr.visitTime = pt.visitTime"

        self.cursor.execute(sql)
        all_reserved_patient = self.cursor.fetchall()
        i = 1
        for x in all_reserved_patient:
            print(str(i),x)
            i += 1

        rowNumber = input()
        patient = all_reserved_patient[int(rowNumber) - 1]
        sql = "DELETE FROM reserved WHERE patientID = %s AND doctorID = %s AND visitTime = %s"
        val = (patient[3],patient[1],patient[4])
        self.cursor.execute(sql,val)
        self.conn.commit()
        print("deleted")
#=======================================================================================================================

    def show_available_time_all_doctors(self):
        self.cursor.execute("SELECT distinct user.userID , user.name FROM availabletimesD , user WHERE availableTimesD.doctorID = user.userID")
        available_times = self.cursor.fetchall()
        return available_times

    def show_availabe_time(self, doctor):
        sql = "SELECT visitTime, patientCount FROM availableTimesD WHERE doctorID = %s"
        self.cursor.execute(sql, (doctor[0],))
        doctor_times = self.cursor.fetchall()
        return doctor_times

    def allocate_bed_to_patient(self, bed_id, section, patient_id, doctor_id):
        sql = "SELECT hospitalbed.bedID, hospitalbed.section, user.name AS patient\
               FROM hospitalbed , user \
               WHERE user.userID = hospitalbed.patientID"
        self.cursor.execute(sql)
        all_beds = self.cursor.fetchall()  # bed_id / section / patientName
        boolean = True
        for x in all_beds:
            if str(x[0]) == str(bed_id) and str(x[1]) == str(section):
                print("This bed was reserved by", x[2])
                boolean = False
                break
        if boolean is True:
            sql = "INSERT INTO hospitalbed(bedID, section, patientID, doctorID) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(sql, (bed_id, section, patient_id, doctor_id))
            self.conn.commit()
            print("DONE !")
        return boolean  # if allocated = True else = False

    def complete_patient_history(self, bed_id, bed_section, patient_id, doctor_id):
        sql = "UPDATE patienthistory SET bedNo = %s , bedSec = %s WHERE patientID = %s AND doctorID = %s"
        self.cursor.execute(sql, (bed_id, str(bed_section), patient_id, doctor_id))
        self.conn.commit()

    def deliver_bed_from_patient(self, bed_id, section, patient_id, doctor_id):
        sql = "DELETE FROM hospitalbed WHERE bedID = %s AND section = %s AND patientID = %s AND doctorID = %s"
        self.cursor.execute(sql, (bed_id, section, patient_id, doctor_id))
        self.conn.commit()

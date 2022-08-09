import mysql.connector

class nurse_connector:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="Hospital")
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

#edit_report==========================================================================================================
    def get_reports(self, nurse_id):
        sql = "SELECT dr.name AS doctor, pt.name AS patient, dr.doctorID, dr.patientID, dr.reportDate, dr.details \
        FROM (SELECT user.name AS name,report.doctorID, report.patientID, report.reportDate, report.details \
              FROM user, report WHERE report.nurseID = %s AND report.doctorID = user.userID) dr JOIN\
             (SELECT user.name AS name,report.doctorID, report.patientID, report.reportDate, report.details\
              FROM user, report WHERE report.nurseID = %s AND report.patientID = user.userID) pt\
        ON dr.doctorID = pt.doctorID AND dr.patientID = pt.patientID AND dr.reportDate = pt.reportDate"

        self.cursor.execute(sql, (nurse_id, nurse_id))
        reports = self.cursor.fetchall()
        return reports

    def edit_doctor_id(self, report, newID, nurse_id):
        sql = "UPDATE report set doctorID = %s WHERE\
                nurseID = %s AND doctorID = %s AND patientID = %s AND reportDate = %s"
        self.cursor.execute(sql, (newID, nurse_id, report[2], report[3], report[4]))
        self.conn.commit()

    def edit_patient_id(self, report, newID, nurse_id):
        sql = "UPDATE report set patientID = %s WHERE\
                nurseID = %s AND doctorID = %s AND patientID = %s AND reportDate = %s"
        self.cursor.execute(sql, (newID, nurse_id, report[2], report[3], report[4]))
        self.conn.commit()

    def edit_date(self, report, newDate, nurse_id):
        sql = "UPDATE report set reportDate = %s WHERE\
                nurseID = %s AND doctorID = %s AND patientID = %s AND reportDate = %s"
        self.cursor.execute(sql, (newDate, nurse_id, report[2], report[3], report[4]))
        self.conn.commit()

    def edit_details(self, report, newDetails, nurse_id):
        sql = "UPDATE report set details = %s WHERE\
                nurseID = %s AND doctorID = %s AND patientID = %s AND reportDate = %s"
        self.cursor.execute(sql, (newDetails, nurse_id, report[2], report[3], report[4]))
        self.conn.commit()

#inset_new_report=====================================================================================================

    def insert_report(self, nurse_id, doctor_id, patient_id, report_date, details):
        sql = "INSERT INTO report(nurseID, doctorID, patientID, reportDate, details) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (nurse_id, doctor_id, patient_id, report_date, details))
        self.conn.commit()

#delete_report========================================================================================================

    def delete_report(self, report, nurse_id):
        sql = "DELETE FROM report\
                WHERE nurseID = %s AND doctorID = %s AND patientID = %s AND reportDate = %s AND details = %s"
        self.cursor.execute(sql, (nurse_id, report[2], report[3], report[4], report[5]) )
        self.conn.commit()


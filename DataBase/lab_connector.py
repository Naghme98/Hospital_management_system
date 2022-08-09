import mysql.connector
import os


class lab_connector:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="hospital")
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    # show_presc_result======================================================================================================
    def show_all_presc(self):
        sql = "SELECT dr.doctor AS doctor, dr.doctorID, pt.patient AS patient, pt.patientID , pt.date, pt.examinationKey \
               From (SELECT user.name AS doctor, examinationpresc.doctorID\
                            , examinationpresc.patientID, examinationpresc.date, examinationpresc.examinationKey \
                     FROM examinationpresc JOIN user\
                     WHERE examinationpresc.doctorID = user.userID) dr JOIN\
                    (SELECT user.name AS patient, examinationpresc.doctorID,\
                              examinationpresc.patientID, examinationpresc.date, examinationpresc.examinationKey\
                     FROM examinationpresc JOIN user\
                     WHERE examinationpresc.patientID = user.userID) pt\
                WHERE dr.doctorID = pt.doctorID AND dr.patientID = pt.patientID And dr.date = pt.date\
                        AND dr.examinationKey = pt.examinationKey"

        self.cursor.execute(sql)
        all_presc = self.cursor.fetchall()
        for x in all_presc:
            print(x)
        return all_presc

    def show_presc_with_specified_date(self, date):
        sql = "SELECT dr.doctor AS doctor, dr.doctorID, pt.patient AS patient, pt.patientID , pt.date, pt.examinationKey \
                      From (SELECT user.name AS doctor, examinationpresc.doctorID\
                                   , examinationpresc.patientID, examinationpresc.date, examinationpresc.examinationKey \
                            FROM examinationpresc JOIN user\
                            WHERE examinationpresc.doctorID = user.userID AND examinationpresc.date = %s) dr JOIN\
                           (SELECT user.name AS patient, examinationpresc.doctorID,\
                                     examinationpresc.patientID, examinationpresc.date, examinationpresc.examinationKey\
                            FROM examinationpresc JOIN user\
                            WHERE examinationpresc.patientID = user.userID AND examinationpresc.date = %s) pt\
                       WHERE dr.doctorID = pt.doctorID AND dr.patientID = pt.patientID And dr.date = pt.date\
                               AND dr.examinationKey = pt.examinationKey"
        self.cursor.execute(sql, (date, date))
        presc = self.cursor.fetchall()

        return presc

    def show_items_of_presc(self, presc):
        sql = "SELECT examinationlist.examinName, examin_items.examinationID, examin_items.resultAdd\
               FROM examin_items, examinationlist \
               WHERE examin_items.examinationKey = %s AND examin_items.examinationID = examinationlist.examinID"
        # print(presc[5])
        self.cursor.execute(sql, ((presc[5]),))
        # presc[5] --> examinationKey
        items_of_presc = self.cursor.fetchall()
        return items_of_presc

    def read_file_for_details(self, address):
        file = open(address, "r")
        print(file.read())
        file.close()

    def write_result_of_item_to_file(self, address, result):
        file = open(address, "w")
        file.write(result)
        file.close()

# a = lab_connector()
# a.show_all_presc()

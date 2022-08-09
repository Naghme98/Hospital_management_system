import mysql.connector


class Doctor_Connector:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="hospital")
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    # see all times
    def see_all_time_table(self, doctorID):
        sql = "select *  from availabletimesd where doctorID=%s "
        vle = (doctorID,)
        self.cursor.execute(sql, vle)
        list3 = self.cursor.fetchall()

        return list3

    # insert_availabletimes===========================================================

    def insert_time_to_avaiabletimes(self, doctorId, visitTime, patienCount):
        sql = "INSERT INTO availabletimesd(doctorID, visitTime, patientCount) VALUE(%s, %s, %s)"
        val = (doctorId, visitTime, patienCount)
        self.cursor.execute(sql, val)
        self.conn.commit()

    # delete_availabletimes===========================================================

    def delete_time_from_avaiabletimes(self, doctorId, visitTime):
        sql = "DELETE FROM availabletimesd WHERE doctorID = %s AND visitTime = %s"
        val = (doctorId, visitTime)
        self.cursor.execute(sql, val)
        self.conn.commit()

    # add prescription==============

    def insert_pres(self, doctorID, patientID, date):
        sql = "insert into  prescription(doctorID, patientID, date) value ( %s, %s, %s)"
        val = (doctorID, patientID, date)
        self.cursor.execute(sql, val)
        self.conn.commit()
        sql1 = "select prescKey from prescription where doctorID=%s and patientID=%s and date = %s"
        self.cursor.execute(sql1, val)
        out = self.cursor.fetchall()
        return out

    # add perscription item======================need to check
    def insert_drug_into_presc_Item2(self, prescKey, drugID, number):
        val = []
        for x in range(len(drugID)):
            val.append(prescKey, drugID[x], number[x])
        sql = "insert into presc_items(prescKey, drugID, number_of_item)   VALUE (%s,%s,%s)"
        self.cursor.executemany(sql, val)
        self.conn.commit()

        # add perscription item======================need to check

    def insert_drug_into_presc_Item(self, prescKey, drugID, number):
        sql = "insert into presc_items(prescKey, drugID, number_of_item) VALUE (%s,%s,%s)"
        val = (prescKey, drugID, number)
        self.cursor.execute(sql, val)
        self.conn.commit()

    # add examin_pres

    def insert_examinpres(self, doctorID, patientID, date):
        sql = "insert into  examinationpresc(doctorID, patientID, date) value ( %s, %s, %s)"
        val = (doctorID, patientID, date)
        self.cursor.execute(sql, val)
        self.conn.commit()
        sql1 = "select examinKey from examinationpresc where patientID=%s and doctorID=%s"
        self.cursor.execute(sql1, val)
        a = self.cursor.fetchall()
        return a

    # add perscription item======================need to check
    def insert_examin_into_examinItem2(self, examinKey, examinID):
        val = []
        for x in examinID:
            val.append(examinKey, x)
        sql = "insert into examin_items(examinationKey, examinationID, resultAdd)  VALUE (%s,%s)"
        self.cursor.executemany(sql, val)
        self.conn.commit()

    def insert_examin_into_examinItem(self, examinKey, examinID):
        val = (examinKey, examinID)
        sql = "insert into examin_items(examinationKey, examinationID, resultAdd)  VALUE (%s,%s)"
        self.cursor.execute(sql, val)
        self.conn.commit()

    # see list of drugs
    def see_all_drug(self):
        sql = "select * from drug"
        self.cursor.execute(sql)
        drugs = self.cursor.fetchall()
        return drugs

    # see all examination
    def see_all_examin(self):
        sql = "select * from examinationlist"
        self.cursor.execute(sql)
        examins = self.cursor.fetchall()
        return examins

    # see patient report
    def see_patient_report(self, doctorID, patientID):
        sql = "select * from report where patientID=%s and doctorID=%s"
        self.cursor.execute(sql, (patientID, doctorID))
        reports = self.cursor.fetchall()
        return reports

    # see patient drug
    def see_patient_drug(self, patientID):

        sql = "select drug.drugName, drug.drugID \
                from (select presc_items.drugID\
                      from (select prescKey\
                      from prescription \
                          where patientID = %s)p join presc_items  \
                          where presc_items.prescKey = p.prescKey) d join drug\
                    where drug.drugID = d.drugID"
        val = patientID
        self.cursor.execute(sql, (patientID,))
        list = self.cursor.fetchall()
        return list

    def insert_History(self, doctorId, patientID, visitTime):
        sql = "insert into patienthistory(patientID, doctorID, visitTime) value (%s,%s,%s)"
        val = (doctorId, patientID, visitTime)
        self.cursor.execute(sql, val)
        self.conn.commit()

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
            print(str(i), x)
            i += 1

        rowNumber = input()
        patient = all_reserved_patient[int(rowNumber) - 1]
        print('paaaa : ', patient)
        sql = "DELETE FROM reserved WHERE patientID = %s AND doctorID = %s AND visitTime = %s"
        val = (patient[3], patient[1], patient[4])
        self.cursor.execute(sql, val)
        self.conn.commit()

# d = Doctor_Connector()

# d.insert_drug_into_presc_Item(int(key[0][0]), 1, 1)

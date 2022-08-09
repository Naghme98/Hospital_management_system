import mysql.connector
class PatentConnectors:
    def __init__(self):
        self.conn =  mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Hospital")
        self.cursor = self.conn.cursor()
    def __del__(self):
        self.conn.close()

    def show_time_list_doc(self, ):
        print('ss')

    def show_doc(self):
        sql_select = "SELECT name,proficiency FROM user,doctor WHERE user.userID = doctor.doctorID"
        self.cursor.execute(sql_select)
        doctors = self.cursor.fetchall()
        print("sizeee: ", doctors.__len__())
        return doctors

    def show_times(self,i):
        print("show_times")
        sql = "SELECT userID FROM user,doctor WHERE user.userID = doctor.doctorID "
        self.cursor.execute(sql)
        dId = self.cursor.fetchall()
        xx =0
        print("iiii: ",i)
        ID = ""
        for x in dId:
            if xx == int(i)-1:
                ID = x
            xx += 1
        # print("IIIIIddd: ",ID[0])
        sql = "SELECT T.visitTime , T.patientCount , tedad FROM (SELECT visitTime, patientCount FROM availableTimesD WHERE doctorID = %s) T LEFT JOIN (SELECT count(patientID) as tedad, visitTime FROM reserved WHERE doctorID = %s GROUP BY(visitTime)) P  ON T.visitTime = P.visitTime where tedad < patientCount OR tedad IS NULL "
        self.cursor.execute(sql,(str(ID[0]),str(ID[0])))
        list = self.cursor.fetchall()
        return list






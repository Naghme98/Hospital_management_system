import mysql.connector


class Connectors:
    def __init__(self):
        self.conn =mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="13768191naghme",
    database="Hospital")
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def check_if_exists(self, username):
        sql_select = "SELECT password,roleId FROM user WHERE userID = %s"
        self.cursor.execute(sql_select, (username,))
        user_p = self.cursor.fetchone()
        # print(user_p)
        return user_p

    def insert_new_person(self, name, password, email, phone_num, med_code,role,deg):
        sql_insert = "INSERT INTO waitingList(name, password, phoneNumber, medicalCode, email,roleId,degree) values (%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(sql_insert,(name,password,phone_num,med_code,email,role,deg))
        self.conn.commit()


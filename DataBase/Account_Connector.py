import mysql.connector

class Account_Connector:
    def __init__(self):
       self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="Hospital")
       self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()
#create_factor==========================================================================================================
    def create_new_factor(self, patient_id, date):
        sql = "INSERT INTO factor(patientID,date) VALUE (%s, %s)"
        self.cursor.execute(sql, (patient_id,date))
        self.conn.commit()
        return self.cursor.lastrowid

    def complete_the_factor(self,factor_id, total_cost, file_address):
        sql = "UPDATE factor \
               set totalCost = %s , fileAddress = %s \
               WHERE patientID = %s"
        val = (total_cost, file_address, factor_id)
        self.cursor.execute(sql , val)
        self.conn.commit()
#edit_factor============================================================================================================
    def edit_patient_id(self, factor_id, newID):
        sql = "UPDATE factor SET patientID = %s WHERE factorID = %s"
        self.cursor.execute(sql , (newID , factor_id))
        self.conn.commit()

    def edit_date(self, factor_id, newDate):
        sql = "UPDATE factor SET date = %s WHERE factorID = %s"
        self.cursor.execute(sql, (newDate, factor_id))
        self.conn.commit()

    def edit_item_name(self, number, file, new_name):
        x = 0
        for x in number-1:
            x = x + 2
        file[x] = new_name
        return file

    def edit_item_price(self, number, file, new_price):
        x = 1
        for x in number-1:
            x = x + 2
        file[x] = new_price
        return file

    def edit_both_price_name(self, number, file, new_price, new_name):
        file = edit_item_name(number, file, new_name)
        file = edit_item_price(number, file, new_price)
        return file

    def get_file_address(self, factor_id):
        sql = "SELECT fileAddress FROM factor WHERE factorID = %s"
        self.cursor.execute(sql , (factor_id))
        address = self.cursor.fetchall()
        return address

    def read_file(self, file):
        lines_of_file = []
        for x in file.readlines():
            lines_of_file.append(x)
        return lines_of_file

    def write_file(self, file_address, edited_file):
        file = open(file_address, "w")
        for x in edited_file:
            file.write(x)
#get_total_cost=========================================================================================================
    def all_factors_total_cost(self):
        sql = "SELECT SUM(totalCost) FROM factor"
        self.cursor.execute(sql)
        all_cost = self.cursor.fetchall()
        return all_cost

    def the_factor_total_cost(self, factor_id):
        sql = "SELECT totalCost FROM factor WHERE factorID = %s"
        self.cursor.execute(sql , (factor_id))
        cost = self.cursor.fetchall()
        return cost
#filter_by_date=========================================================================================================

    def show_factor_specified_date(self, date):
        sql = "SELECT factor.factorID, user.userID, factor.date, factor.totalCost \
               FROM factor , user \
               WHERE date = %s AND user.userID = factor.patientID"
        self.cursor.execute(sql, (date))
        factors = self.cursor.fetchall()
        return factors

    def show_factor_date_interval(self, dateS, dateE):
        sql = "SELECT factor.factorID, user.userID, factor.date, factor.totalCost \
               FROM factor, user \
               WHERE date > %s AND date < %s AND user.userID = factor.patientID"
        self.cursor.execute(sql, (dateS, dateE))
        factors = self.cursor.fetchall()
        return factors
import mysql.connector


class DrugSt_Connector:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="Hospital")
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

#insert_drug=========================================================================================================

    def insert_drug_to_drug_table(self, drug_name, expiration_data, available_number, price):
        sql = "INSERT INTO drug(drugName, expirationDate, availableNumber, price) VALUES (%s, %s, %s, %s)"
        val = (drug_name, expiration_data, available_number,price)
        self.cursor.execute(sql,val)
        self.conn.commit()

#delete_drug=========================================================================================================

    def delete_drug_from_drug_table(self, drug):
        sql = "DELETE FROM drug WHERE drugID = %s"
        self.cursor.execute(sql, (drug[1],))
        self.conn.commit()

#drug_filter_by_date=================================================================================================

    def show_drug_specified_date(self, date):
        sql = "SELECT drugName, availableNumber, price FROM drug WHERE expirationDate <= %s"
        self.cursor.execute(sql, (date,))
        drugs = self.cursor.fetchall()
        return drugs

    def show_drug_date_interval(self, dateS, dateE):
        sql = "SELECT drugName, availableNumber, price FROM drug WHERE expirationDate >= %s AND expirationDate <= %s"
        self.cursor.execute(sql, (dateS, dateE))
        drugs = self.cursor.fetchall()
        return drugs

#give_drug_to_patient================================================================================================

    def show_deatail_of_prescription(self, prescription_key):
        sql = "SELECT drugID, number_of_item FROM presc_items  WHERE prescKey = %s"
        self.cursor.execute(sql, (prescription_key))
        all_drugs_id = self.cursor.fetchall()
        return all_drugs_id

    def search_presc_of_patient(self, patient_id):
        sql = "SELECT user.name AS doctor, prescription.date AS date, prescription.prescKey AS prescription_key \
               FROM prescription JOIN user\
               WHERE prescription.patientID = %s AND prescription.doctorID = user.userID"
        self.cursor.execute(sql, (patient_id))
        prescriptions = self.cursor.fetchall()
        return prescriptions

    def get_details_of_drug(self, drug_id):
        sql = "SELECT drug.drugName, drug.drugID, presc_items.number_of_item, drug.expirationDate,drug.availableNumber, drug.price \
               FROM drug, presc_items \
               WHERE drug.drugID = %s AND presc_items.drugID = %s"
        self.cursor.execute(sql, (drug_id, drug_id))
        this_drug = self.cursor.fetchall()
        return this_drug

    def show_available_and_unavailable_drugs(self, drugs):
        available = []
        unavailable = []
        for x in drugs:
            drug = DrugSt_Connector().get_details_of_drug(x)

            if drug[3] >= x[1]:  # This drug is on hand " availableNumber > number of drug that the patient needs"
                available.append(drug)
            else:
                unavailable.append(drug)

        return available, unavailable

    def reduce_available_number(self, drug_id, number):
        sql = "UPDATE drug SET availableNumber = availableNumber - %s WHERE drugID = %s"
        self.cursor.execute(sql, (number, drug_id))
        self.conn.commit()

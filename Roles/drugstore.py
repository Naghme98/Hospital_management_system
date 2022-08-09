from DataBase.DrugSt_Connector import DrugSt_Connector
from DataBase.Connectors import Connectors


class drugstore:
    drugst_obj = DrugSt_Connector()
    conn_obj = Connectors()

    def insert_drug(self):
        drug_name = input("Enter the drug's name\n")
        expiration_data = input("Enter the date this format YYYY-MM-DD\n")
        available_number = input("Enter number of this drug available\n")
        price = input("Enter the price\n")
        drugstore.drugst_obj.insert_drug_to_drug_table(drug_name, expiration_data, available_number, price)

    def delete_drug(self):
        all_drugs = drugstore.drugst_obj.show_drugs()
        i = 1
        for x in all_drugs:
            print((str(i)+":"), x)
            i += 1

        rowNumber = input("Which drug do you wanna to delete?\n")
        drug_for_del = all_drugs[int(rowNumber) - 1]
        drugstore.drugst_obj.delete_drug_from_drug_table(drug_for_del)

    def drug_filter_by_date(self):
        request = input("Specified date:1\nDate interval:2\nQuite: Q\n")
        while request is not 'Q':
            if request is '1':
                date = input("Please enter data like this pattern : 0000-00-00\n")
                drugs = drugstore.drugst_obj.show_drug_specified_date(date)
                for x in drugs:
                    print(x)
            elif request is '2':
                dataS = input("Please enter started data like this pattern : 0000-00-00\n")
                dataE = input("Please enter finished data like this pattern : 0000-00-00\n")
                if dataS < dataE:
                    drugs = drugstore.drugst_obj.show_drug_date_interval(dataS,dataE)
                    for x in drugs:
                        print(x)
                else:
                    print("You've set the wrong date")
            request = input("Specified date:1\nDate interval:2\nQuite: Q")

    def show_drugs (self):
        all_d = drugstore.drugst_obj.show_drugs()
        i =1
        for x in all_d:
            print((str(i)+":"),x)
            i += 1

    def give_drug_to_patient(self):
        patient_id = input("Enter patient ID:\n")
        prescriptions = drugstore.drugst_obj.search_presc_of_patient(patient_id)
        for x in prescriptions:  # doctor_name / date / prescriptionKey
            print(x, "\n")
        prescription_key = input("Please enter the prescription_key that you want to show deatails:\n")
        all_drugs_id_and_number = drugstore.drugst_obj.show_detail_of_prescription(prescription_key)
        available, unavailable = drugstore.drugst_obj.show_available_and_unavailable_drugs(all_drugs_id_and_number)
        print("These drugs are not available:\n")
        for x in unavailable:
            print(x, "\n")

        print("Available Drugs:\n")
        for x in available:
            print(x, "\n")

        request = input("Which drug do you want?\n Quite:Q")
        while request is not 'Q':
            drug = available[
                request - 1]  # drug(drugName, drugID, number of item, expirationDate, availableNumber, Price)
            drugstore.drugst_obj.reduce_available_number(drug[1], drug[2])
            del available[request - 1]
            print("Available Drugs:\n")
            for x in available:
                print(x, "\n")
            request = input("Which drug do you want?\n Quite:Q")

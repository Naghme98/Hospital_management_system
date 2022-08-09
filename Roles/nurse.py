from DataBase.nurse_connector import nurse_connector


class nurse:
    nurse_obj = nurse_connector()

    def __init__(self):
        print("welcome dear nurse\n")

    def edit_report(self, nurse_id):
        reports = nurse.nurse_obj.get_reports(nurse_id)

        if reports.__len__() != 0:
            i =1
            for x in reports:
                print((str(i)+" : "), x, "\n")
                i += 1
            number = input("Enter the rowNumber\n")
            edit_this_report = reports[int(number)-1]
            request = input("Quite:Q\nEdit doctor:1\nEdit patient:2\nEdit date:3\nEdit details of report:4\n")
            while request is not 'Q':
                if request == '1':
                    new_doctor_id = input("Enter new doctor ID:\n")#change doctorID
                    nurse.nurse_obj.edit_doctor_id(edit_this_report, new_doctor_id, nurse_id)
                elif request == '2':
                    new_patien_id = input("Enter new patien ID:\n")
                    nurse.nurse_obj.edit_patient_id(edit_this_report, new_patien_id, nurse_id)
                elif request == '3': #change date
                    new_date= input("Enter new date:\n")
                    nurse.nurse_obj.edit_date(edit_this_report, new_date, nurse_id)
                elif request == '4': #chenage details
                    new_detail = input("Enter your detail text :\n")
                    nurse.nurse_obj.edit_details(edit_this_report, new_detail, nurse_id)

                cc = input('Q for quiet\n')
                if cc == 'Q':
                    break
                reports = nurse.nurse_obj.get_reports(nurse_id)
                i =1
                for x in reports:
                    print((str(i) + ":"), x, "\n")
                    i += 1
                number = input("Which report do you want to edit?\n")
                edit_this_report = reports[int(number) - 1]
                request = input("Quite:Q\nEdit doctor:1\nEdit patient:2\nEdit date:3\nEdit details of report:4\n")


    def inset_new_report(self,nurse_id):
        c = input('Quiet:Q\nCountinue:C\n')
        while c != 'Q':
            doctor_id = input("Please enter doctor ID\n")
            patient_id = input("please enter patient ID\n")
            date = input("Please enter the date of this report\n")
            details = input("Please enter details of this report\n")
            nurse.nurse_obj.insert_report(nurse_id, doctor_id, patient_id, date, details)
            c = input('Quiet:Q\nCountinue:C\n')

    def delete_report(self, nurse_id):
        reports = nurse.nurse_obj.get_reports(nurse_id)
        i =1
        for x in reports:
            print((str(i)+ ":"), x[0], x[1], x[4], x[5])  # doctor_name \ patient_name \ date \ details
            i += 1

        rowNumber = input("Which report do you want to delete?\nFor Qiute: Q\n")

        while rowNumber is not 'Q':
            report_for_deleting = reports[int(rowNumber)-1]
            delete_report = nurse.nurse_obj.delete_report(report_for_deleting, nurse_id)
            del reports[int(rowNumber) - 1] #delete from list

            i = 1
            for x in reports:
                print((str(i) + ":"), x[0], x[1], x[4], x[5])  # doctor_name \ patient_name \ date \ details
                i += 1

            rowNumber = input("Which report do you want to delete?\nFor Qiute: Q\n")

    def show_reports(self, nurse_id):
        reports = nurse.nurse_obj.get_reports(nurse_id)

        i = 1
        for x in reports:
            print((str(i) + ":"), x[0], x[2], x[1], x[3],x[4], x[5])   # doctor_name / patient_name / doctor_id / patient_id / date / details
            i += 1



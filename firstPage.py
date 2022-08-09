from Roles.Patient import Patient
from Roles.Manager import manager
from Roles.receptionist import receptionist
from DataBase.Connectors import Connectors
from Roles.drugstore import drugstore
from Roles.nurse import nurse


class Main:

    b = False
    while not b:
        choice = input("Hi welcome.. enter 1 for signIn , 2 for SignUp, Q for exit\n")
        if choice == '1':
            username = input("Enter your userName:\n")
            passWord = input("Enter your password:\n")
            userInfo = Connectors().check_if_exists(username)
            # print(userInfo)
            if not userInfo or userInfo[0] != passWord:
                print("This user doesn't exist\n")
            else:
                b = True
                #------------- reception ---------------------
                print("idddd: ",userInfo[1])
                if userInfo[1] is 1:
                    c = input("For updating requests of Patients:1\nFor updating reserved List:2\nFor visiting the Doctors available time:3\nFor assigning Bed:4\nTake back the bed:5\nQuiet:Q\n")
                    while c is not 'Q':
                        recep = receptionist()
                        if c == '1':
                            recep.insert_time()
                        elif c == '2':
                            recep.delete_time()
                        elif c == '3':
                            recep.available_time()
                        elif c == '4':
                            recep.assign_bed()
                        elif c == '5':
                            recep.deliver_bed()
                        c = input("For updating requests of Patients:1\nFor updating reserved List:2\nFor visiting the Doctors available time:3\nFor assigning Bed:4\nTake back the bed:5\nQuiet:Q\n")
                elif userInfo[1] is 3:
                    nurse = nurse()
                    c = input("Q for Quite\nFor editing reports:1\nInsert new report:2\nDeleting some report:3\nShowing all reports:4\n")
                    while c != 'Q':
                        if c == '1':
                            nurse.edit_report(10)    # nurse.edit_report(str(username))
                        elif c == '2':
                            nurse.inset_new_report(10)
                        elif c == '3':
                            nurse.delete_report(10)
                        elif c == '4':
                            nurse.show_reports(10)
                        c = input("\n\nQ for Quite\nFor editing reports:1\nInsert new report:2\nDeleting some report:3\nShowing all reports:4\n")

                elif userInfo[1] is 4:
                    manage = manager()
                    c = input("Q for Quite\nFor update waiting list :1\nFor delete a user:2\nFor observing hospital users:3\nFor adding a user:4\n")
                    while c != 'Q':
                        if c == '1':
                            manage.insert_user_from_waiting_list()
                        elif c == '2':
                            manage.del_user()
                        elif c =='3':
                            manage.show_data()
                        elif c == '4':
                            manage.register_by_manager()
                        c = input("Q for Quite\nFor update waiting list :1\nFor delete a user:2\nFor observing hospital users:3\nFor adding a user:4\n")

                elif userInfo[1] is 2:
                    drugst = drugstore()
                    c = input("Q for Quite\nFor showing all drugs:1\ninsert a drug:2\ndelete a drug:3\nfilter by expiration date:4\n")
                    while c != 'Q':
                        if c == '1':
                            drugst.show_drugs()
                        if c == '2':
                            drugst.insert_drug()
                        elif c == '3':
                            drugst.delete_drug()
                        elif c == '4':
                            drugst.drug_filter_by_date()
                        c = input("Q for Quite\nFor showing all drugs:1\ninsert a drug:2\ndelete a drug:3\nfilter by expiration date:4\n")

        elif choice == '2':
            name = input("Enter the name:\n")
            password = input("Enter the password\n")
            phoneNumber = input("Enter the phoneNumber\n")
            email = input("Enter the email\n")
            roleId = input(
                "For doctor:3 -- patient:2 -- nurse:4 -- accountant:5 -- pharmecy:6 -- reception:7 -- labratory:8\n")
            if roleId == '3' or roleId == '4' or roleId == '6' or roleId == '8':
                medicalCode = input("Enter the medical Code\n")
            else:
                medicalCode = 'NULL'
            degree = 'NULL'
            if roleId == '5':
                degree = input("Enter degree\n")


            userInfo = Connectors().insert_new_person(name,password,email,phoneNumber,medicalCode,roleId,degree)

        elif choice == 'Q':
            break





# if __name__ == '__main__':


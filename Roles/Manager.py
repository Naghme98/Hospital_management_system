from DataBase.Manager_conn import Manager
class manager:

    manger_obj = Manager()
    def register_by_manager(self):
        name = input("Enter the name:\n")
        password = input("Enter the password\n")
        phoneNumber = input("Enter the phoneNumber\n")
        email = input("Enter the email\n")
        roleId = input("For doctor:3 -- patient:2 -- nurse:4 -- accountant:5 -- pharmecy:6 -- reception:7 -- labratory:8\n")
        if roleId == '3' or roleId == '4' or roleId == '6' or roleId == '8':
            medicalCode = input("Enter the medical Code\n")
        else:
            medicalCode = 'NULL'
        degree = 'NULL'
        if roleId == '5' :
            degree = input("Enter degree\n")

        manager.manger_obj.insert_user2(name, password, phoneNumber, email, roleId, medicalCode, degree,False)

    def insert_user_from_waiting_list(self):
        waiting_list =manager.manger_obj.show_waiting_list()
        i =1
        for x in waiting_list:
            print((str(i)+":"), x)
            i += 1
        choice = input("if you want to delete a request: d , confirm: c, quit: q\n")
        while choice is not 'q':
            if choice is 'c':
                rowNumber = input("which user you want to confirm:\n")
                person = waiting_list[int(rowNumber) - 1]
                manager.manger_obj.insert_user(person[0], person[1], person[2], person[4], person[5],person[3], person[6], True)
            else:
                rowNumber = input("which user you want to delete:\n")
                person = waiting_list[int(rowNumber) - 1]
                manager.manger_obj.delete_from_waiting_list(person[4])
            waiting_list = manager.manger_obj.show_waiting_list()
            i = 1
            for x in waiting_list:
                print((str(i) + ":"), x)
                i += 1
            choice = input("if you want to delete a request: d , confirm: c, quit: q\n")

    def del_user(self):
        all_user = manager.manger_obj.show_users()
        i = 1
        for x in all_user:
            print((str(i) + ":"), x)
            i += 1

        rowNumber = input("which user you wanna delete:\n")
        person = all_user[int(rowNumber) - 1]
        manager.manger_obj.delete_user_list(person[4])

    def show_data(self):

        choice = input("Q for quite\nFor user table:1\npatient table:2\nwating List For Confirm Joinnig To hospital:3\nprescriptions:4\n"
                       "waitingList to be confirmed py reception:5\ninuse beds:6\nList of doctors:7\nList of nurses:8\nList of labratory:9\n"
                       "List of pharmacy:10\nList of accountants:11\nList of drugs:12\n")
        while choice is not 'Q':
            if choice is '1':
                all = manager.manger_obj.show_users()
            elif choice is '2':
                all = manager.manger_obj.show_patient()
                i = 1
                for x in all:
                    print((str(i) + ":"), x)
                    i += 1
                print("---------------------------------------")
                req = input("S for searching a certain patient\nQ for quite\n")
                if req is 'S':
                    rowNumber = input("Which Patient do you want to show?\n")
                    person = manager.manger_obj.show_certain_patient(rowNumber)
                    print(person)
                choice = input(
                    "Q for quite\nFor user table:1\npatient table:2\nwating List For Confirm Joinnig To hospital:3\nprescriptions:4\n"
                    "waitingList to be confirmed py reception:5\ninuse beds:6\nList of doctors:7\nList of nurses:8\nList of labratory:9\n"
                    "List of pharmacy:10\nList of accountants:11\nList of drugs:12\n")
                continue
            elif choice == '3':
                all = manager.manger_obj.show_waiting_list()
            elif choice == '4':
                all = manager.manger_obj.show_prescription()
            elif choice == '5':
                all = manager.manger_obj.show_waiting_request_list()
            elif choice == '6':
                all = manager.manger_obj.show_inuse_beds()
            elif choice == '7':
                all = manager.manger_obj.show_doctor()
            elif choice == '8':
                all = manager.manger_obj.show_nurse()
            elif choice == '9':
                all = manager.manger_obj.show_labratory()
            elif choice == '10':
                # print("+++++++======+=_-+-=")
                all = manager.manger_obj.show_pharmacy()
            elif choice == '11':
                all = manager.manger_obj.show_accountant()
            elif choice == '12':
                all = manager.manger_obj.show_drugs()

            i = 1
            for x in all:
                print((str(i) + ":"), x)
                i += 1
            print("---------------------------------------")

            choice = input("Q for quite\nFor user table:1\npatient table:2\nwating List For Confirm Joinnig To hospital:3\nprescriptions:4\n"
                           "waitingList to be confirmed py reception:5\ninuse beds:6\nList of doctors:7\nList of nurses:8\nList of labratory:9\n"
                           "List of pharmacy:10\nList of accountants:11\nList of drugs:12\n")
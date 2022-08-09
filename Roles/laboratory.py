from DataBase.lab_connector import lab_connector


class laboratory:
    lab_obj = lab_connector()

    def show_presc_result(self):
        request = input("Show all prescriptions:1\nShow prescription with specified date:2")
        if request == "1":
            # print("here")
            all_presc = laboratory.lab_obj.show_all_presc()
            for x in all_presc:
                print(str(x) + "\n")
        elif request == "2":
            date = input("Please enter thr date like the pattern yyyy:mm:dd")
            all_presc = laboratory.lab_obj.show_presc_with_specified_date(date)
            for x in all_presc:
                print(str(x) + "\n")

        rowNumber = input("Which prescription do you want to show:\n")
        if int(rowNumber) < 1:
            rowNumber = 1
        elif int(rowNumber) > len(all_presc):
            rowNumber = len(all_presc)
        presc = all_presc[int(rowNumber) - 1]

        items_of_presc = laboratory.lab_obj.show_items_of_presc(presc)

        for x in items_of_presc:
            print(x[0] + "\n")  # just examination_NAME

        rowNumber = input("Which examination's item do you want to show its details :\n")
        details_presc = items_of_presc[int(rowNumber) - 1]
        laboratory.lab_obj.read_file_for_details(details_presc[2])  # Print from file

    def create_result_of_presc(self):
        request = input("Show all prescriptions:1\nShow prescription with specified date:2")
        if request is "1":
            all_presc = laboratory.lab_obj.show_all_presc()
            for x in all_presc:
                print(str(x) + "\n")
        elif request is "2":
            date = input("Please enter thr date like the pattern yyyy:mm:dd")
            all_presc = laboratory.lab_obj.show_presc_with_specified_date(date)
            for x in all_presc:
                print(str(x) + "\n")  # doctor_name / doctor_id / patient_name / patien_id / date / examinationKey

        rowNumber = input("Which prescription do you want to show:\n")
        if int(rowNumber) < 1:
            rowNumber = 1
        elif int(rowNumber) > len(all_presc):
            rowNumber = len(all_presc)
        presc = all_presc[int(rowNumber) - 1]
        items_of_presc = laboratory.lab_obj.show_items_of_presc(presc)  # examinationName / examinationID / address

        for x in items_of_presc:
            print(x[0] + "\n")  # just examination_NAME
        request = input("Quite:Q\nWrite result:W\n")
        while request is not 'Q':
            rowNumber = input("Which item do you want to write its result :\n")
            details_of_item = items_of_presc[int(rowNumber) - 1]
            result = input("Enter the result:\n")
            laboratory.lab_obj.write_result_of_item_to_file(details_of_item[2], result)  # write to file
            request = input("Quite:Q\nWrite another result:W\n")


k = laboratory()
k.create_result_of_presc()

from DataBase.Recep_Connectors import Recep_Connectors
from DataBase.Connectors import Connectors
from datetime import datetime
from datetime import date


class receptionist:

    recpConnector_obj = Recep_Connectors()
    connector_obj = Connectors()

    def insert_time(self):
        waiting_list = receptionist.recpConnector_obj.show_waiting_request_list()

        if not waiting_list:
            print("No one wants to reserve time :))")
        else:
            i = 1
            for x in waiting_list:
                print(((str)(i) + " : "), x)
                i += 1

            rowNumber = input("For Insert a patient: I-numberOfRow\nFor delete from this Table: D-numberOfRow \n")
            patient_time = waiting_list[int(rowNumber[2]) - 1]
            if rowNumber[0] == 'I':
                counter = receptionist.recpConnector_obj.number_of_patients(patient_time[1], patient_time[4])
                patientCount = receptionist.recpConnector_obj.show_patientCount_of_doctors(patient_time[1], patient_time[4])
                if counter < patientCount:
                    receptionist.recpConnector_obj.insert_to_reserve(patient_time)
                    receptionist.recpConnector_obj.delete_from_waiting_list(patient_time)
                    print("Patient was added")
                else:
                    print('The Doctor doesnt have time')
            else:
                receptionist.recpConnector_obj.delete_from_waiting_list(patient_time)
                print("user now is deleted")

    def delete_time(self):

        print('For delete from waiting list enter its row\n')
        receptionist.recpConnector_obj.reserved_patient()

    def available_time(self):

        available_times = receptionist.recpConnector_obj.show_available_time_all_doctors()
        i = 1;
        for x in available_times: #print Doctors' name
            print((str(i)+": "), x[1])
            i += 1
        rowNumber = input("Which doctor do you want to see her\his available times\n")
        doctor = available_times[int(rowNumber) - 1]

        doctor_times = receptionist.recpConnector_obj.show_availabe_time(doctor)
        i =1
        for x in doctor_times:
            print((str(i)+": "), x)
            i += 1

    def assign_bed(self):
        bed_id = input("Please enter bed ID:\n")
        section = input("Which section dou you want to assign:\n")
        patient_id = input("Please enter patient id:\n")
        doctor_id = input("Please enter doctor ID:\n")

        boolean = receptionist.recpConnector_obj.allocate_bed_to_patient(bed_id, section, patient_id, doctor_id)
        if boolean is True:
            receptionist.recpConnector_obj.complete_patient_history(bed_id, section, patient_id, doctor_id)

    def deliver_bed(self):
        bed_id = input("Please enter bed ID:\n")
        section = input("Which section dou you want to assign:\n")
        patient_id = input("Please enter patient id:\n")
        doctor_id = input("Please enter doctor ID:\n")

        receptionist.recpConnector_obj.deliver_bed_from_patient(bed_id, section, patient_id, doctor_id)
from DataBase.Doctor_Connector import Doctor_Connector
from DataBase.Connectors import Connectors
from datetime import datetime
from datetime import date


class Doctor:
    drConnector_obj = Doctor_Connector()
    connector_obj = Connectors()

    def editTimeTable(self):
        print('For delete from waiting list enter its row\n')
        Doctor.recpConnector_obj.reserved_patient()

    def seeHistoryPatient(self):
        x = input('Enter patient id:')
        print('drug list:')
        list4 = Doctor.drConnector_obj.see_patient_drug(x)
        for i in list4:
            print(i)

    def seeReport(self):
        x = input("enter dr id")
        y = input("enter pa id")
        reportList = Doctor.drConnector_obj.see_patient_report(x, y)
        for i in reportList:
            print(i)

    def editAvailableTime(self):
        doctorId = input("enter dr id: ")

        avllist = Doctor.drConnector_obj.see_all_time_table(doctorId)
        for i in avllist:
            print(i)
        b = False
        while not b:
            stat = input("enter D for Delete , enter A for Add,enter E for Exit : ")
            if stat == "D" or stat == "d":
                time = input("enter time to delete: ")
                Doctor.drConnector_obj.delete_time_from_avaiabletimes(doctorId, time)
            elif stat == "A" or stat == "a":
                time = input("enter time to insert: ")
                number = input("enter number of visit : ")
                Doctor.drConnector_obj.insert_time_to_avaiabletimes(doctorId, time, number)
            else:
                b = True

    def addPersc(self):
        patientid = input("enter patient id: ")
        doctorid = input("enter doctor id: ")
        e = False
        while not e:
            stat = input("enter P for add prescription , enter A for Add examination prescription ,enter E for Exit : ")
            if stat == "p" or stat == "P":
                dat = date.today()
                dat1 = "2019-06-14"
                key = Doctor.drConnector_obj.insert_pres(doctorid, patientid, dat1)
                #print(key)
                con = False
                while not con:
                    name = input("for cancel enter C  "
                                 "enter your drug id to add: ")
                    if name == "c" and name == "C":
                        con = True
                        break
                    else:
                        num = input("enter number of it: ")
                        Doctor.drConnector_obj.insert_drug_into_presc_Item(key[0][0], name, num)
            elif stat == "A" or stat == "a":
                dat = str(date.today())

                key = Doctor.drConnector_obj.insert_examinpres(doctorid, patientid, dat)
                con = False
                while not con:
                    name = input("for cancel enter C "
                                 "enter your examin number to add: ")
                    if name == "c" and name == "C":
                        con = True
                        break
                    else:
                        Doctor.drConnector_obj.insert_examin_into_examinItem(key[0][0], name)
            else:
                b = True

    def visit(self):
        patientid = input("enter patient id: ")
        doctorid = input("enter doctor id: ")
        date=datetime.now()
        Doctor.drConnector_obj.insert_History(doctorid, patientid, date)


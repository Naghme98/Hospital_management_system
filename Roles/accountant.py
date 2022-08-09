from Account_Connector import Account_Connector
import os

class accountant:
    account_obj = Account_Connector()

    def create_factor(self):
        patient_id = input("Please enter patienr id: \n")
        data = input("Please enter data of factor: \n")

        factor_id = accountant.account_obj.create_new_factor(patient_id,data)
        factor_file = open(factor_id+".txt","a")

        request = input("add item to factor:C \n Quite:Q")
        i = 1
        total_cost = 0
        while request is not 'Q':
            item = input("write the item\n")
            factor_file.write("%d-%s\n" % (i),(item))
            price = input("write price of item:\n")
            factor_file.write("%d\n" % (price))
            i = i + 1
            total_cost = price + total_cost
            request = input("add item to factor:C \n Quite:Q")

        fileDir = os.path.dirname(os.path.realpath('__file__')) #address
        accountant.account_obj.complete_the_factor(factor_id, total_cost,fileDir)

    def edit_factor(self):
        factor_id = input("Please enter factor id: \n")

        request = input("Edit patient id:1\nEdit date:2\nEdit item:3\nQuite:Q")
        while request is not 'Q':
            if request is 1:
                new_patient_id = input("Enter new patient ID:\n")
                accountant.account_obj.edit_patient_id(factor_i, new_patient_id)
            if request is 2:
                new_date = input("Enter new date\n")
                accountant.account_obj.edit_date(factor_id, new_date)
            if request is 3:
                file_address = accountant.account_obj.get_file_address(factor_id)
                file = open(file_address,"r")
                lines_of_file = accountant.account_obj.read_file(file)
                req = input("Edit item name:1\nEdit price of item:2\nEdit both name and price of item:3\n")
                if req is 1:
                    number = input("Please enter the number of item:\n")
                    new_name = input("Please enter new name of item:\n")
                    lines_of_file = accountant.account_obj.edit_item_name(number, lines_of_file, new_name)
                elif req is 2:
                    number = input("Please enter the number of item:\n")
                    new_price = input("Please enter new price of item:\n")
                    lines_of_file = accountant.account_obj.edit_item_price(number, lines_of_file, new_price)
                elif req is 3:
                    number = input("Please enter the number of item:\n")
                    new_name = input("Please enter new name of item:\n")
                    new_name = input("Please enter new name of item:\n")
                    lines_of_file = accountant.account_obj.edit_both_price_name(number, lines_of_file, new_price, new_name)

                accountant.account_obj.write_file(file_address, lines_of_file)

    def get_total_cost(self):
        request = input("ALL factors:1\n A specific factor:2\nQuite:Q")

        while request is not 'Q':
            if request is 1:
                accountant.account_obj.all_factors_total_cost()
            elif request is 2:
                factor_id = input("Enter factor ID:\n")
                accountant.account_obj.the_factor_total_cost(factor_id)

    def filter_by_date(self):
        request = input("Specified date:1\nDate interval:2\nQuite: Q")
        while request is not 'Q':
            if request is 1:
                date = input("Please enter data like this pattern : 0000-00-00")
                factors = accountant.account_obj.show_factor_specified_date(date)
            elif request is 2:
                dataS = input("Please enter started data like this pattern : 0000-00-00")
                dataE = input("Please enter finished data like this pattern : 0000-00-00")
                if dataS < dataE:
                    factors = accountant.account_obj.show_factor_date_interval(dataS, dataE)
                else:
                    print("You've set the wrong date")

            for x in factors:
                print(x)
            request = input("Specified date:1\nDate interval:2\nQuite: Q")
                












'''
def main():
    h = []
    f = open("sara1.txt", "r")
    for x in f.readlines():
        h.append(x)

   # for x in h:
    print(h[2])
    f.close()



if __name__ == "__main__":
        main()
'''


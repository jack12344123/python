class requisition:
    counter = 0
    total_approved_requisitions = 0
    total_not_approved = 0
    total_pending_requisitions = 0

    def __init__(self,Date, staff_id, staff_name, status ):
        self.Date = Date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.status = status
        self.total = 0
        self.items = []
        self.requisition_id = 0
        self.approval_ref = "Not available"

    def add_requisition(self):


        print("---------Enter your information:-----------")
        import datetime

        while True:
            self.date = input("Date (YYYY-MM-DD): ")
            try:

                self.date = datetime.datetime.strptime(self.date, "%Y-%m-%d").date()
                print("Date valid")
                break
            except ValueError:
                print("Date not valid. Please try again.")

        while True:
            self.staff_id = input("Staff ID: ")
            if self.staff_id == "" or not self.staff_id.isdigit():
                print("Staff ID not valid. Please try again.")
            else:
                print("Staff ID valid")
                break





        while True:
            self.staff_name = input("Enter staff name: ")


            if self.staff_name == "" or not self.staff_name.replace(" ", "").isalpha():
                print("Staff Name not valid. Please try again.")
            else:
                print("Staff name valid.")
                break



        requisition.counter += 1
        self.requisition_id = requisition.counter + 10000

        self.total = 0
        self.items = []

        print("\nAdd items:")
        answer = "yes"

        while answer == "yes":
            item_name = input("Item Name: ")
            item_price = float(input("Item Price ($): "))
            self.items.append((item_name, item_price))
            self.total += item_price

            answer = input("Add another item (yes/no): ").lower()










    def approve_requisition(self):
        self.status = "Pending"

        if self.total < 500:

            self.status = "Approved"
            last_three = str(self.requisition_id)[-3:]
            self.approval_ref = self.staff_id + last_three
            requisition.total_approved_requisitions += 1
        else:

            self.approval_ref = "not available"
            requisition.total_pending_requisitions += 1



    def respond_requisition(self):
        if self.status == "Pending":
            response = input("Approve or Not approved? ")
            if response.lower() == "approved":
                self.status = "Approved"
                requisition.total_approved_requisitions += 1
                requisition.total_pending_requisitions -= 1
            elif response.lower() == "not approved":
                self.status = "Not approved"
                requisition.total_not_approved += 1
                requisition.total_pending_requisitions -= 1
            else:
                print("invalid response. Please try again.")
        else:
            print("This requisition is not pending..")






    def display_requisition(self):
        print("Requisition ID:", self.requisition_id)
        print("Date:", self.date)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("Total:", self.total)
        print("Status:", self.status)
        print("Approval ref:", self.approval_ref)





req = requisition("", "", "", "Pending")
req2 = requisition("", "", "", "Pending")
req3 = requisition("", "", "", "Pending")
req4 = requisition("", "", "", "Pending")
req5 = requisition("", "", "", "Pending")


req.add_requisition()
req.approve_requisition()
req.respond_requisition()
req.display_requisition()

req2.add_requisition()
req2.approve_requisition()
req2.respond_requisition()
req2.display_requisition()

req3.add_requisition()
req3.approve_requisition()
req3.respond_requisition()
req3.display_requisition()

req4.add_requisition()
req4.approve_requisition()
req4.respond_requisition()
req4.display_requisition()

req5.add_requisition()
req5.approve_requisition()
req5.respond_requisition()
req5.display_requisition()

print("Total requisitions submitted:", requisition.counter)
print("Total approved requisitions:", requisition.total_approved_requisitions)
print("Total not approved requisitions:", requisition.total_not_approved)
print("The total number of pending requisitions:", requisition.total_pending_requisitions)


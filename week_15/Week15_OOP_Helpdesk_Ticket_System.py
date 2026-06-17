class ticke:

    ticket_count = 0
    copleted_ticket_count = 0
    in_progress_ticket_count = 0
    closed_tickets_ticket_count = 0


    def __init__(self, ticket_ID, date, employee_ID, employee_name, issue_dedripoion, pryorty):

        self.ticket_ID = ticket_ID
        self.date = date
        self.employee_ID = employee_ID
        self.employee_name = employee_name
        self.issue_dedripoion = issue_dedripoion
        self.pryorty = pryorty
        self.status = "open"


        ticke.ticket_count += 1

    def print_ticket(self):
        print("ticket_ID", self.ticket_ID)
        print("date", self.date)
        print("employee_ID", self.employee_ID)
        print("employee_name", self.employee_name)
        print("issue_dedripoion", self.issue_dedripoion)
        print("status", self.status)

    def auto_reponder(self):
        if self.issue_dedripoion.lower() == "password reset":
            self.status = "resolved"

            print("resolved:", self.status)

            ticke.copleted_ticket_count += 1

            new_password = str(self.employee_ID)[:2] + self.employee_name[:2]
            print("new password:", new_password)

        else:
            self.status = "in progress"
            ticke.in_progress_ticket_count += 1


    def managers_approval(self):
        if self.pryorty == "high":
            print("managers approval needed")
        else:
            print("managers approval not needed")

    def print_ticket_stats(self):
        print("Total tickets:", self.ticket_count)
        print("Completed tickets:",self.copleted_ticket_count)
        print("In progress tickets:", self.in_progress_ticket_count)
        print("closed tickets", self.closed_tickets_ticket_count)

    def close_ticket(self):
        self.status = "closed"
        ticke.closed_tickets_ticket_count += 1

    def display_ticket_info(self):
        print(self.ticket_ID )
        print(self.date)
        print(self.employee_ID)
        print(self.employee_name)
        print(self.issue_dedripoion)
        print(self.pryorty)
        print(self.status)




ticket1 = ticke(1, "10/06/2026", 101, "Jack", "password reset", "low")
ticket2 = ticke(2, "10/06/2026", 102, "Bob", "computer not working", "high")

ticket1.auto_reponder()
ticket2.auto_reponder()

ticket2.managers_approval()

ticket2.close_ticket()

ticket1.print_ticket()
ticket2.print_ticket()

ticket1.print_ticket_stats()















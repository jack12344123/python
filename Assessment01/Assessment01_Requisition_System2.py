def display_requisitions(date, requisition_id, staff_id, staff_name, total, status, approval_ref):
    print("Printing requisitions:")
    print("Date:", date)
    print("Requisition ID:", requisition_id)
    print("Staff ID:", staff_id)
    print("Staff Name:", staff_name)
    print("Total: $" + str(total))
    print("Status:", status)

    if approval_ref is not None:
        print("Approval Reference Number:", approval_ref)
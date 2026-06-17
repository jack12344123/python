def requisition_approval(staff_id, requisition_id, total):
    status = "Pending"
    approval_ref = None
    if total < 500:
        status = "Approved"
        last_three = str(requisition_id)[-3:]
        approval_ref = staff_id + last_three

    return status, approval_ref
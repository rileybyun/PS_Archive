def solution(id_list, report, k):
    total_reported_info = {user: 0 for user in id_list}
    reported_by_whom = {user: set() for user in id_list}
    report_success_emails = {user: 0 for user in id_list}
    
    for report_info in report:
        reporter, reportee = report_info.split()
        if reporter not in reported_by_whom[reportee]:
            total_reported_info[reportee] += 1
            reported_by_whom[reportee].add(reporter)
    
    for reportee, report_count in total_reported_info.items():
        if report_count >= k:
            for reporter in reported_by_whom[reportee]:
                report_success_emails[reporter] += 1
    
    return [email_count for reporter, email_count in report_success_emails.items()]
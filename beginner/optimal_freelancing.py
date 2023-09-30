


def optimalFreelancing(jobs):
    if len(jobs) < 1:
        return 0

    NUMBER_OF_DAYS = 7
        
    work_array = [False] * NUMBER_OF_DAYS
    jobs.sort(key=lambda job: job['payment'], reverse=True)
    profit = 0 
    for job in jobs:
        job_deadline = min(job['deadline'], NUMBER_OF_DAYS)
        for wa in reversed(range(job_deadline)):
            if work_array[wa] == False:
                work_array[wa] = True
                profit = profit + job['payment']
                break

    return profit
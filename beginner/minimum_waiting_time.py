def minimumWaitingTime(queries):
    if len(queries) == 0:
        return 0 
    
    waiting_time = 0
    queries.sort()
    for q_index, q_value in enumerate(queries):
        waiting_time += sum(queries[0:q_index])

    return waiting_time

# We are given an array of positive integers. Each integer in the input array represents the duration of a query that needs to be executed. Only one query can be executed at a time, but the queries can be executed in any order. We are asked to write a function that is going to return the minimum amount of total waiting time for all the queries. We are allowed to mutate the input array.

# Suppose the input array is [1, 3, 2]. The first query can be executed immediately, therefore the waiting time of the first query is 0. The second query have to wait until the first one finishes before it can execute, so the waiting time of the second query is going to be 1 second, the duration of the first query. The third query has to wait for both the first query and the second query to finish executing before it can start. Since the second query takes 3 seconds to execute, the waiting time of the third query is going to be 1 + 3 seconds. So if the queries are executed in that order, then the total awaiting time for all of the queries is going to be (0) + (1) + (1 + 3) = 5.

def minimumWaitingTime(queries):
    if len(queries) == 0:
        return 0 
    
    waiting_time = 0
    queries.sort()
    for q_index, q_value in enumerate(queries):
        waiting_time += sum(queries[0:q_index])

    return waiting_time
"""
Problem description: 
---------
Given a set of N jobs where each jobi has a deadline and profit associated with it.

Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit associated with job if and only if the job is completed by its deadline.

Find the number of jobs done and the maximum profit.

Note: jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job.


Example 1:

Input:
N = 4
jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
Output:
2 60
Explanation:
Job1 and Job3 can be done with
maximum profit of 60 (20+40).
Example 2:

Input:
N = 5
jobs = {(1,2,100),(2,1,19),(3,2,27),
        (4,1,25),(5,1,15)}
Output:
2 127
Explanation:
2 jobs can be done with
maximum profit of 127 (100+27).

Your Task :
You don't need to read input or print anything. Your task is to complete the function jobscheduling() which takes an integer N and an array of jobs(Job id, Deadline, Profit) as input and returns the count of jobs and maximum profit as a list or vector of 2 elements.


Expected Time Complexity: O(NlogN)
Expected Auxilliary Space: O(N)


Constraints:
1 <= N <= 105
1 <= Deadline <= N
1 <= Profit <= 500
"""


class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.profit = profit
        self.deadline = deadline


def job_scheduling(jobs, n):
    # Time complexity: O(n log n)
    # Core idea is to do the highest profit jobs on deadline day to keep space for  other jobs with lower deadline
    # Space complexity: O(n)

    profit = count = 0
    # find the max deadline
    max_deadline = max([job.deadline for job in jobs])

    slots = [False] * (max_deadline + 1)

    jobs.sort(key=lambda x: x.profit, reverse=True)
    for job in jobs:
        slot = job.deadline
        # Try to do the job on the deadline day.
        # If that day is already occupied, then check if the prev day is available
        while slot > 1 and slots[slot]:
            slot -= 1

        if not slots[slot]:
            count += 1
            profit += job.profit
            slots[slot] = True

    return [count, profit]


if __name__ == '__main__':
    print(job_scheduling([Job(1, 2, 100), Job(2, 1, 19), Job(3, 2, 27),
                          Job(4, 1, 25), Job(5, 1, 15)], 5))

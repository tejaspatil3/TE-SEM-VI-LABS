# Jobs, Profit, Slot
profits = [15, 27, 10, 100, 150]
jobs = ["j1", "j2", "j3", "j4", "j5"]
deadlines = [2, 3, 3, 3, 4]

# Combine jobs, profits, deadlines
profitNJobs = list(zip(profits, jobs, deadlines))
# Sort by profit in descending order
profitNJobs.sort(key=lambda x: x[0], reverse=True)

# Find max deadline to size the slot array
max_deadline = max(deadlines)
slots = [0] * (max_deadline + 1)  # slot[0] unused
schedule = ['null'] * (max_deadline + 1)

total_profit = 0

for profit, job, deadline in profitNJobs:
    # Try to schedule the job in the latest available slot
    for j in range(deadline, 0, -1):
        if slots[j] == 0:
            slots[j] = 1
            schedule[j] = job
            total_profit += profit
            break

# Filter out 'null' and show only scheduled jobs
scheduled_jobs = [job for job in schedule if job != 'null']

print("Jobs scheduled:", scheduled_jobs)
print("Total Profit:", total_profit)



# 📊 Dry Run Table
# Step	Job	Deadline	Profit	Slot Assigned	Schedule	Total Profit
# 1	J1	2	100	Slot 1	[_, J1, _]	100
# 2	J3	2	27	Slot 0	[J3, J1, _]	127
# 3	J4	1	25	Skipped	[J3, J1, _]	127
# 4	J2	1	19	Skipped	[J3, J1, _]	127
# 5	J5	3	15	Slot 2	[J3, J1, J5]	142

# 📌 Key Properties
# Greedy Choice: Schedule the most profitable job as late as possible (but before deadline).

# Time Complexity:

# Sorting: O(n log n)

# Scheduling: O(n * d) where d is the max deadline (can be optimized with DSU)

# Result: Maximum total profit with optimal job order.

# 💡 Conceptual Understanding:
# The Job Scheduling Problem is a classic Greedy Algorithm problem. The goal is to maximize total profit if each job takes one unit of time and only one job can be scheduled at a time. Each job has:

# An ID

# A Deadline (latest time it can be completed)

# A Profit (earned if job is completed by or before its deadline)

# ✅ Problem Statement:
# Given a list of jobs where each job has a deadline and profit, schedule the jobs to maximize profit, ensuring:

# A job is scheduled only once.

# It is scheduled before or at its deadline.

# One job per unit time.

# ✅ Greedy Strategy:
# Sort all jobs in descending order of profit.

# Initialize a time slot array with all slots empty.

# For each job:

# Find the latest free slot ≤ job’s deadline.

# If found, assign the job to that slot.

class Job:
    def __init__(self, job_id, arrival_time, burst_time):
        self.job_id = job_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.start_time = 0
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

def fcfs_scheduling(jobs):
    # Sort by arrival time
    jobs.sort(key=lambda x: x.arrival_time)

    current_time = 0
    for job in jobs:
        if current_time < job.arrival_time:
            current_time = job.arrival_time  # CPU waits for the job to arrive
        job.start_time = current_time
        job.completion_time = current_time + job.burst_time
        job.turnaround_time = job.completion_time - job.arrival_time
        job.waiting_time = job.start_time - job.arrival_time
        current_time = job.completion_time

    return jobs

# Example usage
job_list = [
    Job("Job1", 0, 7),
    Job("Job2", 2, 3),
    Job("Job3", 4, 1),
    Job("Job4", 6, 4)
]

scheduled_jobs = fcfs_scheduling(job_list)

print("Job ID | Arrival | Burst | Start | Completion | Waiting | Turnaround")
for job in scheduled_jobs:
    print(f"{job.job_id:^7} | {job.arrival_time:^7} | {job.burst_time:^5} | {job.start_time:^5} | {job.completion_time:^10} | {job.waiting_time:^7} | {job.turnaround_time:^10}")

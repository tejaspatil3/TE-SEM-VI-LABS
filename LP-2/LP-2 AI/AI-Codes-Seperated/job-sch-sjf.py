class Job:
    def __init__(self, job_id, arrival_time, burst_time):
        self.job_id = job_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.start_time = 0
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

def non_preemptive_sjf(jobs):
    # Sort by arrival time first
    jobs.sort(key=lambda x: x.arrival_time)

    completed_jobs = []
    current_time = 0
    while jobs:
        # Get available jobs at current time
        available_jobs = [job for job in jobs if job.arrival_time <= current_time]
        
        if not available_jobs:
            current_time = jobs[0].arrival_time
            continue
        
        # Select job with shortest burst time
        next_job = min(available_jobs, key=lambda x: x.burst_time)
        
        jobs.remove(next_job)

        # Set scheduling times
        next_job.start_time = current_time
        next_job.completion_time = current_time + next_job.burst_time
        next_job.turnaround_time = next_job.completion_time - next_job.arrival_time
        next_job.waiting_time = next_job.start_time - next_job.arrival_time

        current_time = next_job.completion_time
        completed_jobs.append(next_job)
    
    return completed_jobs

# Example usage
job_list = [
    Job("Job1", 0, 7),
    Job("Job2", 2, 4),
    Job("Job3", 4, 1),
    Job("Job4", 5, 4)
]

scheduled_jobs = non_preemptive_sjf(job_list)

print("Job ID | Arrival | Burst | Start | Completion | Waiting | Turnaround")
for job in scheduled_jobs:
    print(f"{job.job_id:^7} | {job.arrival_time:^7} | {job.burst_time:^5} | {job.start_time:^5} | {job.completion_time:^10} | {job.waiting_time:^7} | {job.turnaround_time:^10}")

from job_posting import FullTime, PartTime
from company import Company
from job_seeker import JobSeeker

def main():
    #create JobSeeker, Company instances
    job_seeker = JobSeeker('Serob', 'serob@gmail.com', 'I am Serob Nahapetyan')
    company = Company('Picsar', 'info@picsart.com')


    #create job postings and apply to them
    part_time_job = company.post_part_time_job('Developer', 'Python developer', 200000)
    full_time_job = company.post_full_time_job('Software engineer', 'Python developer with 2 years exp', 400000)
    job_seeker.apply_job(part_time_job, company)
    job_seeker.apply_job(full_time_job, company)

    #review aplications

    company.review_aplicatios()

if __name__ == '__main__':
    main()
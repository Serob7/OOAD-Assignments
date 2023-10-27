from validators import not_empty_string, email_checker
from job_posting import FullTime, PartTime
class Company:
    @not_empty_string('Name', 1)
    @not_empty_string('Contact information', 2)
    @email_checker('Contact information', 2)


    def __init__(self, name, contact_information):
        self.name = name
        self.contact_information = contact_information
        self.posted_jobs = []
        self.aplications = []

    def post_full_time_job(self, title, description, salary):
        posting = FullTime(title, description, salary)
        self.posted_jobs.append(posting)
        print(f'{self.name} posted Full Time job {title}')
        return posting

    def post_part_time_job(self, title, description, salary):
        posting = FullTime(title, description, salary)
        self.posted_jobs.append(posting)
        print(f'{self.name} posted Part Time job {title}')
        return posting

    def review_aplicatios(self):
        print('\tOur company aplicants')
        for application in self.aplications:
            print(f"Aplicant: {application.name}\nEmail: {application.contact_information}\nResume: {application.resume}")

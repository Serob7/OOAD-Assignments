from abc import ABC, abstractmethod
from validators import not_empty_string, email_checker

class Operations(ABC):
    @not_empty_string('Name', 1)
    @email_checker('Contact information', 2)
    @not_empty_string('Resume', 3)
    def __init__(self, name, contact_information, resume):
        self.name = name
        self.contact_information = contact_information
        self.resume = resume

    @abstractmethod
    def apply_job(self, job_posting, company):
        ...


class JobSeeker(Operations):
    def apply_job(self, job_posting, company):
        if job_posting in company.posted_jobs:
            print(f"{self.name} applied to {job_posting.title} at {company.name}")
            company.aplications.append(self)
        else:
            print(f"{company.name} is not looking for {job_posting.title}")

import pandas as pd
from collections import defaultdict
from sqlalchemy import create_engine
from random import randint

batch_size = 1000
insert_count = 1000000

titles = ['Senior Engineering Manager', 'Engineering Manager', 'Development Engineer',
          'Senior Development Engineer', 'Senior Software Engineer', 'Software Engineer', 'QA Engineer']
min_exp_required = [12, 8, 2, 4, 5, 3, 2]
max_exp_required = [16, 11, 4, 6, 7, 4, 4]
min_salary = [6500000, 5500000, 700000, 1500000, 2500000, 1500000, 600000]
max_salary = [8000000, 7000000, 1500000, 3000000, 4500000, 2500000, 1200000]

company_names = ['Microsoft', 'Google', 'Facebook', 'Netflix', 'Apple',
                 'Amazon', 'Pramati', 'Sophos', 'Freshworks', 'Upstox', 'Logmein', 'ServiceNow']
primary_skills = ['Java', 'JavaScript', 'Java, Javascript', 'C++',
                  'Python', 'GoLang', 'Java, SpringBoot', 'JavaScript, React, Angular']
secondary_skills = ['Git, SVN', 'Docker', 'Kubernetes',
                    'AWS/Azure/GCP', 'AWS', 'Distributed Systems', 'System Design']
job_locations = ['Hyderabad', 'Bengaluru', 'New Delhi',
                 'Noida', 'Pune', 'Ahemdabad', 'Chennai']

engine = create_engine('mysql://root:root@localhost/solr_test', echo=False)


def insert_job_listing():

    fake_data = defaultdict(list)

    for _ in range(batch_size):
        index = randint(0, len(titles))-1
        fake_data["title"].append(titles[index])
        fake_data["min_exp_yrs"].append(min_exp_required[index])
        fake_data["max_exp_yrs"].append(max_exp_required[index])
        fake_data["min_salary"].append(min_salary[index])
        fake_data["max_salary"].append(max_salary[index])

        fake_data["organization_name"].append(
            company_names[randint(0, len(company_names)-1)])
        fake_data["locations"].append(
            job_locations[randint(0, len(job_locations)-1)])
        fake_data["primary_skills"].append(
            primary_skills[randint(0, len(primary_skills)-1)])
        fake_data["secondary_skills"].append(
            secondary_skills[randint(0, len(secondary_skills)-1)])

    df_fake_data = pd.DataFrame(fake_data)

    df_fake_data.to_sql('job_listing', con=engine,
                        index=False, if_exists='append')

    return


def batch():
    for _ in range(0, insert_count, batch_size):
        insert_job_listing()
    return


batch()

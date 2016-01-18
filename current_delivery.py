__author__ = 'paul'

#from database.jobs import get_alljobs, find_job, update_job
from crc_lib import now, DUEDATES
import datetime

DUEDATETYPE = 'CRC-Books'
CRC_DUEDATES = [d.lower() for d in DUEDATES[DUEDATETYPE]]


def current_delivery(job_recs, stage):
    # mongo complient
    weeks = [] # The performance in each of three weeks (last, this, next)
               # And a first entry of jobs undelivered before last week
    today = datetime.datetime.today()
    #job_recs = get_alljobs(company = 'MTC', customer = 'CRC')
    start_monday = '{}'.format(thismonday(today))[:10]
    next_monday = '{}'.format(nextmonday(today))[:10]
    last_monday = '{}'.format(lastmonday(today))[:10]
    next_next_monday = '{}'.format(nextmonday(today, days=14))[:10]
    # Find any jobs not delivered before last Monday
    week = {}
    week['title'] = 'Undelivered jobs due before {}'.format(last_monday)
    jobs = get_earlyjobs_no_delivery(job_recs, last_monday, stage)
    #temp_display(jobs, '2014-01-01', last_monday, stage, 'Jobs no delivery date')
    week['jobs'] = format_jobs(jobs, stage)
    weeks.append(week)
    # Jobs that were due last week
    week = {}
    week['title'] = 'Last Week ({} - {}'.format(last_monday, start_monday)
    jobs = get_jobsdueindaterange(job_recs, last_monday, start_monday, stage)
    #temp_display(jobs, last_monday, start_monday, stage, 'Jobs last week')
    week['jobs'] = format_jobs(jobs, stage)
    weeks.append(week)
    # Jobs due this week
    week = {}
    week['title'] = 'This Week ({} - {}'.format(start_monday, next_monday)
    jobs = get_jobsdueindaterange(job_recs, start_monday, next_monday, stage)
    #temp_display(jobs, start_monday, next_monday, stage, 'Jobs this week')
    week['jobs'] = format_jobs(jobs, stage)
    weeks.append(week)
    # Jobs due next week
    week = {}
    week['title'] = 'Next Week ({} - {}'.format(next_monday, next_next_monday)
    jobs = get_jobsdueindaterange(job_recs, next_monday, next_next_monday, stage)
    #temp_display(jobs, next_monday, next_next_monday, stage, 'Jobs next week')
    week['jobs'] = format_jobs(jobs, stage)
    weeks.append(week)
    return weeks

def format_jobs(jobs, stage): # Format for the html page template
    tj = []
    for job in jobs:
        duedate = get_duedate(job, stage)
        actual = get_actual(job, stage)
        j = {}
        j['jobname'] = job['jobname']
        j['duedate'] = duedate
        j['delivered'] = actual
        j['comment'] = job.get('comment:{}'.format(stage),'')
        j['style'] = "width:6em"
        if duedate < actual:
            j['style'] = "background-color:#ff0000;width:6em"
            if not j['comment']:
                j['comment'] = 'LATE - NO COMMENT!!!'
        elif not actual:
            #print (now())
            if duedate < now()[:10]:
                j['style'] = "background-color:#ccff00;width:6em"
        tj.append(j)
    return tj


def get_jobsdueindaterange(job_recs, start, end, stage):
    jobs = []
    for job in job_recs:
        # Get jobs with the stage due date between the monday dates
        duedate = get_duedate(job, stage)
        if duedate >= start and duedate < end:
            jobs.append(job)
    return jobs

def get_earlyjobs_no_delivery(job_recs, end, stage):
        # Also get any earlier jobs that have not been delivered (they are late)
    jobs = []
    for job in job_recs:
        # Get jobs with the stage due date between the monday dates
        duedate = get_duedate(job, stage)
        if duedate and duedate < end:
            actual = get_actual(job, stage)
            if not actual:
                jobs.append(job)
    return jobs


def get_duedate(job, stage):
    ans = ''
    if 'duedates' in job:
        if stage in job['duedates']:
            ans = job['duedates'][stage]
    return ans

def get_actual(job, stage):
    ans = ''
    if 'deliverydates' in job:
        if stage in job['deliverydates']:
            ans = job['deliverydates'][stage]
    return ans



def thismonday(d):
    while d.weekday() != 0: #0 for monday
        d -= datetime.timedelta(days=1)
    return d

def lastmonday(d):
    d -= datetime.timedelta(days=7)
    while d.weekday() != 0: #0 for monday
        d -= datetime.timedelta(days=1)
    return d

def nextmonday(d, days=7):
    d += datetime.timedelta(days=days)
    while d.weekday() != 0: #0 for monday
        d -= datetime.timedelta(days=1)
    return d

"""
def currentdelivery_save(dct):
    # mongo complient
    jobname = dct['updatejob']
    comment = dct['comment']
    stage = dct['stage']
    duedate = dct['duedate']
    delivered = dct['delivered']
    print ('Updating Job')
    print (jobname, comment, stage, duedate)
    job = find_job({'customer':'CRC','jobname': jobname})
    if job:
        job['duedates'][stage] = duedate
        if 'deliverydates' not in job: # Add delivery date dict if not already existing
            job['deliverydates'] = {}
        job['deliverydates'][stage] = delivered
        job['comment:{}'.format(stage)] = comment
        update_job(job)
"""

def temp_display(jobs, start, end, stage, txt): # Currently not used
    print ('-'*70)
    print ('  {} - {} < {} : {}'.format(txt, start,end,stage))
    print ('-'*70)
    for job in jobs:
        duedate = get_duedate(job, stage)
        actual = get_actual(job, stage)
        print ('{:20} : Duedate: {} -  Delivered: {}'.format(job['jobname'],duedate, actual))

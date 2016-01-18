import datetime
from pymongo import MongoClient

DUEDATES = {}

DUEDATES['CRC-Books'] = ['CED', 'Initial', '2ndPages', 'FinalPages','Printer']
DUEDATES['ICE-Articles'] = ['CED','Proofreading', 'XML', 'Corrections', 'FinalPages','Printer']

def get_crc_all_jobs():
    mongo = MongoClient('localhost', 27017 )
    db = mongo.Production
    jobs = db.Jobs
    job_recs = jobs.find({"company":'MTC', "customer":'CRC'})
    return  list(job_recs)

def now():
    x = datetime.datetime.today()
    return datetime.datetime.strftime(x, '%Y-%m-%d-%H-%M-%S')
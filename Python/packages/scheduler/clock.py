from apscheduler.schedulers.blocking import BlockingScheduler
'''
    reference: https://apscheduler.readthedocs.org/en/v3.0.5/userguide.html
'''
sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=3)
def timed_job():
    print('This job is run every three seconds.')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

try:
    sched.start()
except KeyboardInterrupt as e:
    print("\t!! KeyboardInterrupt occured... Task is done...")
    pass

from apscheduler.schedulers.blocking import BlockingScheduler
'''
    reference: https://apscheduler.readthedocs.org/en/v3.0.5/userguide.html
'''
sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=3)
def timed_job():
    """ @sched.scheduled_job annotation에 의해 3초 마다 실행합니다.
    """
    print('This job is run every three seconds.')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    """ @sched.scheduled_job annotation에 의해 월-금요일 오후 5시에 실행합니다 
    """
    print('This job is run every weekday at 5pm.')

try:
    sched.start()
except KeyboardInterrupt as e:
    print("\t!! KeyboardInterrupt occured... Task is done...")
    pass

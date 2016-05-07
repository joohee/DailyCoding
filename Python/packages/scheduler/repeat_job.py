from apscheduler.schedulers.blocking import BlockingScheduler
from time import sleep 

""" apscheduler.schedulers.blocking.BlockingScheduler 를 
    RepeatJob 클래스의 멤버로 설정해놓고 외부에서 시작/종료를 설정할 수 있도록 한다. 

"""
class RepeatJob:
    """ BlockingScheduler()를 멤버변수로 하여 입력받은 job을 실행한다. 
    """
    def __init__(self):
        self.scheduler = BlockingScheduler()
        print("scheduler init...")

    """ job, job_type (e.g. ``date``, ``interval`` or ``cron``), seconds 를 입력받는다. 
    """
    def add_job(self, job, typ, seconds):
        self.scheduler.add_job(job, typ, seconds=seconds)
        print("added interval job: ", job)
    
    """ BlockingScheduler를 실행한다. 
    """
    def start(self):
        self.scheduler.start()

def sample_job():
    print("sample job started...")
    sleep(1)
    print("sample job ended...")

if __name__ == "__main__":
    try:
        repeat_job = RepeatJob()
        repeat_job.add_job(sample_job, 'interval', 3)
        repeat_job.start()
    except (KeyboardInterrupt, SystemExit) as e:
        print("except...", e)
        pass


import os
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

try:
    import asyncio
except ImportError:
    import trollius as asyncio

class AsyncIOJob:
    """
        AsyncIOScheduler를 이용하여 job을 등록하고, 
        실행하는 쪽에서 asyncio.get_event_loop().run_forever() 함수를 통해 
        KeyboardInterrupt/SystemExit 이벤트가 오기 전 까지 실행한다. 
    """

    def __init__(self):
        """ 
            scheduler를 AsyncIOScheduler로 생성한다.
        """
        self.scheduler = AsyncIOScheduler()
        self.scheduler.start()

    def add_job(self, job, typ, seconds):
        """ 
            Job을 등록한다. typ={'date', 'interval', 'cron'} 이 들어갈 수 있다. 
        """
        self.scheduler.add_job(job, typ, seconds=seconds)

def tick():
    print("The Time is: {}".format(datetime.now()))

if __name__ == "__main__":
    asyncIO = AsyncIOJob()
    asyncIO.add_job(tick, 'interval', 3)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit) as e:
        print("error occured....{}".format(e))
        pass


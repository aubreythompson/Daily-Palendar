from apscheduler.schedulers.blocking import BlockingScheduler
from run import fun1
sched = BlockingScheduler()

'''
@sched.scheduled_job('interval', minutes=1)
def timed_job():
    print('This job is run every one minute.')
    fun1()
''''
@sched.scheduled_job('cron', day_of_week='mon-fri', hour=8)
def scheduled_job():
    print('This job is run every weekday at 8 AM.')
    fun1()
sched.start()

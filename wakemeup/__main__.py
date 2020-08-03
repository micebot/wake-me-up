from datetime import datetime
from threading import Event, Thread
from typing import NoReturn

from httpx import get

from wakemeup.env import env


class Job(Thread):
    def __init__(self, callback, event, interval):
        self.callback = callback
        self.event = event
        self.interval = interval
        super(Job, self).__init__()

    def run(self) -> NoReturn:
        while not self.event.wait(self.interval):
            self.callback()


def request(url: str) -> NoReturn:
    response = get(url, timeout=99999)
    print(
        f'Requisição para "{url}" '
        f'realizada em "{datetime.utcnow()}" '
        f'com código HTTP "{response.status_code}".'
    )


def wakeup():
    [request(url=endpoint) for endpoint in env.endpoints]


the_event = Event()

wakeup()
job = Job(wakeup, the_event, env.interval)
job.start()

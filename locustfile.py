import uuid

from locust import TaskSet, task, between
from locust.contrib.fasthttp import FastHttpLocust


class MyTaskSet(TaskSet):
    @task
    def index(self):
        self.client.post("/dynamodb", data={'uuid': str(uuid.uuid4())})


class MyLocust(FastHttpLocust):
    task_set = MyTaskSet
    wait_time = between(1, 1)

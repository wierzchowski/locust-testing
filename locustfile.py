import uuid

from locust import TaskSet, task, between
from locust.contrib.fasthttp import FastHttpLocust


class MyTaskSet(TaskSet):
    @task
    def index(self):
        self.client.post("/dynamodb-asynch", data={'uuid': str(uuid.uuid4())})
        # self.client.get("/healthcheck")


class MyLocust(FastHttpLocust):
    task_set = MyTaskSet
    wait_time = between(0.001, 0.001)

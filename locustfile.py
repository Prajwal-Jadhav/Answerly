import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def hello_world(self):
        self.client.get("/", verify=False)

    @task(3)
    def view_items(self):
        for item_id in range(1, 3):
            self.client.get(f"/questions/{item_id}", name="/questions", verify=False)
            time.sleep(1)


    def on_start(self):
        self.client.verify = False
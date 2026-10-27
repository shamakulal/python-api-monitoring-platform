from locust import HttpUser, task, between


class APIUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def check_health(self):
        self.client.get("/health")
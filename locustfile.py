from locust import HttpUser, task
SERVER_IP_ADDR = "134.0.112.20"


class LoadTestingBraniacLMS(HttpUser):
    @task
    def test_some_pages_open(self):
        # Mainapp
        self.client.get(f"http://{SERVER_IP_ADDR}/mainapp/")
        self.client.get(f"http://{SERVER_IP_ADDR}/mainapp/courses/")
        self.client.get(f"http://{SERVER_IP_ADDR}/mainapp/courses/1/")
        self.client.get(f"http://{SERVER_IP_ADDR}/mainapp/news/")
        self.client.get(f"http://{SERVER_IP_ADDR}/mainapp/news/1/detail")
        self.client.get(f"http://{SERVER_IP_ADDR}/mainapp/contacts/")
        self.client.get(f"http://{SERVER_IP_ADDR}/mainapp/doc_site/")
        # Authapp
        self.client.get(f"http://{SERVER_IP_ADDR}/authapp/register/")
        self.client.get(f"http://{SERVER_IP_ADDR}/authapp/login/")

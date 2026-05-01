from locust import User, task, between

class MyUser(User):
    wait_time = between(5, 15)

    @task
    def my_task_one(self):
        print("Hello, Locust!")

    @task
    def my_task_two(self):
        print("Hello again, Locust!")

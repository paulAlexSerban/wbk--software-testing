from locust import TaskSet, task, User, between, events

# execute only once before and after suite
@events.test_start.add_listener
def on_test_start():
    print("... initiating load test ... ON_TEST_START")


@events.test_stop.add_listener
def on_test_stop():
    print("... load test finished ... ON_TEST_STOP")


class SearchProduct(TaskSet):
    # execute for each taskset execution
    def on_start(self):
        print('search product: task execution started')

    def on_stop(self):
        print('search product: task execution stopped')

    @task
    def search_men_products(self):
        print("Searching for men's products...")

    @task
    def search_kids_products(self):
        print("Searching kids products")
        
    @task
    def exit_task_execution(self):
        self.interrupt()


class MyUser(User):
    
    wait_time = between(1, 2)
    tasks = [SearchProduct]
    
    # execute for each user locust hatch
    def on_start(self):
        print('my user: hatching new user')

    def on_stop(self):
        print('my user: stopping user')
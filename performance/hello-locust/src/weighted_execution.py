from locust import TaskSet, task, User, between

class SearchProduct(TaskSet):
    @task(4)
    def search_men_products(self):
        print("Searching for men's products...")
        
    @task(1)
    def search_kids_products(self):
        print("Searching kids products")
        
class MyUser(User):
    wait_time = between(1, 2)
    tasks = [SearchProduct]
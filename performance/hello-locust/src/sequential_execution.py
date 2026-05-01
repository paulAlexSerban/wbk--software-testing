from locust import task, User, between, SequentialTaskSet

class SearchProduct(SequentialTaskSet):
    @task
    def search_men_products(self):
        print("Searching for men's products...")
        
    @task
    def search_kids_products(self):
        print("Searching kids products")
        
class MyUser(User):
    wait_time = between(1, 2)
    tasks = [SearchProduct]
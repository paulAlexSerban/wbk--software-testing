from locust import task, User, between, SequentialTaskSet


class SearchProduct(SequentialTaskSet):
    @task
    def search_men_products(self):
        print("Searching for men's products...")

    @task
    def search_kids_products(self):
        print("Searching kids products")

    @task
    def exit_task_execution(self):
        self.interrupt()


class ViewCart(SequentialTaskSet):
    @task
    def get_cart_items(self):
        print("Getting cart items...")

    @task
    def search_cart_items(self):
        print("Searching cart items...")

    @task
    def exit_task_execution(self):
        self.interrupt()


class MyUser(User):
    wait_time = between(1, 2)
    tasks = [SearchProduct, ViewCart]

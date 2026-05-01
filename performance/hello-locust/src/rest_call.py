from locust import SequentialTaskSet, task, HttpUser

class ViewBlogPost(SequentialTaskSet):

    @task
    def view_post(self):
        with self.client.get("/blog/dealing-with-anxious-dogs-during-grooming-tips-and-tricks", catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to view post: " + str(response.status_code))
            else:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure("Failed to view post: " + str(response.status_code))

    @task
    def exit_navigation(self):
        self.interrupt()

class MyUser(HttpUser):
    tasks = [ViewBlogPost]
from user import User
from post import Post
app_user_one = User("vg@vg.com", "Vaibhav Goyal", "pwd1", "system engineer")
app_user_one.get_user_info()

app_user_two = User("aa@aa", "goyal", "pwd2", "Devops")
app_user_two.get_user_info()

new_post = Post("On Secret mission today", app_user_two.name)
new_post.get_post_info()

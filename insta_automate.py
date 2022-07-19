from instabot import Bot
bot = Bot()
# login instagram
bot.login(username = "mr____gaddam" , password = "shailesh123")
# follow user
bot.follow("virat.kohli")
# upload photos on instagram
# bot.upload("/PHOTO PATH/" , Caption = "I'm a Python Programmer")
# unfollow user
bot.unfollow("virat.kohli")
# sending multiple messages
bot.send_message("I love Python" , ["virat.kohli", "ishankishan23"])
# info of the followers
followers = bot.get_user_followers("mr____gaddam")
for i in followers:
    print(bot.get_user_info(i))

following = bot.get_user_following("mr____gaddam")
for i in following:
    print(bot.get_user_info(i))
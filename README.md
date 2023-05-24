# Social network

This project allows you to create posts, like and comment posts, follow on another user and view your feed.  
You can try this API [here](http://16.16.210.18/docs)

## Endpoints

1. default

* "/" - You can check if you authorized user.

2. auth

* "/auth/register/" - You can create user.
* "/auth/jwt/login/" - You can login.
* "/auth/jwt/logout/" - You can logout.

3. posts

* "/post/create/" - Create post with text and with file (not required).
* "/post/{id}/" - Check another post.
* "/post/like/{id}/" - Like or dislike post.
* "/post/comment/add/{id}/" - Leave comment.
* "/post/comment/view/{id}/" - View comments for post.

4. users

* "/user/me/" - Get information about yours user.
* "/user/{username}/" - Get information about another user
* "/user/follow/{username}/" - Follow or unfollow to another user. Follow will help you to get yours feed.

5. feed

* "/feed/" - Gives you the newest posts from yours followed user.

6. message

* "/messages/" - You can check or send message.

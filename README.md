# Newspaper_App

This web application is written in Django and Bootstrap. It allows logged in users to post articles and edit the articles that they posted.

## Skills that I learned:

1. Model-view-controller software design pattern in Django. Specifically, how to route pages to eachother.
2. Create, read, update, delete functionality.
3. Template Inheritance, HTML and CSS.
4. Django's ORM management. Specifically, how to set fields to models and set up many-to-one relationships in class-based views.

## Highlight
I created a ArticleCommentView that allowed the users to add comments to the articles without the admin's moderation. I used the article's primary key to attach the article to the commment when the comment was created. Big thanks to u/onosendi for helping me with this: https://www.reddit.com/r/django/comments/fy1x3g/comments_do_not_appear_under_article_without/

The most interesting apect of this project was using Django's mixins to ensure that only the users that created the articles can edit them afterward.




## Any suggestions are greatly appreciated: jamesbot@seas.upenn.edu

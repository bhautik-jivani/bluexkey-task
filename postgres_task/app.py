# app.py

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:SuperSecret!1@localhost/pg_db_task_1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from myapp.models import *

@app.route('/')
def index():
    users = User.query.all()
    posts = Post.query.all()
    comments = Comment.query.all()
    tags = Tag.query.all()
    categories = Category.query.all()

    return render_template('index.html', users=users, posts=posts, comments=comments, tags=tags, categories=categories)

@app.route('/insert_static_data', methods=['POST'])
def insert_static_data():
    # Insert static data into User table
    user1 = User(username='user1', email='user1@example.com')
    user2 = User(username='user2', email='user2@example.com')
    db.session.add_all([user1, user2])
    db.session.commit()

    # Insert static data into Post table
    post1 = Post(title='Post 1', content='Content of post 1', user_id=user1.id)
    post2 = Post(title='Post 2', content='Content of post 2', user_id=user2.id)
    db.session.add_all([post1, post2])
    db.session.commit()

    # Insert static data into Comment table
    comment1 = Comment(text='Comment on post 1', user_id=user1.id, post_id=post1.id)
    comment2 = Comment(text='Comment on post 2', user_id=user2.id, post_id=post2.id)
    db.session.add_all([comment1, comment2])
    db.session.commit()

    # Insert static data into Tag table
    tag1 = Tag(name='Tag 1')
    tag2 = Tag(name='Tag 2')
    db.session.add_all([tag1, tag2])
    db.session.commit()

    # Insert static data into Category table
    category1 = Category(name='Category 1')
    category2 = Category(name='Category 2')
    db.session.add_all([category1, category2])
    db.session.commit()

    return "Static data inserted successfully!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

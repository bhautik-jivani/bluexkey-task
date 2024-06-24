# myapp/tests/test_database.py

import pytest
from app import app, db
from myapp.models import User, Post, Comment, Tag, Category

@pytest.fixture(scope='module')
def setup_database():
    """ Fixture to set up the database for testing. """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:SuperSecret!1@localhost/pg_db_task_1'  # Use a test database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()
        yield db  # Provide the fixture object

        # Teardown
        db.session.remove()
        db.drop_all()

def test_insert_user(setup_database):
    """ Test inserting a User into the database. """
    user = User(username='testuser', email='testuser@example.com')
    db.session.add(user)
    db.session.commit()

    assert User.query.filter_by(username='testuser').first() is not None

def test_insert_post(setup_database):
    """ Test inserting a Post into the database. """
    user = User(username='testuser', email='testuser@example.com')
    db.session.add(user)
    db.session.commit()

    post = Post(title='Test Post', content='This is a test post.', user_id=user.id)
    db.session.add(post)
    db.session.commit()

    assert Post.query.filter_by(title='Test Post').first() is not None

def test_insert_comment(setup_database):
    """ Test inserting a Comment into the database. """
    user = User(username='testuser', email='testuser@example.com')
    db.session.add(user)
    db.session.commit()

    post = Post(title='Test Post', content='This is a test post.', user_id=user.id)
    db.session.add(post)
    db.session.commit()

    comment = Comment(text='Test comment', user_id=user.id, post_id=post.id)
    db.session.add(comment)
    db.session.commit()

    assert Comment.query.filter_by(text='Test comment').first() is not None

def test_insert_tag(setup_database):
    """ Test inserting a Tag into the database. """
    tag = Tag(name='Test Tag')
    db.session.add(tag)
    db.session.commit()

    assert Tag.query.filter_by(name='Test Tag').first() is not None

def test_insert_category(setup_database):
    """ Test inserting a Category into the database. """
    category = Category(name='Test Category')
    db.session.add(category)
    db.session.commit()

    assert Category.query.filter_by(name='Test Category').first() is not None

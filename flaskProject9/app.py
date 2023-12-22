from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/SportsNewsDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database model for News
class News(db.Model):
    NewsID = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(255))
    Content = db.Column(db.Text)
    Category = db.Column(db.String(100))
    PublishDate = db.Column(db.DateTime)
    Source = db.Column(db.String(255))
    Views = db.Column(db.Integer, default=0)

# Database model for Users
class User(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(100))
    Password = db.Column(db.String(100))
    Email = db.Column(db.String(100))
    Role = db.Column(db.String(50))
    ProfilePic = db.Column(db.String(255))
    RegisteredDate = db.Column(db.DateTime, default=datetime.utcnow)

# Database model for ChatLogs
class ChatLog(db.Model):
    LogID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('user.UserID'))
    Message = db.Column(db.Text)
    Timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Database model for UserRecommendations
class UserRecommendation(db.Model):
    RecommendationID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('user.UserID'))
    NewsID = db.Column(db.Integer, db.ForeignKey('news.NewsID'))
    Score = db.Column(db.Float)

# Database model for Comments
class Comment(db.Model):
    CommentID = db.Column(db.Integer, primary_key=True)
    NewsID = db.Column(db.Integer, db.ForeignKey('news.NewsID'))
    UserID = db.Column(db.Integer, db.ForeignKey('user.UserID'))
    Content = db.Column(db.Text)
    CommentDate = db.Column(db.DateTime, default=datetime.utcnow)

# Database model for UserPreferences
class UserPreference(db.Model):
    PreferenceID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('user.UserID'))
    PreferenceType = db.Column(db.String(100))
    Value = db.Column(db.String(100))

# Database model for Categories
class Category(db.Model):
    CategoryID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))

# Route definitions
@app.route('/')
def homepage():
    return render_template('homepage.html')

# Define other routes as needed...

if __name__ == '__main__':
    app.run(debug=True)

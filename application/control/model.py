from application.control.extentions import db

class trending_data(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    # String muotoa dd-mm-yyyy
    date_string = db.Column(db.String(10), nullable=False)
    # JSON muotoinen String
    trends_string = db.Column(db.Text, nullable=False)

    def __repr__(self) -> str:
        return "Added trending data for: %r" % self.date_string
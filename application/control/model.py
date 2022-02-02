from application.control.extentions import db

# Muistiinpano: kuinka luoda database contextilla
# >>> python
# >>> from application.control.extentions import db
# >>> from application import create_app            
# >>> db.create_all(app=create_app())

class trending_data(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    # String muotoa dd-mm-yyyy
    date_string = db.Column(db.String(10), nullable=False, unique=True)
    # JSON muotoinen String
    trends_string = db.Column(db.Text, nullable=False)

    db.UniqueConstraint(date_string)

    def __repr__(self) -> str:
        return "Added trending data for: %r" % self.date_string
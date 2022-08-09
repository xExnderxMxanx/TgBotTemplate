from sqlalchemy import Column, Integer

from dispatcher import model

class User(model):
    __tablename__ = 'Users'
    
    id = Column("id", Integer, primary_key=True, autoincrement=True, unique=True)
    user_id = Column("user_id", Integer, unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.user_id}>'
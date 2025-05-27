from db.model import User, session


def add_user_to_db(id_, name, address, contact):
    user = User(id=id_, name=name, location=address, contact=contact)
    session.add(user)
    session.commit()

def select_user_from_db(id_):
    user = session.query(User).filter(User.id == id_).first()
    if user is None:
        return None
    return user.name, user.location, user.contact
from flask_login import UserMixin


class User(UserMixin):
    pass


def query_user(user_id):
    if user_id == 'ruanzhen1234@126.com':
        ret = ["ruanzhen1234@126.com", "jianming"]
    else:
        ret = None
    return ret


'''def register_user(email, passwd):
    #  Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yg_userlogin = Userlogin(email=email, passwd=passwd)
    session.add(yg_userlogin)
    session.commit()'''

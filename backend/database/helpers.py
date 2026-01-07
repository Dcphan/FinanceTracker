from sqlalchemy import exists

def data_exists(session, table, **filters):
    return session.query(table).filter_by(**filters).first() is not None


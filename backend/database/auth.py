from database.session import SessionStorage
from database.helpers import data_exists
from datetime import datetime, timedelta
from sqlalchemy import update, insert
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

def insert_refresh_token(db: Session, user_id, refresh_token, expired_time):
    # UpSert
    insert_stmt = insert(SessionStorage).values(refresh_token = refresh_token, user_id=user_id, expired_at = datetime.now() + timedelta(minutes=expired_time))
    do_update_stmt = insert_stmt.on_conflict_do_update(
        index_elements = ['user_id'],
        set_= dict(refresh_token= refresh_token, expired_at = datetime.now() + timedelta(minutes=expired_time))
    )

    db.execute(do_update_stmt)
    db.commit()
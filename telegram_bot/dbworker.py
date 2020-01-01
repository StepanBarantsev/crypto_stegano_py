from vedis import Vedis
import dbconfiguration


def get_current_state(user_id):
    with Vedis(dbconfiguration.db_file) as db:
        try:
            return db[user_id].decode()
        except KeyError:
            return dbconfiguration.MAIN


def set_state(user_id, value):
    with Vedis(dbconfiguration.db_file) as db:
        try:
            db[user_id] = value
            return True
        except:
            return False

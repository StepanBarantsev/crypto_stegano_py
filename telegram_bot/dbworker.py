from vedis import Vedis
import dbconfiguration
import shelve


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


def set_data(user_id, field, data):
    with shelve.open(dbconfiguration.db_file_data, writeback=True) as db:
        if str(user_id) not in db:
            db[str(user_id)] = {}
        db[str(user_id)][field] = data


def clear_data(user_id):
    with shelve.open(dbconfiguration.db_file_data, writeback=True) as db:
        db[str(user_id)] = {}


def get_data(user_id, field):
    with shelve.open(dbconfiguration.db_file_data) as db:
        return db[str(user_id)][field]


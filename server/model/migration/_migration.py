from datetime import datetime
import logging

log = logging.getLogger('migration')
log.setLevel(logging.DEBUG)

migrate_funcs = []

def migrate(time_stamp, migration):
    log.debug(f"wrap {migration}")
    def migrate_decorator(func):
        def wrapper(migrated, *args, **kwargs):
            if migrated.data().filter(lambda x: x['migration'] == migration).has_content():
                return

            log.info('Migration: ' + migration)
            doc = {
                'migration': migration,
                'time_stamp': time_stamp,
                'started': datetime.now()}
            func(*args, **kwargs)
            doc['completed'] = datetime.now()
            migrated.insert_one(doc)

        # add the wrapper to the list of migrations
        # if it hasn't already been called, then it will
        # be called once and recorded in the database
        migrate_funcs.append(wrapper)
        return func

    return migrate_decorator


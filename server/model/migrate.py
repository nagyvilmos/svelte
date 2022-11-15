"""
    Database migration
    Set up the initial db content and amend as required
    Any method with the migrate decorator is run if not called before according to the 'migrated' collection
"""

import logging
from json_store import get_store
from .migration._migration import migrate_funcs 

log = logging.getLogger('migration')
log.setLevel(logging.DEBUG)

log.debug(f"migrations: {len(migrate_funcs)}")

def set_model():
    global store, migrated
    store = get_store()
    migrated = store.get("migrated")
    for func in migrate_funcs:
        func(migrated, store)
    log.info('db up to date')

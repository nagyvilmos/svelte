from ._migration import migrate

@migrate('2022-04-04-1400', 'create admin user')
def users(db):
    db.get("user").insert_one({'name': 'admin'}, False)

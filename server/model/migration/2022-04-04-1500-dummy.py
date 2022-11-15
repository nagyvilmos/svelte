from ._migration import migrate, log

@migrate('2022-04-04-1500', 'Dummy test')
def create_new_stuff(db):
    db.get("dummy").insert_many([
        {'this': 'that', 'age': 4},
        {'this': 'other', 'age': 17}
    ])

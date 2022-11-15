from ._migration import migrate
@migrate('2022-10-14-1120', 'Add password')
def add_password(db):
    user=db.get("user")
    db.get("dummy").insert_many([
        {'this': 'that', 'age': 4},
        {'this': 'other', 'age': 17}
    ])

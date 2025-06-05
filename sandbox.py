import uuid


from uuid import uuid1, uuid3

import uuid

def generate_short_id():
    return uuid.uuid4().hex[:6]  # First 6 characters of the UUID

id = generate_short_id()
print(id)
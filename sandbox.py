import uuid


from uuid import uuid1, uuid3

import uuid

def generate_short_id(item_type):
    item_type = item_type.lower()
    if item_type == "user":
        return f"C{uuid.uuid4().hex[:4]}"  # First 4 characters of the UUID
    elif item_type == "flight":
        return f"F{uuid.uuid4().hex[:4]}"
    else:
        pass

flight = "flight"
id = generate_short_id(flight)
print(id)
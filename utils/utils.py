import random
import uuid

# Register your models here.

class Utility:
    def generate_uuid(self):
        return str(uuid.uuid4())

    def is_empty(self, _string: str):
        if _string and _string.strip(" \n\r"):
            return False
        return True

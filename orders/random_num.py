import random
import string


def randomStringNumber():
    stringLength = 5
    """Generate a random string of fixed length """
    letters = string.ascii_uppercase + string.digits
    r = ''.join(random.choice(letters) for i in range(stringLength))
    return r


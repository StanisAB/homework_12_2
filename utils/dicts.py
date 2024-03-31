
def get_val(collection, key, default='git'):

    if collection.get(key) == None:
        return default
    else:
        return collection.get(key)


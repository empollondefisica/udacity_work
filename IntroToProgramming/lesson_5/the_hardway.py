
def make_hashtable(nbuckets):
    table = []
    for i in range(0, nbuckets):
        table.append([])

    return table

def hash_string(keyword, buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def hashtable_get_bucket(hashtable, keyword):
    nbuckets = len(hashtable)
    hashVal = hash_string(keyword, nbuckets)
    return hashtable[hashVal]

def hashtable_add(htable, word, value):
    pair = [word, value]
    bucket = hashtable_get_bucket(htable, word)
    bucket.append(pair)

def hashtable_lookup(htable, word):
    bucket = hashtable_get_bucket(htable, word)
    for entry in bucket:
        if entry[0] == word:
            return entry[1]
    return None

def hashtable_update(htable, key, value):
    my_value = hashtable_lookup(htable, key)
    bucket = hashtable_get_bucket(htable, key)

    if my_value == None:
        entry = [key, value]
        bucket.append(entry)
    else:
        for entry in bucket:
            if entry[0] == key:
                entry[1] = value
        
    return htable


table = [[['Francis', 13], ['Ellis', 11]], [], [['Bill', 17], ['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]]
print hashtable_get_bucket(table, "Zoe")

print hashtable_lookup(table, 'Carl')
print hashtable_update(table, 'Francis', 24)

import hashlib



h = hashlib.sha1()
h.update(b"password")
print(h.hexdigest())
def extract_full_name(names):
    return list(map(lambda o: "{0} {1}".format(o["first"], o["last"]), names))


names = [{"first": "Elie", "last": "Schoppik"}, {"first": "Colt", "last": "Steele"}]
print(extract_full_name(names))  # ['Elie Schoppik', 'Colt Steele']

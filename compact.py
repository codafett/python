def compact(values):
    return [val for val in values if val]


print(compact([0, 1, 2, "", [], False, {}, None, "All done"]))  # [1,2, "All done"]

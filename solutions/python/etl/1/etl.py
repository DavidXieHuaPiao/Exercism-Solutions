def transform(legacy_data):
    result={}
    for key, value in legacy_data.items():
        for letter in value:
            result[letter.lower()] = key
    result_sorted = dict(sorted(result.items()))
    return result_sorted

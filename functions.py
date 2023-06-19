def function_to_filter(value, data):
    filter_by_word = value
    result = filter(lambda one_string: filter_by_word in one_string, data)
    return list(result)


def function_to_map(value, data):
    column = int(value)
    result = map(lambda one_string: one_string.split(' ')[column], data)
    return list(result)


def function_to_limit(value, data):
    count_of_string = int(value)
    result = data[0:count_of_string]
    return result


def function_to_unique(value: str, data):
    value = ""
    return list(set(data))


def function_to_sort(value, data):
    if value == "asc":
        flag_reverse = False
    else:
        flag_reverse = True

    result = sorted(data, reverse=flag_reverse)
    return result

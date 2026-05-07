def get_dict_value(d, key):
    try:
        value = d[key]
    except KeyError as e:
        print(f"Error: {e}")
        value = None
    finally:
        print("Execution complete.")
    return value


d = {'a': 1, 'b': 2, 'c': 3}
print(get_dict_value(d, 'b'))  # 2
print(get_dict_value(d, 'x'))  # None
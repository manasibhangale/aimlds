def get_value_at_index(list,index):
    try:
        value=list[index]
    except IndexError as e:
        print(f" Error: {e}")
        value=None
    finally:
        print("execution completed")
    return value
list=[1,2,3,4,5,6]
print(get_value_at_index(list,5))
print(get_value_at_index(list,9))
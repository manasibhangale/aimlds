def write_strings_to_file(strings, filename):
    try:
        file = open(filename, 'w')
        for string in strings:
            file.write(string + '\n')
    except IOError as e:
        print(f"Error: {e}")
    finally:
        try:
            file.close()
        except NameError:
            pass

# Test
write_strings_to_file(['Hello', 'World'], 'output.txt')
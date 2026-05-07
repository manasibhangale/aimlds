def read_a_file(filename):
    try:
        file=open(filename,'r')
        content=file.read()
        print(content)

    except FileNotFoundError as ex:
        print(f"error {ex}")

    finally:

        try:
            file.close()

        except NameError:
            pass
        
read_a_file("demo.txt")
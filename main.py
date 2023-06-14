from func import open_file_json
from classes.operations import Operations


def main():
    operations = open_file_json('operations.json')
    operations = Operations(operations)
    operations.last_five_operations()
    operations.__repr__()



if __name__ == '__main__':
    main()

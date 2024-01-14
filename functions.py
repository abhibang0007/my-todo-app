def get_todos(filepath='todos.txt'):  # default file path define in the function
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='todos.txt'):  # default file path define in the function
    """ Write content of given list
    in specified text file.
    """
    with open(filepath, 'w') as file_w:
        file_w.writelines(todos_arg)


"""Below condition use to run 
selected code lines in this function only 
and no in the main function """

if __name__=="__main__":
    print(get_todos())
def file_read(file_name):

    return_data = {
        'output': None,
        'error': None
    }

    try:
        file = open(file_name, 'r')
    except FileNotFoundError as error:
        return_data['output'] = False
        return_data['error'] = error
    except UnicodeDecodeError as error:
        return_data['output'] = False
        return_data['error'] = error
    except IsADirectoryError as error:
        return_data['output'] = False
        return_data['error'] = error
    else:
        return_data['output'] = file.read()
        file.close()
    finally:
        return return_data


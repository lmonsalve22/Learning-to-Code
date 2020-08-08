def get_formatted_name(first, last, middle=''):
    """ Generate a neatly formatted full name """
    if middle:
        return f'{first.title()} {middle.title()} {last.title()}'
    else:
        return f'{first.title()} {last.title()}'

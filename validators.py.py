def text(value):
    while True:
        text=input(value)
        if text=="":
            print('Value should not be empty')
            continue
        return text.strip().title()

def digit(value):
    while True:
        digit=input(value)
        if digit=='':
            print('Value should not be empty')
            continue
        elif not digit.isdigit():
            print('Values should be numbers')
            continue
        return int(digit)

def classification(value):
    while True:
        classification=input(value).lower()
        if classification not in ['yes','no']:
            print('Choose (Yes/No)')
            continue
        return classification


def common_fields():
    isbn=digit('Enter ISBN Number')
    title=text('Book Title')
    author=text('Author Name')
    publisher=text('Publishing Company')
    edition=text('Book Edition')
    publication_year=text('Year of publication')
    language=text('Language of book (eg:English/Telugu..)')
    total_copies=digit('Total no.of copies of book')
    while True:
        available_copies=digit('Available copies of book')
        if available_copies>total_copies:
            print('Available copies cannot be greater than total copies')
            continue
        break
    
    data={
    'ISBN':isbn,
    'TITLE':title,
    'AUTHOR':author,
    'PUBLISHER':publisher,
    'EDITION':edition,
    'PUBLICATION_YEAR':publication_year,
    'LANGUAGE':language,
    'TOTAL_COPIES':total_copies,
    'AVAILABLE_COPIES':available_copies,
    'CONDITION':text('Condition of book (eg:Good/Damaged)'),
    'ACQUISITION_DATE':text('When Library bought it'),
    'RACK':digit('Rack Number'),
    'SHELF':digit('Shelf Number')
    
        }
    return data

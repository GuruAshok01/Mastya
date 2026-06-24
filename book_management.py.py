#importing reusable input Validaion and common field funcion 
import repeating_functions_for_iterations as rep

#Separate dictionaries used to store books by category
#ISBN is used as the unique key and book details are stored as values
competitive_books={}
rare_books={}
magazines={}
sc_books={}
spiritual_books={}
academic_textbooks={}


#Collect and store Competitive Exam book information 
def competitive_book():
    print()
    print('COMPETITIVE EXAM BOOK INFORMATION FORM')
    print()
    while True:
        common_data=rep.common_fields()

        exam_type=rep.text('UPSC/GATE/CAT/BANKING')
        subject_area=rep.text('Enter subject/topic covered by this book')
        dificulty_level=rep.text('Choose whether the resource is (Beginner/Intermediate/Advanced)')
        practice_questions=rep.classification('Is practice questions included (Yes/No)')
        summary=rep.text('Description about the book')

        common_data.update({
        'CATEGORY':'Competitive Exam',
        'EXAM_TYPE':exam_type,
        'SUBJECT_AREA':subject_area,
        'DIFFICULTY_LEVEL':dificulty_level,
        'PRACTICE_QUESTIONS':practice_questions,
        'LATEST_EDITION':rep.text('Latest Edition Year'),
        'SUMMARY':summary
 
            })
        competitive_books[common_data['ISBN']]=common_data

        print()
        print('Information Added Succesfully')
        print('*'*50)
        break

#Collect and store Rare Book information
def rare_book():
    print()
    print('RARE BOOKS INFORMATION FORM')
    print()
    while True:
        common_data=rep.common_fields()

        rarity_level=rep.text('Rarity Level (eg:Rare/Very Rare')
        historical_period=rep.text('Historical period (eg:Century/Era)')
        price=rep.digit('Estimated Historical price')
        archive_location=rep.text('Special archive section')
        summary=rep.text('Description about the book')
        digital_availability=rep.classification('Is Digital copy available (Yes/No)')

        common_data.update({
        'CATEGORY':'Rare Book',
        'RARITY_LEVEL':rarity_level,
        'HISTORICAL_PERIOD':historical_period,
        'PRICE':price,
        'ARCHIVE_LOCATION':archive_location,
        'SUMMARY':summary,
        'DIGITAL_AVAILABILITY':digital_availability
            })

        rare_books[common_data['ISBN']]=common_data
        print()
        print('Information Added Successfully')
        print('*'*50)
        break

#Collect and store Magazine information
def magazine():
    print()
    print('MAGAZINES INFORMATION FORM')
    print()
    while True:
        #taking magazine details
        common_data=rep.common_fields()
        common_data.update({
        'CATEGORY':'Magazine',
        'VOLUME_NUMBER':rep.text('Volume Number'),
        'ISSUE_NUMBER':rep.text('Issue Number'),
        'PUBLICATION_MONTH':rep.text('Month of Issue'),
        'PUBLICATION_YEAR':rep.digit('Publicatoin Year'),
        'PUBLICATION_FREQUENCY':rep.text('Publication frequency (eg:Weekly/Monthly)'),
        'SUMMARY':rep.text('Description about Magazine'),
        'DIGITAL_AVAILABILITY':rep.classification('Is Digitally Available (Yes/No)')
            })
        #adding data to dictionary
        magazines[common_data['ISBN']]=common_data
        print()
        print('Information Added Succesfully')
        print('*'*50)
        break

#Collect and store SC/ST educational resource information   
def sc_st_books():
    print()
    print('SC/ST BOOKS FORM')
    print()
    while True:
        common_data=rep.common_fields()
        common_data.update({
        'CATEGORY':'Aptitude And Resoning',
        'PROGRAM_TYPE':rep.text('Select educational support program\n eg:1.SC Study Circle\n 2.ST Study Circle\n 3.Government Coaching Scheme\n 4.Competitive Exam Training Program'),
        'SUBJECT_FOCUS':rep.text('Enter the main subject covered by this resource (eg:Aptitude\Resoning..)'),
        'SPONSORED_BY':rep.text('Enter sponsoring organization'),
        'TRAINING_MATERIAL':rep.classification('Is this resource part of a training program? (Yes/No)'),
        'SUMMARY':rep.text('Description about the book'),
        'DIGITAL_AVAILABILITY':rep.classification('Is Digitally Available (Yes/No)')
            })
        sc_books[common_data['ISBN']]=common_data
        print()
        print('Information Added Succesfully')
        print('*'*50)
        break
    
#Collect and store Spiritual book information
def spiritual():
    print()
    print('SPIRITUAL BOOK INFORMATION')
    print()
    while True:
        common_data=rep.common_fields()
        common_data.update({
        'CATEGORY':'Spiritual',
        'RELIGION':rep.text('Select the Religion (eg:Hindu/Buddhist/etc..)'),
        'SCRIPTURE_TYPE':rep.text('Select the type of scripture (eg:Sacred text/prayer book/biography/devotional literature)'),
        'PHILOSOPHY_BRANCH':rep.text('Philosophy branch (eg:Vedanta/Yoga/Bhakti/Tantra..)'),
        'TRANSLATOR':rep.text('Enter translator name if the book is translated'),
        'SUMMARY':rep.text('Descriptoin about the book'),
        'DIGITAL_AVILABILITY':rep.classification('Is Digitally Available (Yes/No)')
        
             })

        spiritual_books[common_data['ISBN']]=common_data
        print()
        print('Information Added Succesfully')
        print('*'*50)
        break

#Collect and store Academic Textbook information
def academic_book():
    print()
    print('ACADEMIC BOOKS INFORMATION')
    print()
    while True:
        common_data=rep.common_fields()
        common_data.update({
        'CATEGORY':'Academic Book',
        'SUBJECT_NAME':rep.text('Subject Name'),
        'COURSE_CODE':rep.text('Course Code'),
        'SUMMARY':rep.text('Descriptoin about the book'),
        'DIGITAL_AVILABILITY':rep.classification('Is Digitally Available (Yes/No)'),
        
            })
        academic_textbooks[common_data['ISBN']]=common_data
        print()
        print('Information Added Succesfully')
        print('*'*50)
        break


'''Display available categories and redirect the user
to the appropriate book entry form.'''
def add_book():
    print()
    print('*'*50)
    print('Add Book')
    while True:
        #displaying categories to choose by user to add book
        category=input('Choose book category 1.Competitive Exam Book\n 2.Rare Book\n 3.Magazine\n 4.Aptitude & Reasoning (sc/st) Books\n 5.Spiritual Book\n 6.Academic Textbook\n').lower()
        if category=='':
            print('Choose category')
            continue
        elif category in ['1','competitive exam book']:
            competitive_book()
            break
        elif category in ['2','rare book']:
            rare_book()
            break
        elif category in ['3','magazine']:
            magazine()
            break
        elif category in ['4','aptitude & resoning']:
            sc_st_books()
            break
        elif category in ['5','spiritual book']:
            spiritual()
            break
        elif category in ['6','academic textbook']:
            academic_book()
            break
        else:
            print('Choose valid category')
            continue

#Returns a list containing all category dictionaries.
#This prevents code duplication in search,edit,and remove operations.
def all_categories():
    return[
        competitive_books,
        rare_books,
        magazines,
        sc_books,
        spiritual_books,
        academic_textbooks

        ]

'''Search for a book using ISBN and allow the librarian
to update any field of the selected book'''
def edit_book():
    isbn=rep.digit('Enter ISBN Number of book')
    
    '''Search through every category dictionary
    until the matching ISBN is found'''
    categories=all_categories()
    for category in categories:
        for title,details in category.items():
            if details['ISBN']==isbn:
                book=details

                '''Display all current book information
                before allowing modifications'''
                print('Book Found')
                for key,value in book.items():
                    print(f"{key}:{value}")

                while True:
                    #Update selected field with new value
                    field_name=input('Enter the field name to change (or "Enter Done" to finish)').upper()
                    if field_name=='':
                        print('Value should not be emtpy')
                        continue
                    if field_name=='DONE':
                        print('Book updated succesfully')
                        return

                    if field_name not in book:
                        print('Enter valid field name')
                        continue
                    field_value=input('Enter new field value')
                    book[field_name]=field_value
                    print('Field Information Updated Successfully')
    print('Book not found')
       

#Remove a book from its category using ISBN
def remove_book():
    isbn=rep.digit('Enter ISBN Number of book')
    categories=all_categories()
    for category in categories:
        #Store the dictionary key that needs to be removed
        book_to_delete=None
        
        for title,details in category.items():
            if details['ISBN']==isbn:
                book_to_delete=title
                break
        #Delete the book from its category dictionary
        if book_to_delete:
            category.pop(book_to_delete)
            print('Book removed successfully')
            return
    
    print('ISBN not found')


'''Combine books from all categories into a single dictionary
and display every stored book'''
def view_books():
    books={
        **competitive_books,
        **rare_books,
        **magazines,
        **sc_books,
        **spiritual_books,
        **academic_textbooks
        }
    if not books:
        print('No books available')
        return

    for key,value in books.items():
        print(f"{key}:{value}")

#Search and display books by title
def search_by_title():
    search=rep.text('Enter title of book').strip().title()
    categories=all_categories()
    for category in categories:
        for title,details in category.items():
            if details['TITLE']==search:
                book=details
                print('Book Found')
                for key,value in book.items():
                    print(f"{key}:{value}")

#Search and display books by author name
def search_by_author():
    search=rep.text('Enter Author name of book').strip().title()
    categories=all_categories()
    for category in categories:
        for title,details in category.items():
            if details['AUTHOR']==search:
                book=details
                print('Book Found')
                for key,value in book.items():
                    print(f"{key}:{value}")

#Search and display books specific category
def search_by_category():
    search=rep.text("Enter book category name\n Competitive Exam\n  Rare Book\n Magazine\n Aptitude And Resoning\n Spiritual\n Academic Book").strip().title()
    categories=all_categories()
    for category in categories:
        for title,details in category.items():
            if details['CATEGORY']==search:
                book=details
                print()
                for key,value in book.items():
                    print(f"{key}:{value}")
    print(f'{search} category has no books') 

#search academic textbooks by subject name
def search_by_subject():
    search=rep.text('Enter subject name').strip().title()

    for title,details in academic_textbooks.items():
        if details['SUBJECT_NAME']==search:
            book=details
            print()
            for key,value in book.items():
                print(f"{key}:{value}")
 
    

'''Main application loop
   Display Librarian and Student operations repeatedly
   until the program is terminated'''
while True:
    #Read user operation and call the corresponding function
    print()
    print('MASTYA LIBRARY MANAGEMENT')
    print()

    print('*'*50)
    #difining operations
    print('Librarian Operations')
    print('1.Add Book')
    print('2.Edit Book')
    print('3.Remove Book')
    print('4.View Books')
    print('*'*50)



    print('Student Operations')
    print('5.Search by Title')
    print('6.Search by Author')
    print('7.Search by Category')
    print('8.Search by Subject')
    print('*'*50)
    #Librarian choosing operation
    choice=input('Choose Operation').lower()
    if choice in ['1','add book']:
        add_book()
    elif choice in ['2','edit book']:
        edit_book()
    elif choice in ['3','remove book']:
        remove_book()
    elif choice in ['4','view books']:
        view_books()
    elif choice in ['5','search by title']:
        search_by_title()
    elif choice in ['6','search by author']:
        search_by_author()
    elif choice in ['7','search by category']:
        search_by_category()
    elif choice in ['8','search by subject']:
        search_by_subject()
    else:
        print('Choose valid operation')
        continue
        
        
        



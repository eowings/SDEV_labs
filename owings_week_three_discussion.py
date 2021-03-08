"""Owings week three discussion:
    Input Validation"""
#Before
def before_fucntion():
    """Unmodified code"""
    firstname = input('Enter your first name: ')
    while not firstname.isalpha():
        firstname = input('That was not a compatible name type,'
                          'please try again. ')
    print('Your first name is: ' + firstname)
#After
def after_fucntion():
    """Modified for proper use of flag."""
    char_check = False
    while not char_check:
        firstnametwo = input('Enter your first name: ')
        if firstnametwo.isalpha():
            char_check = True
        else:
            print('That was not a compatible name type, '
                  'please try again.')
        print('Your first name is: ' + str(firstnametwo))
before_fucntion()
after_fucntion()

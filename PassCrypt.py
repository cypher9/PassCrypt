from os.path import isfile
from src.info import Info
from src.functions import Functions


if __name__ == '__main__':
    info = Info()
    info.start_text()
    function = Functions()
    if isfile('passcrypt.enc'):
        function.xml_to_pass()

    options = {1: function.add_new_entry,
               2: function.show_entries,
               0: function.quit
               }

    while True:
        try:
            info.menu()
            option = int(raw_input('Option: '))
            if option < 0 or option > 2:
                print ("\n...not a valid input...\n")
            else:
                options[option]()
        except ValueError:
            print ("\n...not a valid input...\n")
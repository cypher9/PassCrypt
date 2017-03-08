from os.path import isfile
from src.info import Info
from src.functions import Functions
from src.crypto import set_password
from src.xml_func import write_xml


def passcrypt():
    info = Info()
    info.start_text()
    function = Functions()
    if isfile('passcrypt.enc'):
        function.xml_to_pass()
    else:
        set_password()
        write_xml("")

    options = {1: function.add_new_entry,
               2: function.show_entries,
               3: info.help,
               0: function.quit
               }

    while True:
        try:
            info.menu()
            option = int(raw_input('Option: '))
            if option < 0 or option > 3:
                print ("\n...not a valid input...\n")
            else:
                options[option]()
        except ValueError:
            print ("\n...not a valid input...\n")

    return


if __name__ == '__main__':
    passcrypt()

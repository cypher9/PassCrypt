class Info(object):
    '''
    Info of version and tool
    '''

    def start_text(self):
        print("PassCrypt v0.0.1")
        print("--")
        print("PassCrypt is a simple commandline tool for keeping up with your Passwords and login data")
        print("PassCrypt encrypts your database with PyCrypto to make your stuff really private ")
        print("\n")

    def help(self):
        print("\nhelp for PassCrypt")
        print("you have 6 options to select from:\n")
        print("1 - Add a new entry")
        print("2 - Show entries")
        print("0 - Quit \n")

        print("Option 1 - Add a new entry              : Add a new entry to your database\n")
        print("Option 2 - Show entries                 : Show all available entries")
        print("Option 0 - Quit                         : Exit PassCrypt")

        raw_input("Press ENTER to go on...")

    def menu(self):
        print("\nSelect what you want to do")
        print("1 - Add a new entry")
        print("2 - Show entries")
        print("0 - Quit\n")

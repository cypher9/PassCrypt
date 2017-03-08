import sys
from datetime import datetime
from src.pass_entry import make_entry
from src.xml_func import create_xml, get_root

class Functions(object):
    '''
    classdocs
    '''

    pass_entry_list = []

    def print_passentry(self, pass_entry):
        print("\n**************************")
        print("Name: " + pass_entry.entry_name)
        print("URL: " + pass_entry.url)
        print("Username: " + pass_entry.username)
        print("Password: " + pass_entry.password)
        print("**************************")

    def show_entries(self):
        for pass_entry in self.pass_entry_list:
            self.print_passentry(pass_entry)

    def xml_to_pass(self):
        try:
            self.pass_entry_list = []
            xml_root = get_root()
            for pass_entry in xml_root.findall('pass_entry'):
                if pass_entry is None:
                    break
                else:
                    entry_name = pass_entry.attrib['name']
                    url = pass_entry.attrib['url']
                    username = pass_entry.attrib['username']
                    password = pass_entry.attrib['password']

                    self.pass_entry_list.append(make_entry(entry_name, url, username, password))
        except:
            print "failed to read xml...\nYour password may be incorrect!\nRestart PassCrypt and try again!"
            self.quit()

    def save_entry_list(self):
        create_xml(self.pass_entry_list)

    def add_new_entry(self):
        print("\nAdd your new entry...\n")
        entry_name = str(raw_input('Name: '))
        url = str(raw_input('URL: '))
        username = str(raw_input('Username: '))
        password = str(raw_input('Password: '))

        self.pass_entry_list.append(make_entry(entry_name, url, username, password))
        self.save_entry_list()
        print "\nEntry saved...\n"

    def quit(self):
        sys.exit(0)

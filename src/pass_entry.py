
class PassEntry():
    entry_name = ""
    url = ""
    username = ""
    password = ""
    category = ""

    def __init__(self, entry_name, url, username, password, category):
        self.entry_name = entry_name
        self.url = url
        self.username = username
        self.password = password
        self.category = category


def make_entry(entry_name, url, username, password, category):
    entry = PassEntry(entry_name, url, username, password, category)
    return entry


class PassEntry():
    entry_name = ""
    url = ""
    username = ""
    password = ""

    def __init__(self, entry_name, url, username, password):
        self.entry_name = entry_name
        self.url = url
        self.username = username
        self.password = password


def make_entry(entry_name, url, username, password):
    entry = PassEntry(entry_name, url, username, password)
    return entry

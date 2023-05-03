class Key:
    def __len__(self):
        return 1337

    def __getitem__(self, key):
        if key == 404:
            return 3

    def __gt__(self, other):
        return 9001 > other

    def __getattr__(self, name):
        if name == "passphrase":
            return "zax2rulez"

    def __str__(self):
        return "GeneralTsoKeycard"

key = Key()
assert len(key) == 1337
assert key[404] == 3
assert key > 9000
assert key.passphrase == "zax2rulez"
assert str(key) == "GeneralTsoKeycard"
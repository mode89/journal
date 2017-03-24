import os
import subprocess
import tempfile

class Application:

    def __init__(self):
        self.journal = str()

    def run(self):
        text = self.edit()
        # do not add empty records
        if text != "":
            self.journal += self.time() + " " + text
            # save journal
            with open(self.journal_file, "w") as f:
                f.write(self.journal)

    def edit(self):
        with tempfile.NamedTemporaryFile("r", suffix=".txt") as f:
            subprocess.call([os.environ["EDITOR"], f.name])
            return f.read()

    def time(self):
        return str()
import sys
import pathlib

import html_constants as _html


class toFoxResult:
    """
    Given CLI filepath and split character values, this translates a certain
    flat file (see input-template.txt) to generate simple html that firefox can
    import.
    """

    def __init__(self):
        self.filepath: pathlib.Path = pathlib.Path(sys.argv[1])
        self.split: str = sys.argv[2]
        self.bits: list = []
        self.result = update_result(prev_result="", addition=_html.HEAD)
        self.do_body()
        self.result = update_result(prev_result=self.result, addition=self.body)

        self.result = update_result(prev_result=self.result, addition=_html.FOOT)

    def sanitize_bits(self) -> list:
        """
        Apply data cleaning, then try to combine into formatted output
        :param bits: list (expected to be two elements long-- url then description
        :return: version of bits which has been sanitized
        """
        try:
            url = self.bits[0].strip()
            descr = self.bits[1].strip()
        except:
            raise ValueError("That probably wasn't a list!")

        bits = [url, descr]
        self.bits = bits

    def do_body(self) -> str:
        self.body: str = ""
        file = open(self.filepath, "r")
        for row in file.readlines():
            try:
                self.bits = row.split(self.split)
                self.sanitize_bits()
                row_result = self.process_entry()
                self.body = update_result(self.body, row_result)
            except:
                print("SPLIT-RECOMBINE FAILED, CHECK RESULT CAREFULLY!")

    def process_entry(self) -> str:
        to_chunk = [
            _html.DT,
            _html.HREF_SLUG0,
            self.bits[0],
            _html.HREF_SLUG1,
            self.bits[1],
            _html.LABEL_END,
            _html.DTs,
        ]
        row_result = "".join(to_chunk)
        return row_result

    def output(self):
        with open("output.html", "w") as output_file:
            output_file.write(self.result)


def update_result(prev_result: str, addition: str) -> str:
    # combines two strings without adding whitespace; syntactic convenience/preference
    result = "".join([prev_result, addition])
    return result


if __name__ == "__main__":
    # FILEPATH: pathlib.Path = pathlib.Path("/home/dirk_rec/fromWinLinks.txt")
    # SPLIT: str = "|"
    ffox_importer = toFoxResult()
    ffox_importer.output()

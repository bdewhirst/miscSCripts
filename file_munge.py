import pathlib

import html_constants as _html


# TODO: class called 'foxResult'?
def main(filepath) -> str:
    """
    Read the specified file and parse each line, splitting on SPLIT
    :param filepath: a pathlib path to a file of expected syntax 'url | description string \n'
    :return: a long html-like string which should be "legal" to import as firefox bookmark file
    """
    result: str = ""
    result = update_result(prev_result=result, addition=_html.HEAD)

    body: str = do_body(filepath)
    result = update_result(prev_result=result, addition=body)

    result = update_result(prev_result=result, addition=_html.FOOT)

    return result


def update_result(prev_result: str, addition: str) -> str:
    result = "".join([prev_result, addition])

    return result


def sanitize_bits(bits: list) -> list:
    """
    Apply data cleaning, then try to combine into formatted output
    :param bits: list (expected to be two elements long-- url then description
    :return: version of bits which has been sanitized
    """
    if bits[0]:  # i.e., string of length at least 1
        if len(bits[0]) < 5:
            url = "http://www.example.com"
        else:
            url = bits[0].strip()  # remove surrounding whitespace
    else:
        raise ValueError("that probably wasn't a list!")
    if bits[1]:
        descr = bits[1].strip()
    else:
        descr = "placeholder-inspect-me"

    bits = [url, descr]

    return bits


def do_body(filepath) -> str:
    body: str = ""
    file = open(filepath, "r")
    for row in file.readlines():
        try:
            bits = row.split(SPLIT)
            clean_bits = sanitize_bits(bits=bits)
            row_result = process_entry(clean_bits=clean_bits)
            body = update_result(body, row_result)

        except:
            print("SPLIT FAILED, CHECK RESULT CAREFULLY!")
            return body

    return body


def process_entry(clean_bits) -> str:
    to_chunk = [
        _html.DT,
        _html.HREF_SLUG0,
        clean_bits[0],
        _html.HREF_SLUG1,
        clean_bits[1],
        _html.LABEL_END,
        _html.DTs,
    ]
    row_result = "".join(to_chunk)
    return row_result


if __name__ == "__main__":
    FILEPATH: pathlib.Path = pathlib.Path("/home/dirk_rec/fromWinLinks.txt")
    SPLIT: str = "|"

    result = main(filepath=FILEPATH)
    # print(result)
    with open("output.txt", "w") as output_file:
        output_file.write(result)

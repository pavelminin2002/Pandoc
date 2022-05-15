from panflute import *
import sys

headers = {}


def filter(e, doc):
    if type(e) == Header:
        if stringify(e) in headers.keys():
            if headers.get(stringify(e)) == e.level:
                sys.stderr.write("Повторяются заголовки " + str(e.level) + "уровень, " + stringify(e))
        else:
            headers[stringify(e)] = e.level
        if e.level <= 3:
            title = [Str(stringify(e).upper())]
            return Header(*title, level=e.level)

    if type(e) == Str:
        if str(e.text).lower() == "bold":
            title = [Str(e.text)]
            return Strong(*title)


def main(file=None):
    return run_filter(filter, doc=file)


if __name__ == "__main__":
    main()
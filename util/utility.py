"""Utility functions.
"""

from datetime import date
from settings import *


def format_date(a_date):
    """Converts a date from datetime.date() to a string of the form '<month> <day>, <year>'.
    Uses strftime() method of datetime.date class and its pre-defined format codes from
    https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    """

    return a_date.strftime(PREFERRED_DATE_FORMAT) if isinstance(a_date, date) else 'unknown'


def date_py_to_json(a_date):
    """Converts datetime.date objects to JSON, returning a string formatted as 'YYYY-mm-dd'.
    To be used directly to update date values in JSON strings when converting Python objects to JSON,
    not as the default= parameter in json.dumps() (which creates "\"<iso_date_str>\"", not "<iso_date_str>" strings).
    """

    return a_date.isoformat() if isinstance(a_date, date) else "null"


def date_json_to_py(iso_date):
    """Converts string formatted as 'YYYY-mm-dd' to datetime.date object.
    To be used directly to update date fields in conversions of JSON strings to Python objects,
    not as the object_hook= parameter in json.loads().
    """

    return date.fromisoformat(iso_date)


def get_project_dir():
    """Returns the Path object corresponding to the project root directory.
    """

    return PROJECT_DIR


def get_data_dir():
    """Returns the Path object corresponding to the data directory
    (by convention located right under the project root directory).
    """

    data_dir = get_project_dir() / 'data'
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir


if __name__ == '__main__':

    # pass

    # Demonstrate pathlib.Path
    # - user's home dir: Path.home()
    # - current dir: Path.cwd(), Path('.'), Path()
    # - absolute path: <path>.absolute()
    # - parent dir: <path>.parent
    # - new dir: <newDir> = <path> / '<subdir1>/<subdir2>/.../<subdirN>'
    #            <newDir>.mkdir(parents=True, exist_ok=True)
    # - remove dir: <dir>.rmdir()                                           # requires the <dir> to be empty
    # - project dir: settings.PROJECT_DIR

    # Demonstrate get_project_dir(), get_data_dir()
    print(get_project_dir())
    print(get_data_dir())

__author__ = 'vikesh'

import os
import sys

from docopt import docopt

__version__ = '0.0.1'

_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_data_dir(path):
    """

    :param path: Returns the path of the directory matching the passed `path`
    :return: path
    """
    return os.path.dirname(os.path.join(_ROOT, 'data', path))


def _iterate_gitignores():
    """
    :return: Iterates over all the data directory and return all the .gitignore files
    """
    gitignores = []
    for _root, _sub_folders, files in os.walk(DATA_DIR):
        gitignores += [f.replace('.gitignore', '')
                       for f in files if f.endswith('.gitignore')]
    return sorted(gitignores)

# Find location of all gitignore files

DATA_DIR = get_data_dir('*.gitignore')

# Fetch all gitignore files

GitIgnore_RAW = _iterate_gitignores()
GitIgnore = [filename.lower() for filename in GitIgnore_RAW]


def return_filenames():
    """
    :return: return all available .gitignore files available in data
    """
    return ', '.join(GitIgnore)


def check_gitignores(names):
    """
    :param names: takes name as parameter , generates and handles exceptions
    :return: return gitignore content
    """
    output = '### Created by L-Commands : Powerful Linux Commands : http://git.io/v4LVP. \n'
    error_ = []
    for name in names:
        try:
            raw = GitIgnore_RAW[GitIgnore.index(name.lower())]
            output += print_gitignore(raw)
        except ValueError:
            error_.append(name)
    if error_:
        sys.stderr.write((
            'L-Command Could\'t recognise the following gitignore'
            '\n%s\n'
            'Try `gitignore ls` to see list of available gitingores.\n'
        ) % "\n".join(error_))
        output = []
    return output


def print_gitignore(raw, directory=''):
    """
    :param raw: takes the raw as a filename
    :param directory: current directory
    :return: returns the corresponding gitignore file
    """

    output = '\n#####=== %s ===####\n' % raw
    if directory:
        filepath = os.path.join(DATA_DIR, '%s/%s.gitignore' % (directory, raw))
    else:
        filepath = os.path.join(DATA_DIR, raw + '.gitignore')
        output += '\n'
    try:
        with open(filepath) as gitignore:
            output += gitignore.read()
        return output
    except IOError:
        return print_gitignore(raw, 'Global')


def main():
    """
    :return: L-Commands generates .gitignore files
    """
    arguments = docopt(__doc__, version=__version__)

    if arguments['ls'] or arguments['list']:
        print(return_filenames())
    elif arguments['NAME']:
        print(check_gitignores(arguments['NAME']))
    else:
        print(__doc__)


if __name__ == '__main__':
    main()




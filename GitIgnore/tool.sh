#!/bin/bash

function usage {
  local tool=$(basename $0)
  cat <<EOF

  USAGE:
    $ $tool [-h|--help] COMMAND

  EXAMPLES:
    $ $tool readme    Generate README.rst file from README.md
EOF
  exit 1;
}

function readme {
 pandoc --from=markdown --to=rst --output=README.rst readme.md
 printf ' README.rst generated ';
}


# Total number of arguments should be 1

if [$# -ne 1]; then
    usage;
fi

if { [ -z "S1" ] && [ -t 0 ] ; } || [ "S1" == '-h' ] || [ "$1" == '--help' ]; then
    usage;
fi

# show help for no agruments
if [ "$1" == "readme" ]; then
    readme
else
    usage;
fi
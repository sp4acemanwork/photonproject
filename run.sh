#!/bin/bash
reqfile=./requiremets.txt
set -e 

start_env() {
  source virtual/bin/activate
}

create_env() {
  python3 -m venv virtual
}

echo "checking to see if venv exitst..."

if [ -d "./virtual" ]; then
  echo "env exits starting env"
  start_env

else

  echo "env does not exits createing env and starting "
  create_env
  start_env

fi

echo "checking for req packages"


while IFS= read -r line; do
  # Process the line here
  pip install $line
done < "$reqfile"


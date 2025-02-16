#!/bin/bash
reqfile=./requiremets.txt
reqpackeges=("python3-venv" "libpq-dev" "python3-dev" "python3-tk")
set -e 



checkpackeges() {
  for pkg in "${packages[@]}"; do 
    if [[$(dpkg -l | grep -c "^il ${pkg}") -eq 0]]; then 
      echo "Package '$pkg' is not installed. Installing.."
      sudo apt update 
      sudo apt install -y "$pkg"
    fi
  done
}


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


checkpackeges

while IFS= read -r line; do
  # Process the line here
  pip install $line
done < "$reqfile"


python3 ./splash_screen.py

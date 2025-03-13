#!/bin/bash
reqfile=./requiremets.txt
reqpackeges=("python3-venv" "libpq-dev" "python3-dev" "python3-tk")
set -e 



checkpackeges() {
  reqpackages=("python3-venv" "libpq-dev" "python3-dev" "python3-tk")

# Flag to determine if we need to update
  needs_update=false

  for pkg in "${reqpackages[@]}"; do
    echo "Checking package: $pkg"  # Debugging output

      # Check if package is installed
      if ! dpkg -l | awk '{print $2}' | grep -qw "^${pkg}$"; then
        echo "Package '$pkg' is NOT installed."
        needs_update=true
      else
        echo "Package '$pkg' is already installed."
      fi
    done

  # Run apt update only if a package is missing
  if [ "$needs_update" = true ]; then
    echo "Updating package lists..."
    sudo apt update
  fi

  # Install missing packages
  for pkg in "${reqpackages[@]}"; do
    if ! dpkg -l | awk '{print $2}' | grep -qw "^${pkg}$"; then
      echo "Installing '$pkg'..."
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

echo "checking for req apt packages"

checkpackeges

echo "checking to see if venv exitst..."

if [ -d "./virtual" ]; then
  echo "env exits starting env"
  start_env

else

  echo "env does not exits createing env and starting "
  create_env
  start_env

fi

echo "checking for req pip packages"

while IFS= read -r line; do
  # Process the line here
  pip install $line
done < "$reqfile"

clear 

python3 ./splash_screen.py

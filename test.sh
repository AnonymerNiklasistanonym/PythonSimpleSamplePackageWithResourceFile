#!/usr/bin/env bash

set -x
set -e

DIST_DIRECTORY="dist"
SRC_DIRECTORY="src"
PACKAGE_NAME="your_package_name"
PACKAGE_VERSION="1.0.0"
BUILD_ENVIRONMENT="venv_build_environment"
INSTALL_ENVIRONMENT="venv_install_environment"

rm -rf "$BUILD_ENVIRONMENT"
rm -rf "$DIST_DIRECTORY"
rm -rf "$SRC_DIRECTORY/$PACKAGE_NAME.egg-info"
rm -rf "$INSTALL_ENVIRONMENT"

python3 -m venv "$BUILD_ENVIRONMENT"
source "$BUILD_ENVIRONMENT/bin/activate"
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
python3 -m build
deactivate

python3 -m venv "$INSTALL_ENVIRONMENT"
source "$INSTALL_ENVIRONMENT/bin/activate"
python3 -m pip install --upgrade pip
pip install "$DIST_DIRECTORY/$PACKAGE_NAME-$PACKAGE_VERSION-py3-none-any.whl"
your_package_name_init
your_package_name
deactivate

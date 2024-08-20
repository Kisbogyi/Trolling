#!/bin/bash

CURRENT_DIRECTORY=pwd
WORKING_DIRECTORY=$HOME/.config/updater
mkdir $WORKING_DIRECTORY

cp ./sound/quack.mp3 $WORKING_DIRECTORY
cp ./src/Quack.py $WORKING_DIRECTORY
cp ./quack.sh $WORKING_DIRECTORY
cp ./requirements.txt $WORKING_DIRECTORY
cp ./quack.service $WORKING_DIRECTORY

cd $WORKING_DIRECTORY
# Replace working dir with real working directory
sed -ie "s|{WORKINGDIR}|${WORKING_DIRECTORY}|" quack.service

python3 -m venv .

source bin/activate

pip install -r requirements.txt

cp $WORKING_DIRECTORY/quack.service $HOME/.config/systemd/user/quack.service

systemctl start --user quack.service
systemctl enable --user quack.service

rm -rf  $CURRENT_DIRECTORY

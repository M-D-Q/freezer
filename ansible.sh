#!/bin/bash

#keeping passphrase in memory

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa

##################

ansible-playbook syu.yml -vv

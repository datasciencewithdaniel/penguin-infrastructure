#!/bin/bash

sudo yum update -y
sudo yum install git -y

sudo touch ~/test.txt

sudo git clone https://github.com/datasciencewithdaniel/penguin.git

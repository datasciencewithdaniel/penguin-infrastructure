#!/bin/bash

sudo yum update -y
sudo yum install git -y

cd ~

git clone https://github.com/datasciencewithdaniel/penguin.git
cd penguin

#!/bin/bash

python3 pip list | tr '  ' '==' > requirements.txt

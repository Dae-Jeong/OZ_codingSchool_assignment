#!/bin/bash

# Python 3.12 버전의 가상환경을 만들고, 가상환경을 활성화하며,
# requirements.txt 파일로 패키지를 설치하고 main.py 파일을 실행하는 쉘 스크립트

# 1. Python 3.12 버전의 가상환경을 만듭니다.
python3 -m venv venv

# 2. 가상환경을 활성화합니다.
source venv/bin/activate

# 3. requirements.txt 파일로 패키지를 설치합니다.
pip install -r requirements.txt

# 4. main.py 파일을 실행합니다.
python main.py

# 5. 가상환경을 비활성화합니다. (옵션)
deactivate
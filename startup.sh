echo "Start startup.sh"
VENV_NAME="venv"
# Install python3.10
if ! command -v python3.10 &> /dev/null
then
    sudo apt-get update
    sudo apt-get install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get update
    sudo apt-get install python3.10
fi
# Install virtualenv
if ! command -v virtualenv &> /dev/null
then
    sudo apt-get update
    sudo apt-get install python3-virtualenv
fi
# Create venv
virtualenv -p python3.10 $VENV_NAME
# Activate venv
source $VENV_NAME/bin/activate
pip install --upgrade pip
# Install Python packages
pip install asgiref==3.7.2 \
            cffi==1.16.0 \
            cryptography==41.0.5 \
            Django==4.2.7 \
            djangorestframework==3.14.0 \
            djangorestframework-simplejwt==5.3.0 \
            Pillow==10.1.0 \
            pycparser==2.21 \
            PyJWT==2.8.0 \
            pytz==2023.3.post1 \
            setuptools==68.2.2 \
            sqlparse==0.4.4 \
            typing_extensions==4.8.0 \
            wheel==0.41.3
apt-get install libjpeg8-dev zlib1g-dev
python manage.py migrate
echo "startup.sh complete"
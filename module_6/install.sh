set -e

apt-get update 
apt-get install ffmpeg -y

pip install torch -f https://download.pytorch.org/whl/torch_stable.html

pip install -e ../module_2
set -e

apt-get update install -y ffmpeg

pip install torch -f https://download.pytorch.org/whl/torch_stable.html

pip install -e ../module_2
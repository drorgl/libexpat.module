sudo apt-get nstall autoconf
sudo apt-get install cmake
sudo apt-get install libtool

git submodule sync
build_linux.sh
cd build.linux
make

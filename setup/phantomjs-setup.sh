curl https://phantomjs.googlecode.com/files/phantomjs-1.9.0-linux-x86_64.tar.bz2  -o /tmp/phantomjs-1.9.0-linux-x86_64.tar.bz2 &&
cd /usr/local/ &&
sudo tar xvjf /tmp/phantomjs-1.9.0-linux-x86_64.tar.bz2 &&
sudo ln -s  /usr/local/phantomjs-1.9.0-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs &&
rm -r /tmp/phantomjs-1.9.0-linux-x86_64.tar.bz2
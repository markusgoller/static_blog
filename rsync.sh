echo "rsync nginx start"

cd ./webroot/

make html

cd ../

rsync -a --delete-before --progress --exclude-from='.gitignore' --exclude='*.git*' --exclude='webroot' --exclude='log' --exclude='statlocal_container.sh' /home/unix/dev/static_blog/ webserver@markusgoller.at:/etc/docker/nginx

rsync -a --delete-before --progress /home/unix/dev/static_blog/webroot/markusgoller webserver@markusgoller.at:/www/

echo "rsync nginx done"

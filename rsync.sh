echo "rsync nginx start"

rsync -a --delete-before --progress --exclude-from='.gitignore' --exclude='*.git*' --exclude='webroot' --exclude='log' --exclude='statlocal_container.sh' /home/unix/dev/nginx/ webserver@markusgoller.at:/etc/docker/nginx
rsync -a --delete-before --progress /home/unix/dev/nginx/webroot webserver@naschi.info:/www/

echo "rsync nginx done"

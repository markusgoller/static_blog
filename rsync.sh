echo "rsync nginx start"
rsync -a --delete-before --progress --exclude-from='.gitignore' --exclude='*.git*' --exclude='webroot' /home/unix/dev/nginx/ webserver@markusgoller.at:/etc/docker/nginx
rsync -a --delete-before --progress /home/unix/dev/nginx/webroot webserver@naschi.info:/www/
scp /home/unix/dev/nginx/.env webserver@naschi.info:/etc/docker/nginx
echo "rsync nginx done"

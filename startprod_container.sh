echo "NGINX_CONF=production.conf" > .env 

echo "INSTALLFOLDER=/etc/docker/nginx" >> .env

echo "WEBROOT=/www/markusgoller" >> .env

cat .env

mkdir -p /etc/docker/nginx/log/nginx

docker-compose build

docker-compose up -d

echo "startprod_container.finished"
echo "NGINX_CONF=development.conf" > .env 

echo "INSTALLFOLDER=/home/unix/dev/nginx" >> .env

echo "WEBROOT=/home/unix/dev/static_blog/webroot/output" >> .env

cat .env

mkdir -p ./log/nginx

docker-compose build

docker-compose up -d

echo "startlocal_container.finished"
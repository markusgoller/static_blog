# nginx
My personal website: [http://markusgoller.at](http://markusgoller.at)

## nginx logfiles
/var/log

## Dependencies
conda activate pelican

* pip install pelican[Markdown]

## Development
```
cd ./webroot
make serve
```

## Build
```
cd ./webroot
make html
```

## Deploy
Upload local files including the built Pelican website to the server.

```
sh rsync.sh
```

## Start localhost server
Nginx start locally and inspect built pelican artifacts.
```
sh startlocal_container.sh
```


## Start production server
The docker containers and the website must be built and started on the server.

```
cd /var/docker/nginx
sh startprod_container.sh
```

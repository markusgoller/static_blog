# static_blog
My personal website: [http://markusgoller.at](http://markusgoller.at)

## nginx logfiles
/var/log

## Dependencies
conda activate pelican

* pip install pelican[Markdown]

## Development
```
cd ./webroot
make devserver
```

## Build
```
cd ./webroot
make html
```

## Uploading Pictures
og_image and pelican HOME_COVER in landscape format.

downsize quality
```
cd ./content/images 
convert IMG_Example.jpg -quality 50 IMG_Example_resize.jpg
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

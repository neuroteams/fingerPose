Запустить контейнер с общей папкой для контейнера и хост-машины (запустить 1 раз перед запуском скрипта):

```
docker run -d -it --mount type=bind,source=/home/fingerpose/Videos,target=/openpose/Videos  --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=0 --name fingerpose cwaffles/openpose
```
Общая папка на сервере: /home/fingerpose/Videos

Общая папка в контейнере:/openpose/Videos

По-хорошему ещё бы в Videos создать под вывод папку:

```mkdir /home/fingerpose/Videos/output```

Если на вход принимается произвольное видео, то сначала его копируем в общую папку:

```
cp /адрес_видео /home/fingerpose/Videos/video.avi
```

Запускаем видео на обработку:

```
docker exec -it fingerpose ./build/examples/openpose/openpose.bin --video Videos/video.avi --write_json Videos/output/ --display 0 --render_pose 0 --face --hand
```

jsonы сохраняются в Videos/output, с которой мы можем взаимодействовать и из хост-машины

Дальше на папке с Videos/output запускается Полинин скрипт

**Как открыть openpose и работа с docker:**

Открыть контейнер и удалить после выхода:

```
docker run -it --rm --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=0 cwaffles/openpose
```

Открыть контейнер в фоновом режиме:

**Внимание!!! Не забывайте периодически проверять, сколько контейнеров запущено, чтобы не плодить их!!!**
(как остановить контейнер - см.ниже)

```
docker run -it -d --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=0 cwaffles/openpose
```

Посмотреть список контейнеров:

```
docker container ls -a -s 
```

Как остановить контейнер:

```
docker container stop идентификатор_контейнера_можно_посмотреть_в_списке_контейнеров
```

Как удалить контейнер:

```
docker container rm идентификатор_контейнера_можно_посмотреть_в_списке_контейнеров
```

Как запустить команды openpose не заходя в контейнер:

```
docker exec идентификатор_контейнера команда_для_openpose
```

Как копировать файл из контейнера на сервер:

```
docker cp  идентификатор_контейнера:путь_к_файлу_в_контейнере путь_к_файлу_на сервере
```
Пример использования:

```
docker cp quizzical_burnell:/openpose/output/video_000000000077_keypoints.json ./openpose_files/new.json
```


Как копировать файл с сервера в контейнер:

```
docker cp путь_к_файлу_на_сервере идентификатор_контейнера:путь_к_файлу_в_контейнере
```

**Как запустить openpose в работу:**

```
./build/examples/openpose/openpose.bin --video examples/media/video.avi --write_json output/ --display 0 --render_pose 0 --face --hand
```

Что это значит:

```./build/examples/openpose/openpose.bin``` - запустить openpose

```--video``` - ключ, который говорит, что будем анализировать видео (альтрнатива - анализ с вебки, для этого ключей не нужно. И, возможно, по фотоке, пока с фото не разобралась). За этим ключом должен идти адрес видео, которое будем анализировать

```examples/media/video.avi``` - собственно, адрес видео, которое будем распозновать

```--write_json``` ключ, который говорит, что результаты надо записывать в файл формата json. За ним долно быть написано, в какую папку сохранять такие файлы

```output/``` - расположение папки, в которую сохраняем результаты

```--display 0``` - ключ, который говорит, что не надо/не надо использовать дисплей. 0 - это как раз потому, что не надо

```--render_pose 0``` - это ещё не разобралась

```--face --hand``` - ключи, которые говорят, какие части тела анализировать. Без этих ключей анализирует всё тело

## Об OpenPose
Программа умеет:
- В режиме реального времени строить 2D модель ключевых точек нескольких людей
- В режиме реального времени строить 2D модель ключевых точек рук (21 точка на каждую руку) нескольких людей
- В режиме реального времени строить 3D модель ключевых точек одного человека
- Существует возможность калибровать искажения/параметры,которые накладывает камера

Входные данные: image, video, webcam, Flir/Point Grey and IP camera. Included C++ demos to add your custom input.
Выходные данные: basic image + keypoint display/saving (PNG, JPG, AVI, ...), keypoint saving (JSON, XML, YML, ...), and/or keypoints as array class.

Имеется [Python API (```doc/modules/python_module.md```)](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/modules/python_module.md)

Есть возможность улучшить скорость/уменьшиить затраты по времени

Важные страницы:

О формате вывода данных: https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/output.md

Основные ключи (параметры) openpose:https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/demo_overview.md#main-flags

## Ключи:
### Источники материала для анализа:

**Видео:**
```--video``` видеофайл.разрешение

**Фото:**
```--image_dir``` папка_с_фото/

**Вебка:**
без ключей


### 
**Сохранить результат в видео:**
--write_video output/result.avi
**Сохранить результат в json**
--write_json output/


## Взаимодействие через docker
Копировать файлы из openpose-контейнера на хост

```docker cp confident_booth:openpose/examples/media/video.avi ./openpose_files/video.avi```


## Полезные команды Linux
Перейти в папку с результатами:

```cd ./output```

Посмотреть список файлов в папке:

```ls```


Вывести содержимое файла:

```cat ./название_файла```

Выйти из контейнера:

```exit```

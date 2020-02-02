# Обмен данными с Docker из виртуальной машины
```
sudo docker cp keen_heisenberg:/openpose/examples/media/Polina_test_001.jpg ./
```

# Запуск OpenPose внутри Docker
```
docker exec keen_heisenberg ./build/examples/openpose/openpose.bin --video examples/media/Polina_test_002.jpg --write_json output/Polina_two_images/ --display 0 --render_pose 0 --hand
```
```
docker exec keen_heisenberg ./build/examples/openpose/openpose.bin --image_dir examples/media/our_input/ 
 --write_json output/our_output/json/ --display 0 --render_pose 0 --hand --hand_scale_number 6 --hand_scale_range 0.4
--write_images output/our_output/images/
```

# Обмен данными с виртуальной машиной из локальной
```
sudo scp fingerpose@nsu.sharapov.uz:nsu.sharapov.uz/test/Polina_two_images/* ./
```

from pytube import YouTube
import os



print('Сколько видео вы хотите скачать?\n'
      '1 - Одно видео\n'
      '2 - Несколько')
task = int(input())
if task == 1:
    link_video = str(input("Введите ссылку на видео: "))
    yt = YouTube(link_video)

    quality = [stream.resolution for stream in yt.streams.filter(progressive=True)]
    print(quality)
    choose = int(input('Выберете качество видео: ')) - 1

    v_name = yt.title
    path = 'C:\\Downloaded Videos'
    if os.path.isdir(path):
        print("Загрузка видео в качестве {} начата".format(quality[choose]))
    else:
        os.mkdir(path)
        print('Создана папка для видео по пути C:\Downloaded Videos')
        print("Загрузка видео в качестве {} начата".format(quality[choose]))

    yt.streams.get_by_resolution(quality[choose]).download(path, v_name)
    print('Загрузка закончена')

elif task == 2:
    path = 'C:\\Downloaded Videos'

    list_link = []
    quantity = int(input('Введите количество видео: '))
    Max = quantity + quantity
    while quantity < Max:
        list_link.append(input(str('Введите ссылку: ')))
        quantity = quantity + 1
    a = 0
    if os.path.isdir(path):
        print('Загрузка в максимальном качестве началась')
        
        for video in list_link:
            yt = YouTube(list_link[a])
            v_name = yt.title
            yt.streams.get_highest_resolution().download(path, v_name)
            bar.next()
            print(' Видео номер {} скачалось'.format(a + 1))
            a = a + 1
        
        print('Загрузка видео завершена')
    else:
        os.mkdir(path)
        print('Создана папка для видео по пути C:\Downloaded Videos')
        print('Загрузка в максимальном качестве началась')
       
        for video in list_link:
            yt = YouTube(list_link[a])
            v_name = yt.title
            yt.streams.get_highest_resolution().download(path, v_name)
            print('Видео номер {} скачалось'.format(a + 1))
            a = a + 1
        
        print('Загрузка видео завершена')

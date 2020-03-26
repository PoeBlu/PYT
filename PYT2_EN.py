from pytube import YouTube
import os

print('How many videos do you want to download??\n'
      '1 - One\n'
      '2 - Several')
task = int(input())
if task == 1:
    link_video = str(input("Enter a link to the video: "))
    yt = YouTube(link_video)

    quality = [stream.resolution for stream in yt.streams.filter(progressive=True)]
    print(quality)
    choose = int(input('Select quality: ')) - 1

    v_name = yt.title
    path = 'C:\Downloaded Videos'
    if os.path.isdir(path):
        print("Loading video with quality {} has started".format(quality[choose]))
    else:
        os.mkdir(path)
        print('Created a folder for videos along the way C:\Downloaded Videos')
        print("Loading video with quality {} has started".format(quality[choose]))

    yt.streams.get_by_resolution(quality[choose]).download(path, v_name)
    print('Download finished')

elif task == 2:
    path = 'C:\Downloaded Videos'

    list_link = []
    quantity = int(input('Enter the number of videos: '))
    Max = quantity + quantity
    while quantity < Max:
        list_link.append(input(str('Enter a link: ')))
        quantity = quantity + 1
    a = 0
    if os.path.isdir(path):
        print('Loading in maximum quality has started')
        for video in list_link:
            yt = YouTube(list_link[a])
            v_name = yt.title
            yt.streams.get_highest_resolution().download(path, v_name)

            print(' Video number {} downloaded'.format(a + 1))
            a = a + 1
        print('Download finished')
    else:
        os.mkdir(path)
        print('Created a folder for videos along the way C:\Downloaded Videos')
        print('Loading in maximum quality has started')
        for video in list_link:
            yt = YouTube(list_link[a])
            v_name = yt.title
            yt.streams.get_highest_resolution().download(path, v_name)
            print('Video number {} downloaded'.format(a + 1))
            a = a + 1
        print('Download finished')

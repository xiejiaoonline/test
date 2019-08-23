import time

duetime = int(input('输入你要倒计的时长（秒）：'))
for i in range(duetime, 0, -1):
    msg = u'\n计时在 ' + str(i) + '秒 后停止'
    print(msg, end='')
    time.sleep(1)
end_msg = '\n叮~~~~' + '  '*(len(msg)-len('结束')) 
print(u'\r'+end_msg)
print()


print('超出预计？敲击ENTER继续计时, 按Ctrl + C结束')
while True:
    try:
        input()
        starttime = time.time()
        print('开始')
        print()
        while True:
            print('现在是第 ', round(time.time() - starttime, 0), '秒', end='\n')
            time.sleep(1)

    except KeyboardInterrupt:
        print('停~~~')
        print()
        endtime = time.time()
        print('超出时间是:', round(endtime - starttime, 2),'秒')
        break

        


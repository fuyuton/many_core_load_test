#参考: [【Raspberry Pi】爆速！ラズパイでマルチコア並列コンピューティング | Murasan Lab](https://murasan-net.com/index.php/2022/02/13/post-635/)


import multiprocessing as mp
import random
import sys

#加算を10M回実行
def cal(q):
    r = random.randint(2, 7)
    n = r * 10000000
    for cal in range(n):
        cal += 1
    q.put(cal)

if __name__ == '__main__':
    a = len(sys.argv)
    if a <= 1:
        print("hint: $python3 mctest.py <process number>")
        exit()
        
    #プロセス間通信用のキューを生成
    queue = mp.Queue()
    
    n = int(sys.argv[1])
    p = []

    #プロセスを生成
    for i in range(n):
        p.append( mp.Process(target=cal, args=(queue,)) )

    #プロセス実行
    for i in range(n):
        p[i].start()

    #キューから結果を取り出す
    for i in range(n):
        print(queue.get())

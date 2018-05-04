import time
import _thread

def fun(thread,de) :
    while(1) :
        time.sleep(de)
        todos=open("news.txt",'r')
        for i in todos :
            if (len(i)<50 and i[0]!=" "):
                print(i)
        todos.close()
_thread.start_new_thread(fun,("thread",5))

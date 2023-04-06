from threading import Lock
from multiprocessing import Process,Value

lock = Lock()

class file_lock:
    def __init__(self,filename,mode) -> None:
        self.filename = filename 
        self.mode = mode
        self.file_obj = None
        
    def __enter__(self):
        print(f"Start processing ")
        self.file_obj = open(self.filename,self.mode)
        return self.file_obj
     
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(f"End processing ")
        self.file_obj.close()

        
def Tea(mode,data):
    approved=0
    # while True:
        # if approved:
    if mode == "r":
        with file_lock("Manav.txt",mode) as file_obj:
            # approved=1
            file_obj.readlines()
            # s+=1
            # approved=0
    else:
        with file_lock("Manav.txt",mode) as file_obj:
            # approved=1
            file_obj.write(data)
            # approved=0
            # s+=1

if __name__ == "__main__":
    p1=Process(target=Tea,args=("r","Ok"))
    p2=Process(target=Tea,args=("w","Done"))
    p3=Process(target=Tea,args=("w+","Whee"))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
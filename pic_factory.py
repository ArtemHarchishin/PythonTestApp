import subprocess
import os
import multiprocessing


def create_empty(w, h, pic_path):
        
        if isinstance(pic_path, list) or isinstance(pic_path, tuple):

                pool = multiprocessing.Pool(processes=5)
                res = []
                
                for p in pic_path:

                        is_created = pool.apply(create_empty_one, [w, h, p])
                        res.append((is_created, p))

                return res
        else:

                return create_empty_one(w, h, pic_path)
        

def create_empty_one(w, h, pic_path):
        dir_path, _ = os.path.split(pic_path)
        
        if dir_path and not os.path.exists(dir_path):
                os.makedirs(dir_path)
        
        if os.path.exists(pic_path):
                return False

        completed_process = subprocess.run(["magick", "-size", "%dx%d" % (w, h), "xc:white", pic_path])
        if completed_process.returncode != 0:
                completed_process.check_returncode()

        return True
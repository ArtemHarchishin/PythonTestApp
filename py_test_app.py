import pic_factory
import random
import os
import multiprocessing
import time


def get_random_name(name_template):
        a = 0
        b = 10
        return name_template % random.randint(a, b)


def main():
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filename_template = os.path.join(dir_path, "pics", "test%d.jpeg")

        filenames = get_random_name(filename_template)
        pic_factory.create_empty(32, 32, filenames)
        

if __name__ == "__main__":
        t = time.time()
        main()
        print(time.time() - t)
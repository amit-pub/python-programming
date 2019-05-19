import os

IMG_DIR = "/images/"

hash_dict = {}

for img in os.listdir(IMG_DIR):
        print "....\n"
        print img
        h_of = img.split(".")[0][-4:]
        hash_value = hash(h_of)
        print h_of
        hash_dict[img] = hash_value / (10 ** 16)
        print hash_dict[img]
        #:print hash_dict[img][:4]

pp(hash_dict)


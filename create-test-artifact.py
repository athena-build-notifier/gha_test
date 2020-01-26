import json
import time
import struct
import random

MEGABYTES_TO_BYTES = 1024 * 1024
FILE_READ_BUFFER = 4096

def generate_file(filename, sizeInMegabytes):
    f = open(filename, "wb")
    # add time at front
    f.write(bytearray(struct.pack("f", time.time())))
    # add some random value to get unique files
    f.write(bytearray(random.getrandbits(8) for _ in range(32)))
    f.seek((sizeInMegabytes * MEGABYTES_TO_BYTES) - 1)
    f.write(bytearray([1]))
    f.close()
    pass

temp_filename = 'temp_file.dat'

generate_file(temp_filename, 100)

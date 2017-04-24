import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import random

from drawnow import drawnow

if __name__ == '__main__':
    with open('dummy.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(range(1024))
        for i in range(10):
            writer.writerow(range(1024, 2048))

import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
import time


def count_bdate(bdate_list):
    ages = []
    curr_date = datetime.date.today()
    for i in bdate_list:
        tempd = i.split(".")
        my_date = datetime.date(int(tempd[2]), int(tempd[1]), int(tempd[0]))
        delta = ((curr_date - my_date).total_seconds()) / 365 / 24 / 3600

        ages.append(int(delta))

    return ages


def histog(array):
    plt.hist(array)
    plt.show()

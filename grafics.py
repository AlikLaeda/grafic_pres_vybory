import matplotlib.pyplot as plt
import csv, io
import numpy as np

headers = []

def all_list():
    global headers
    rows = []
    with io.open('results-uik-20240325T0139UTC.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        for row in reader:
            rows.append(row)
    return rows

def slice_one_region(region: str):
    target_rows = []
    for row in all_list():
        if row[0] == region:
            target_rows.append(row)
    return target_rows

def slice_one_tik_from_region(region_list: list, tik: str):
    target_rows = []
    for row in region_list:
        if row[1] == tik:
            target_rows.append(row)
    return target_rows

def slice_one_tik(region: str, tik: str):
    target_rows = []
    for row in all_list():
        if (row[0] == region) & (row[1] == tik):
            target_rows.append(row)
    return target_rows


if __name__ == "__main__":

#    tik = slice_one_tik('Московская область', 'Люберецкая городская')
    tik = slice_one_region('Московская область')
    k=0
    # for i in headers:
    #     print(f"{k}: {i}")
    #     k +=1
    # print(headers)
    x = []
    y = []    
    color_a = []

    yavka_bolshe_99 = []
    inkumb_menshe_40 = []
    
    for uik in tik:
        x.append((int(uik[9])+int(uik[10]))/int(uik[3]))
        y.append(int(uik[17])/(int(uik[9])+int(uik[10])))
        if int(uik[3]) < 200:
            color_a.append(('blue', 0.1))
        elif int(uik[3]) > 2000:
            color_a.append(('blue', 1))
        else:
            color_a.append(('blue', int(uik[3])/2000))
        # if (int(uik[9])+int(uik[10]))/int(uik[3]) > 0.99:
        #     print(uik)
        #     yavka_bolshe_99.append(uik)
        if (int(uik[17]))/(int(uik[9])+int(uik[10])) < 0.5:
            print(uik)
            inkumb_menshe_40.append(uik)
        
 
#    plt.style.use('_mpl-gallery')
    fig, ax = plt.subplots()
    plt.xlabel('Явка')
    plt.ylabel('Результат инкумбента')
    
    ax.scatter(x, y, c=color_a, s=1)
    ax.set(xlim=(0, 1),
           ylim=(0, 1))
    plt.grid(True, which='both', linestyle='-')
    ax.set_yticks(np.arange(0, 1.01, 0.1))
    ax.set_yticks(np.arange(0, 1.01, 0.05), minor=True)
    ax.set_xticks(np.arange(0, 1.01, 0.1))
    ax.set_xticks(np.arange(0, 1.01, 0.05), minor=True)
    plt.show()

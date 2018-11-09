import array as arr

import matplotlib.pyplot as plt

filepath = '10-06-2018.asc'
a = [1, 3.5, "Hello"]
with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        n_column = line.split()
        ncols = int(n_column[1])
        print(ncols)

        line = fp.readline()
        n_rows = line.split()
        nrows = int(n_rows[1])
        print(nrows)

        line = fp.readline()
        x_llcorner = line.split()
        xllcorner = float(x_llcorner[1])
        print(xllcorner)

        line = fp.readline()
        y_llcorner = line.split()
        yllcorner = float(y_llcorner[1])
        print(yllcorner)

        line = fp.readline()
        x_cellsize = line.split()
        cellsize = float(x_cellsize[1])
        print(cellsize)

        line = fp.readline()
        NO_DATA_value = line.split()
        NODATA_value = float(NO_DATA_value[1])
        print(NODATA_value)

        line = fp.readline()
        x = arr.array("d",[])
        while line:

            #print(line.strip())
            tempt= line.split()
            for i in range(0, ncols):

               # print("ID {}: {}".format(i+1, tempt[i]))'

                a = arr.array('d', [xllcorner,yllcorner,float(tempt[i])])
                #print(a[2])
                if a[2]==-9999:
                   a[2]= 0
                x.append(a[2])
                line = fp.readline()

#plt.plot(1, x, 'bo')
for row in line:
    float(row)
    print(row)


print(x)
plt.plot(x,'bo')
plt.xlabel('x test label')
plt.ylabel('y test label')
plt.title("Test title")

plt.legend()

plt.show()
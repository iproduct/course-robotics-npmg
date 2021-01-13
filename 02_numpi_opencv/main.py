import numpy as np

if __name__ == '__main__':
    arr = np.array([
        [1, 2, 3, 4, 5],
        [11, 11, 13, 14, 15],
        [31, 32, 33, 34, 35],
        [41, 42, 43, 44, 45],
    ])
    print(f'Dimensions: {arr.ndim}')
    print(f'Shape: {arr.shape}')
    print(arr)
    print(arr[1,3])
    print(arr[0:4:2])
    print(arr[3][1:])

    for row in arr:
        for col in row:
            print(f"{col}\t", end = '')
        print()

    for idx, x in np.ndenumerate(arr):
        print(f'{idx} -> {x}')

    filter = [True, False, False, True]
    print(arr[filter])
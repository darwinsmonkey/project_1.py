import random
import time

# the moment the code starts running
starting = time.time()

# This dictionary contains the information needed to convert bit numbers to hex numbers.
encoder = {"0000": "0",
           "0001": "1",
           "0010": "2",
           "0011": "3",
           "0100": "4",
           "0101": "5",
           "0110": "6",
           "0111": "7",
           "1000": "8",
           "1001": "9",
           "1010": "A",
           "1011": "B",
           "1100": "C",
           "1101": "D",
           "1110": "E",
           "1111": "F"}

# Variables to contain initial, temporary and final data
x = 0
bit_count = 64 * int(input('Sayı Giriniz: '))
data_base = []
temp_data_set = ''
final_data_set = []

# This loop creates the random bit array with given lenght (in bit_count) and stores it in data_base variable.
while bit_count > x:
    data_base.append(random.randint(0, 1))
    x += 1

# This loop goes until initial data (in data_base) is run out. Truncates the data belonging to the database list in 4 pieces and loads them into temp_data.
# Finds the hex equivalent of each part and loads it into final_data.
while data_base:
    for i in range(4):
        temp_data_set += str(data_base.pop(0))
    final_data_set.append(encoder[temp_data_set])
    temp_data_set = ''

# This loop runs for one-thirty two of the total number of bits (This is because each hex consists of 4 bits and we have to put 8 bits next to each other).
# This loop has a control flow so that previously joined parts are not joined again (Break statement).
# This loop cuts 8 units of data, concatenates them, stores them in a temporary string and restores them to the data set.
for a in range(int(bit_count / 32)):
    if len(final_data_set[0]) == 0 or len(final_data_set[0]) == 1:
        for i in range(8):
            temp_data_set += str(final_data_set.pop(0))
        final_data_set.append(temp_data_set)
        temp_data_set = ''
    else:
        break

print(final_data_set)
# Calculates the time period from when the code starts to run until it finishes
print(f"geçen süre {time.time()-starting}")




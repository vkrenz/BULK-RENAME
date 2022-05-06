import os
from datetime import datetime

i = 0

# dd/mm/yyyy H:M:S
now = datetime.now()
dt = now.strftime("[%d-%m-%y]")


def main():
    count = 0
    path = input("\nPlease enter path: ")
    path = path.replace('\\', '/') + '/'
    selection = input("\nSave as:\n[1] JPG\n[2] JPEG\n\n... ")
    opt = '.jpg' if selection == 1 else '.jpeg'
    # print("Selection: {}".format(selection) + " Type: {}".format(type(selection)))
    for file in os.listdir(path):
        count += 1
        my_dest = 'Image_' + str(count) + " " + dt + opt
        my_src = path + file
        my_dest = path + my_dest
        os.rename(my_src, my_dest)

if __name__ == '__main__':
    main()
    print("\nDone!")

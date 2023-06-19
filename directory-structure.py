import os

path = "./test-directory/test-one/test2"

#os.mkdir(path)


if not os.path.exists(path):
    os.mkdir(path)
    print('Folder %s successfully created' % path)
else:
    print('Folder %s already exists' % path)


try:
    os.makedirs(path)
    print('Folder %s successfully created' % path)
except FileExistsError:
    print('Folder %s already exists' % path)

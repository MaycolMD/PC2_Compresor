import sys

f1 = open(sys.argv[1], 'rb')
rawdata1 = f1.read()
f1.close()

f2 = open('descomprimido-elmejorprofesor.txt', 'rb')
rawdata2 = f2.read()
f2.close()

if rawdata1 == rawdata2:
    print('ok')
else:
    print('nok')
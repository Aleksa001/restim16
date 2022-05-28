from Scripts.Podatak import Podatak
def loadFromFile(fileName):
    file = open(fileName)
    filePodaci = []  # niz vrednosti iz fajla
    for line in file.readlines():
        print(line.strip() + "!")
        filePodaci.append(line.strip())
    podaci = []
    for x in range(len(filePodaci)):
        if (x % 2 == 0):
            podaci.append(Podatak(filePodaci[x], filePodaci[x + 1]))

    for pod in podaci:
        print(f"Id brojila: {pod.id} \nVrednost brojila: {pod.vrednostBrojila}\n")
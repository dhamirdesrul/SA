import random
import math

def fungsi(x1,x2):
    akar = math.sqrt((x1**2)+(x2**2))
    f = -1*(abs(math.sin(x1) * math.cos(x2) * math.exp(abs(1 - (akar/math.pi)))))
    return f

def randomNilai():
    x = float(random.uniform(-10, 10))  # menentukan batasan dari nilai x secara random
    return x

def probabilitas(deltaE):
    prob = math.exp(-1*(deltaE)/T_max) #mencari selisih antar state
    return prob

def pembandingProbabilitas():
    pp = float(random.uniform(0, 1)) #melakukan random probabilitas untuk dijadikan pembanding
    return pp

if __name__ == "__main__":
    x1 = randomNilai() #menentukan batasan dari nilai x1 secara random
    x2 = randomNilai() #menentukan batasan dari nilai x2 secara random
    T_max = 100 #nilai suhu bebas dan ditentukan sesuai dengan nilai dari fungsi terkecil
    T_min = 0.001

    #mencari state
    currentState = fungsi(x1,x2)
    bestSoFar = currentState

    while (T_max > T_min):
        #mencari nilai lagi dan akan selalu memaksukan ke dalam data sebagai new state yang dibutuhkan dalam mencari nilai pernodenya
        x1 = randomNilai()  # menentukan batasan dari nilai x1 secara random
        x2 = randomNilai()  # menentukan batasan dari nilai x2 secara random

        #memanggil fungsi dengan mengisi nilai x1 dan x2 yang telah di random menjadi newState
        newState = fungsi(x1,x2)
        deltaE = newState - currentState #mencari nilai deltaE untuk melanjutkan ke dalam rumus
        #print(newState, deltaE)

        if (deltaE < 0):
            #ketika nilainya dibawah 0 maka current state diisi dengan new state dan best so far diisi dengna ncurrent state
            currentState = newState
            bestSoFar = currentState
            #print(bestSoFar, currentState)

        elif (deltaE >= 0):
            probs = probabilitas(deltaE)

            #menentukan nilai yang baru untuk dapat dibandingkan dengan probabilitas yang sebelumnya
            pembandingprob = pembandingProbabilitas()  #interval dari probabilitas yakni 0 sampai 1

            #dilakukan pengecekan terhadap pembanding probabilitas dengan probabilitas
            if (pembandingprob < probs):
                currentState = newState
                bestSoFar = currentState
                T_max = T_max * 0.009

    print('nilai best: ', bestSoFar)
    print('nilai x1: ', x1)
    print('nilai x2: ', x2)
    print('nilai deltaE: ', deltaE)













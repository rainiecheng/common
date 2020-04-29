import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# for norm
# theta choices


def T_mean(x):
    return np.mean(x)


def T_var(x):
    return (np.sum((x-np.mean(x))**2))/len(x)


def del_1_jk():
    X = np.random.normal(loc=0, scale=1, size=100).tolist()
    full_T = T_mean(X)
    # full_T = T_var(X)
    del_1_T_i = []
    pseudo_T_i = []

    for i in range(0, len(X)):
        X_temp = X[:i] + X[i+1:]
        del_1_T_i.append(T_mean(X_temp))
        # del_1_T_i.append(T_var(X_temp))
        pseudo_T_i.append(len(X)*full_T - len(X_temp)*T_mean(X_temp))
        # pseudo_T_i.append(len(X) * full_T - len(X_temp) * T_var(X_temp))


    jack_T =np.mean(pseudo_T_i)
    bias = full_T - jack_T
    return jack_T, bias


    # print(jack_T, bias)

if __name__ == '__main__':
    AN_test = []
    n = 100
    # AN_test.append(jack_T)
    for i in range(0, n):
        AN_test.append(del_1_jk()[0])

    plt.hist(AN_test,color='red', alpha=0.4)
    plt.show()
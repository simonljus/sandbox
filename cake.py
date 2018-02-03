import numpy as np
import matplotlib.pyplot as plt

'''
A simple interactive tool for plotting how Swedes eat cake
'''
def cakeGraph(original_size_of_cake,n_bits):
    vfun = np.vectorize(cakeLeft,otypes=[np.float])
    x = range(n_bits +1)
    y=vfun(original_size_of_cake,x)
    fig,ax = plt.subplots()
    xy = zip(x,y)
    normal_label = True
    swede_label = True
    for i in range(n_bits):
        if (y[i] <= 1.0):
            plot_color = "red"
            plot_label = "'I can not take all of it but I can take half'"
            if swede_label:
                ax.plot(x[i:i+2],y[i:i+2],color=plot_color,label=plot_label)
                swede_label = False
            else:
                ax.plot(x[i:i+2],y[i:i+2],color=plot_color)
        else:
            plot_color = "blue"
            plot_label = "takes a regular sized piece"

            if normal_label:
                ax.plot(x[i:i+2],y[i:i+2],color=plot_color,label=plot_label)
                normal_label = False
            else:
                ax.plot(x[i:i+2],y[i:i+2],color=plot_color)
        

       

    if original_size_of_cake ==1:
        plt.title("How Swedes eat the last bit of cake")
    else:
        plt.title("How Swedes eat cake")
    plt.xlabel("Pieces taken")
    plt.ylabel("Cake left")
    plt.xticks(range(n_bits +1))
    plt.legend()
    plt.show()

def cakeLeft(original_size_of_cake,part):
    #return amount of cake left
    if original_size_of_cake > 0:
        if original_size_of_cake <= part:
            return 1.0/(2**(part - original_size_of_cake + 1 ))
        else:
            return original_size_of_cake - part






if __name__== "__main__": 
    print("Welcome to Swedish cake plotter\n")
    need_input = True
    cake_size = 4
    bits = 12
    while(need_input):
        try:
            cake_size = int(input("how big is your cake [enter a positive integer] \n"))
            bits =int(input("How many rounds will the cake been shared [enter a positive integer] \n"))
            if cake_size > 0 and bits > 0:
                need_input = False
        except:
            print("Positive integers are required to get an awesome cake plot \n")

    cakeGraph(cake_size,bits)
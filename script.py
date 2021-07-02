import os
import matplotlib.pyplot as plt
import numpy as np

class GraphVars():
    def __init__(self):
        # str
        self._title = None
        self._plot_name = None
        # list
        self._plot_names = None


def main():
    
    def read_data():

        '''
        Lê o arquivo de dados
        '''

        data = open('plots.slevel.txt', 'r')
        return data


    def start_name(GraphVars):
        
        '''
        Pega os nomes dos plots disponíveis
        '''

        GraphVars._plot_names = list()
        for line in data:
            if line.startswith('start_bar'):
                GraphVars._plot_name = line.split()[1]
                GraphVars._plot_names.append(GraphVars._plot_name)
        return GraphVars._plot_names
    
    def get_data(GraphVars):
        '''
        Lidando com o arquivo de dados
        '''

        data = read_data()
        text = []
        record = False

        for line in data:
            if line.startswith('start_bar ' + GraphVars._plot_name):
                record = True
                text = []
            if record:
                text.append(line)
            if line.startswith('end_plot'):
                record = False
            
                with open("%s.dat" % GraphVars._plot_name,"w") as new_file:
                    lines ='\n'.join(text)  # limpa o cabeçalho das linhas
                    new_file.write(lines)
                new_file.close()

                with open("%s.dat" % GraphVars._plot_name,"r") as read_file:
                    for line in read_file:
                        if line.startswith('   title ='): 
                            GraphVars._title = line.strip('title =').replace("'","")
                        if line.startswith('   data'): 
                            record = True
                            text =[]
                        if record:
                            text.append(line.strip())
                        if line.startswith('end_plot'):
                            record = False

                            with open("%s-data.dat" % GraphVars._title,"w") as new_file:
                                lines ='\n'.join(text[1:-1])  # limpa o cabeçalho das linhas
                                new_file.write(lines)
                            new_file.close()
        return


    def gen_graph(GraphVars):
        '''
        Graphic Generation
        '''

        data_plot = np.loadtxt('%s-data.dat' % GraphVars._title, unpack = True)
        colors = ['#66ccff', '#cc3399', '#669999', '#ff6600', '#0066cc', '#6600cc',
                  '#999966', '#993399', '#ffbf80', '#ff3300', '#00ffcc', '#006699', 
                  '#99ff99', '#ffff00', '#ff0000', '#ff00ff', '#000066', '#ffff99', 
                  '#996600', '#6666ff', '#663300', '#ff66ff', '#ccff33', '#003300', 
                  '#ff9900', '#3366cc', '#000000']

        # fatiamento

        explode = []
        i = 0

        while i < len(data_plot[0]):
            explode.append(0)
            i += 1



        fig, ax = plt.subplots(figsize=(6.5,6.0))

        #ax.pie(data[1], explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)  

        ax.pie(data_plot[1], explode=explode, colors=colors, shadow=True, startangle=140, normalize=True)  #sem porcentagem
        ax.set_title(GraphVars._title)

        plt.legend(data_plot[0],bbox_to_anchor=(1.05,0.95), loc="upper right")
        plt.savefig('%s.pdf' % GraphVars._title)

        os.system('rm *.dat')
        return

    data = read_data() 
    nfp = start_name(GraphVars)
    i = 0
    print("")
    print("")
    print("")
    print("These are the available plots in the data file:")
    print("")
    print("")
    print("")
    print("Please, choose the weight plot by a number")
    print("")
    print("")
    print("")
    for name in nfp:
        print('('+ str(i) + ')', name)
        i += 1 
    print("")
    print("")
    print("")
    plot_number = int(input("What plot do you choose? "))
    if plot_number > (int(len(nfp)) - 1):
        print("")
        print("")
        print("")
        print("ERROR: Number greater than the available plots")
    else:
        GraphVars._plot_name = nfp[plot_number] 

    
    get_data(GraphVars) # pega os dados
    gen_graph(GraphVars) # gera os gráficos


main()
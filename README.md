# PIE-Plot-V2

#------------------------------------------#
#         English instructions             #
#------------------------------------------#

This script is written in Python3 to plot pie charts ONLY for weight results generated by Pilgrim.

The user needs the followings libraries:
- os
- matplotlib
- numpy

Instructions for use:

Data file:

1) The data file 'plots.slevel.txt' needed for the plot, can be found in folder '6-PLOTFILES' originated by the Pilgrim.


Are available 21 different colors and more can be added to the list of colors inside the function 'gen_graph' belonging to the script. The order of the colors also can be changed.
Is recommended that the inclusion of colors is made using the hexadecimal code.


This script only accepts the file 'plots.slevel.txt'. And don't plot another plot type beyond weight.

The generated graphics are saved in '.pdf' extension inside the folder.


#------------------------------------------#
#         Portuguese instructions          #
#------------------------------------------#


Este script é escrito em Python3 para plotar APENAS resultados 'weight' originários do Pilgrim.

O usuário precisa das seguintes bibliotecas:
- os
- matplotlib
- numpy

Instruções de uso:

Arquivos de dados:
1) O arquivo de dados 'plots.slevel.txt' necessário para o plot pode ser encontrado na pasta '6-PLOTFILES' criada pelo Pilgrim.


Estão disponíveis 21 cores diferentes e mais podem ser adicionadas na matriz de cores dentro da função 'plot_data' pertencente ao script. A ordem das cores também pode ser alterada. Recomenda-se que a inclusão de cores seja feita utilizando o código hexadecimal.

Este script só aceita o arquivo 'plots.slevel.txt'. E não realiza os plot para  qualquer outro tipo de plot além do peso de cada conformero.

Os gráficos gerados são salvos na extensão '.pdf' dentro da pasta.
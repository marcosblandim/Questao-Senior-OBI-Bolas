# Questao-Senior-OBI-Bolas
Solução em Python da questão (com o nome de "Bolas") nivel sênior da OBI 2018 fase 3.

# Descrição:
Podemos notar que a única condição para que não tenhamos bolas com números iguais lado-a-lado é que não haja uma quantidade de bolas repetidas maior que a metade do total de bolas, pois isso faria com que se "lotasse" as posições, levando a ocorrer ao menos duas bolas repetedidas lado a lado. Portanto, foi-se desenvolvido um código que faz essa verificação: preenche-se um dicionário com a quantia de cada bola, e então é procurada uma que tenha cinco ou mais bolas, retornando "N" caso encrontando e "S" caso contrário.
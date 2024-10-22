import networkx as nx
import matplotlib.pyplot as plt    
from random import choice,randint

ogrenciler = ['Yunus','Berat','Altun','Huseyin','Yavuz','Akif','Selin','Zeynep','Zeynep Elif','Melek Sude','Hasan','Efe','Arda','Belinay','Aysu','ilker','Talha','Umut','Esma','Dila','Dilara','Duru','Nurdane','Almina','Mustafa','M. Berat','Yakup','Irem','Azra']
kume = len(ogrenciler)

G = nx.DiGraph()
G.add_node(ogrenciler[0])


for i in range(kume):
    a1= choice(ogrenciler)
    a2 = choice(ogrenciler) 
    while a1 == a2:
        a1= choice(ogrenciler)
        a2 = choice(ogrenciler)
    G.add_edge(a1,a2,weight=randint(3,10))
    o = choice([0,1])
    if o == 1:
        G.add_edge(a2,a1,weight=randint(3,10))

pos = nx.circular_layout(G)
nx.draw(G,pos,node_size=1000, with_labels=True,font_size=10)

labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')

fig = plt.gcf()
fig.canvas.manager.set_window_title('10/D Sosyal Ag Tablosu')

plt.show()  

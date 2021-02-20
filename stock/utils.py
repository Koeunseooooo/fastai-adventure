import matplotlib.pyplot as plt 
import base64
from io import BytesIO


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer,format = 'png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph 

def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title("Stock value",fontweight="bold")
    plt.plot(x,y)
    # plt.xticks(rotation = 45)
    plt.xlabel('mm - dd - hh',fontweight="bold") 
    plt.ylabel('value',fontweight="bold")
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_bar_graph(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title("Probability for each class",fontweight="bold")
    plt.bar(x,y,align='center',color="midnightblue")
    plt.xticks(rotation = 45)
    plt.xlabel('class',fontweight="bold")
    plt.ylabel('percentage',fontweight="bold")
    plt.tight_layout()
    graph = get_graph()
    return graph
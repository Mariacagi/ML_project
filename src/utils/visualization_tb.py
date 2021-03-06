import matplotlib.pyplot as plt
import seaborn as sns

# PARA CAMBIAR DE CM A PULGADAS

def cm_to_inch(value):
    return value/2.54

# PARA HACER UN HISTOGRAMA
def histogram_figure(x, y, x_label, y_label, rooth_path, name_fig):
    # Creación de la figura
    plt.figure(figsize=(cm_to_inch(20),cm_to_inch(10)))
    plt.bar(x=x, height=y, facecolor='#222220')

    #Etiquetas
    plt.xlabel(x_label, weight="bold")
    plt.ylabel(y_label, weight="bold")
    plt.xticks(rotation="90")

    # Guarda la figura
    carpeta_reports = "\\reports"
    plt.savefig(rooth_path + carpeta_reports + name_fig, dpi=300, bbox_inches='tight')

    # Muestra la figura
    plt.show()

# PARA HACER UN PIE CHART
def piechart_figure(x1, x2, x3, x4, x5, x6, labels, name_fig, rooth_path):
    
    plt.figure(figsize=(cm_to_inch(20),cm_to_inch(20)))

    colors = ["#222220","#2C2C2C", "#434343", "#62635D", "#868781", "#D6D6D4"]
    # colors = ["#3d4248","#222E3E", "#4D6380", "#5579A9", "#6B737E", "#C4CBD6"]

    plt.pie([x1, x2, x3, x4, x5, x6], labels = labels, colors=colors, autopct="%.1f %%")    

    # Guarda la figura
    carpeta_reports = "\\reports"
    plt.savefig(rooth_path + carpeta_reports + name_fig, dpi=300, bbox_inches='tight')

    # Se muestra la figura
    plt.show()

def piechart_figure_5labels(x1, x2, x3, x4, x5, labels, name_fig, rooth_path):
    
    plt.figure(figsize=(cm_to_inch(20),cm_to_inch(20)))
    
    colors = ["#2C2C2C", "#434343", "#62635D", "#868781", "#D6D6D4"]
    # colors = ["#3d4248","#222E3E", "#4D6380", "#5579A9", "#6B737E", "#C4CBD6"]

    plt.pie([x1, x2, x3, x4, x5], labels = labels, colors=colors, autopct="%.1f %%")    

    # Guarda la figura
    carpeta_reports = "\\reports"
    plt.savefig(rooth_path + carpeta_reports + name_fig, dpi=300, bbox_inches='tight')

    # Se muestra la figura
    plt.show()


def diagramalinea_figure(x, y, x_label, y_label, rooth_path, name_fig):

    plt.figure(figsize=(cm_to_inch(20),cm_to_inch(10)))

    # Creación de la figura
    plt.plot(x, y, color='#434343', marker=".", markersize=15, linewidth= 3, label="Year")

    #Etiquetas
    plt.xlabel(x_label, weight="bold")
    plt.ylabel(y_label, weight="bold")
    plt.xticks(rotation="90")

    # Guarda la figura
    carpeta_reports = "\\reports"
    plt.savefig(rooth_path + carpeta_reports + name_fig, dpi=300, bbox_inches='tight')

    # Muestra la figura
    plt.show()


def correlation_matrix(df):
    
    plt.figure(figsize=(cm_to_inch(30),cm_to_inch(20)))

    correlation_ = df.corr()
    heatmap_ = sns.heatmap(correlation_, cmap="bone",annot=True)
    fig_cor_ = heatmap_.get_figure()

    # Etiquetas
    plt.yticks(va="center", rotation = 0)
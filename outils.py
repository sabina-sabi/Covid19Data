import matplotlib.pyplot as plt 

def visualiser_valeurs_aberrantes(df):
    # Créer des box plots pour chaque variable
    df.boxplot(figsize=(12, 6))
    # Ajouter un titre et des étiquettes aux axes
    plt.title("Box plot des variables")
    plt.xlabel("Variables")
    plt.ylabel("Valeurs")
    # Afficher le graphique
    plt.show()
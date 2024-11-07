import matplotlib.pyplot as plt

def main(a):
    fig, ax = plt.subplots(figsize=(4, 2))

    ax.axis('off')

    ax.text(0.5, 0.5, r"$%s$" % (a), fontsize=30, color="black", ha='center', va='center')
    plt.savefig("formula.png", dpi = 300, bbox_inches='tight')

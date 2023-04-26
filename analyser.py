import os
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")

#product_code = input("Podaj kod produktu: ")
product_code = 105563156

opinions = pd.read_json(f"./opinions/{product_code}.json")
opinions.score = opinions.score.map(lambda x: float(x.split("/")[0].replace(",",".")))

opinions_count = opinions.shape[0]  #len(opinions.index)    #opinions.opinion_id.count()
pros_count = opinions.pros.map(bool).sum()
cons_count = opinions.cons.map(bool).sum()
#pros_count = sum([False if len(p)==0 else True for p in opinions.pros])
#cons_count = sum([False if len(c)==0 else True for c in opinions.cons])
#pros_count = opinions.pros.map(lambda p: False if len(p)==0 else True).sum()
#cons_count = opinions.cons.map(lambda c: False if len(c)==0 else True).sum()
avg_score = opinions.score.mean().round(2)

print(f"""Dla produktu o kodzie {product_code} pobrano {opinions_count} opinii/opinie. 
Dla {pros_count} opinii dostępna jest lista  zalet, a dla {cons_count} opinii dostępna est lista wad. 
Średdnia ocena produktu wynosi {avg_score}.""")

# histogram częstości występowania poszczególnych ocen
score = opinions.score.value_counts().reindex(list(np.arange(0,5.5,0.5)), fill_value=0)
#print(score)
score.plot.bar(color="hotpink")
#plt.show()
plt.savefig(f"./plots/{product_code}_score.png")
plt.close()

# udział poszczególnych rekomendacji w ogólnej liczbie opinii
recommendation = opinions["recommendation"].value_counts(dropna = False).sort_index()
print(recommendation)
recommendation.plot.pie(label="",autopct ="%1.1f%%")
plt.savefig(f"./plots/{product_code}_recommendation.png")
plt.close()
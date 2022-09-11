#%% read the lib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

#%%
masterFile = pd.read_csv('C:/Users/VigneshwarPesaru/Downloads/course-project-Vigneshwar5072-master/course-project-Vigneshwar5072-master/data/players_20.csv')
#plot-3
#%%
def func():
    dff=masterFile[["player_traits","sofifa_id"]]
    dff['player_traits_count']=dff.player_traits.str.count(', ')+1
    dff.sort_values("player_traits_count",ascending=False,inplace=True)
    dff=dff.iloc[0:10]
    plt.title("Players having top 10 largest number of player_traits")
    plt.tick_params(axis='x', rotation=45)
    return sns.barplot(data=dff,x='sofifa_id',y='player_traits_count')

#%%
output  = func()


#%%
#plot 2

def value():
    dff=masterFile[["value_eur","sofifa_id"]]
    dff=masterFile.sort_values("value_eur",ascending=False)
    dff=dff.iloc[0:5]
    
    plt.title("Players having top 5 highest value_eur")
    plt.tick_params(axis='x', rotation=45)
    return sns.barplot(data=dff,x='sofifa_id',y='value_eur')
#%%

plot2 = value()

#%%
# Defining a empty list
mean_list = []

#%%
# Defining a function to calculate improvement percentage based on average across all skillsets
def func():
    
    dff = masterFile[["attacking_crossing","goalkeeping_reflexes"]]
    mean_list = [dff["attacking_crossing"].mean(axis=0),dff["goalkeeping_reflexes"].mean(axis=0)]
    attacking_crossing=[]
    goalkeeping_reflexes=[]

    k=0
    for i in ["attacking_crossing","goalkeeping_reflexes"]:
        for j in range(len(dff)):
            if i=="attacking_crossing":
                a=((dff[i][j]-mean_list[k])/mean_list[k])*100
                attacking_crossing.append(a)
            if i=="goalkeeping_reflexes":
                b=((dff[i][j]-mean_list[k])/mean_list[k])*100
                goalkeeping_reflexes.append(b)
        k+=1

    dff1=pd.DataFrame(attacking_crossing,columns=["attacking_crossing"])
    dff1["sofifa_id"]=masterFile["sofifa_id"]
    dff1=dff1.sort_values("attacking_crossing",ascending=False)
    dff1=dff1.iloc[0:10]

    dff2=pd.DataFrame(goalkeeping_reflexes,columns=["goalkeeping_reflexes"])
    dff2["sofifa_id"]=masterFile["sofifa_id"]
    dff2=dff2.sort_values("goalkeeping_reflexes",ascending=False)
    dff2=dff2.iloc[0:10]
    
    return (dff1,dff2)

#%%
def highest_improvement():
    (dff1,dff2) = func()
    
    plt.title("Players having top improvements in different skills")
    plt.tick_params(axis='x', rotation=90)
    sns.barplot(data=dff1,x='sofifa_id',y='attacking_crossing')
    plt.show()
    
    plt.title("Players having top improvements in different skills")
    plt.tick_params(axis='x', rotation=90)
    sns.barplot(data=dff2,x='sofifa_id',y='goalkeeping_reflexes')
    plt.show()


#%%

highest_improvement()


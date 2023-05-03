'''
Created on 2023. 5. 3.

@author: admin
'''
from djang_webboard.settings import STATIC_DIR, TEMPLATE_DIR
import os, folium
import pandas as pd
from folium import plugins
from konlpy.tag import Hannanum
from nltk import Text
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import rc,font_manager
import matplotlib
matplotlib.use('agg')

def wordcloud():
    font_path='C:/Windows/Fonts/gulim.ttc'
    font_name=font_manager.FontProperties(fname=font_path).get_name()
    rc('font',family=font_name)
    
    path=os.path.join(STATIC_DIR,'data/word_data.txt')
    
    df=open(path, 'r' , encoding='UTF-8').read()
    
    han=Hannanum()

    yes_fd=Text(han.nouns(df), name='yes')
    
    
    wc=WordCloud(width=800, height=600, background_color='white', font_path=font_path)
    plt.imshow(wc.generate_from_frequencies(yes_fd.vocab())) #fd를 써도된다
    plt.axis('off')
    plt.savefig(os.path.join(STATIC_DIR, 'images/wordcloud.png'))
    
def cctv_map():
    popup=[]
    locations=[]
    
    path=os.path.join(STATIC_DIR,'data/CCTV_20190917.csv')
    
    df=pd.read_csv(path)
    
    for data in df.values:
        if data[4]>0:
            popup.append(data[1])
            locations.append([data[10],data[11]])
     
    m=folium.Map([35.1803305, 129.0516257], zoom_start=11)
    plugins.MarkerCluster(locations, popups=popup).add_to(m)
    m.save(os.path.join(TEMPLATE_DIR, 'map/map01.html'))       
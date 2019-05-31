# import libraries
from bs4 import BeautifulSoup
#import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import time
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#DATA SEBARAN PDRB JATIM
url2 = 'https://jatim.bps.go.id/dynamictable/2017/07/05/36/distribusi-pdrb-provinsi-jawa-timur-atas-dasar-harga-berlaku-menurut-lapangan-usaha-tahun-2010-2016-persen-.html'
# The path to where you have your chrome webdriver stored:
webdriver_path = 'E:\chromedriver_win32\chromedriver.exe'

# Add arguments telling Selenium to not actually open a window
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1920x1080')
browser = webdriver.Chrome(executable_path=webdriver_path,
                           options=chrome_options)
# Load webpage
browser.get(url2)

# It can be a good idea to wait for a few seconds before trying to parse the page
# to ensure that the page has loaded completely.
time.sleep(10)

# Parse the raw into delicious soup
soup2 = BeautifulSoup(browser.page_source, 'html.parser')

def PDRB01():
    tabel2 = soup2.find('table', attrs={'id':'tableRightBottom'})
    hasil2 = tabel2.find_all('tr')
    print(hasil2)

    wilJatim = []
    wilJatim.append(['Provinsi Jatim'])
    indeksPDRB = []
    t2010 = []
    t2011 = []
    t2012 = []
    t2013 = []
    t2014 = []
    t2015 = []
    t2016 = []

    # loop over hasil
    for h2 in hasil2:
        # find all columns per result
        dataTot2 = h2.find_all('td', attrs={'class':'datas'})
        # check that columns have data
        if len(dataTot2) == 0:
            continue

        thn2010 = dataTot2[0].getText()
        thn2011 = dataTot2[1].getText()
        thn2012 = dataTot2[2].getText()
        thn2013 = dataTot2[3].getText()
        thn2014 = dataTot2[4].getText()
        thn2015 = dataTot2[5].getText()
        thn2016 = dataTot2[6].getText()

        # Remove decimal point
        thn2010 = thn2010.replace(' ','')
        thn2011 = thn2011.replace(' ','')
        thn2012 = thn2012.replace(' ','')
        thn2013 = thn2013.replace(' ','')
        thn2014 = thn2014.replace(' ','')
        thn2015 = thn2015.replace(' ','')
        thn2016 = thn2016.replace(' ', '')

        thn2010 = float(thn2010)
        thn2011 = float(thn2011)
        thn2012 = float(thn2012)
        thn2013 = float(thn2013)
        thn2014 =  float(thn2014)
        thn2015 = float(thn2015)
        thn2016 = float(thn2016)

        t2010.append(thn2010)
        t2011.append(thn2011)
        t2012.append(thn2012)
        t2013.append(thn2013)
        t2014.append(thn2014)
        t2015.append(thn2015)
        t2016.append(thn2016)

    indeksPDRB.append((t2010[-1]))
    indeksPDRB.append((t2011[-1]))
    indeksPDRB.append((t2012[-1]))
    indeksPDRB.append((t2013[-1]))
    indeksPDRB.append((t2014[-1]))
    indeksPDRB.append((t2015[-1]))
    indeksPDRB.append((t2016[-1]))


    #print indexSebaranPDRB
    PDRB = []
    PDRB.append('Pertanian, Kehutanan, dan Perikanan')
    PDRB.append('Pertambangan dan Penggalian')
    PDRB.append('Industri Pengolahan')
    PDRB.append('Pengadaan Listrik dan Gas')
    PDRB.append('Pengadaan Air, Pengelolaan Sampah, Limbah dan Daur Ulang')
    PDRB.append('Konstruksi')
    PDRB.append('Perdagangan Besar dan Eceran; Reparasi Mobil dan Sepeda Motor')

    print (PDRB)
    print (indeksPDRB)
    np_PDRB = np.array(PDRB)
    np_indeks = np.array(indeksPDRB)

    #naming Label
    plt.xlabel('PDRB')
    plt.ylabel('Distribusi PDRB Provinsi Jawa Timur')

    #styling x,y value
    plt.xticks(rotation=30,ha='right')
    plt.yticks(np.arange(np_indeks.min(),np_indeks.max(),4000000))

    #plot data
    #plt.subplot(2,1,2)
    plt.plot(np_PDRB,np_indeks,color='red',label='PDRB')
    plt.legend(loc='upper right')
    plt.yscale('linear')
    plt.show()


PDRB01()
from flask import Flask,send_file,render_template
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import csv
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.offline import iplot, init_notebook_mode
import calendar
from plotly.subplots import make_subplots





df = pd.read_csv('./powerconsumption.csv')
df.isnull().sum()
df.rename(columns={'Unnamed: 0':'Date'}, inplace=True)
df_long = pd.read_csv('./long_data_.csv')
df_long['Dates'] = pd.to_datetime(df_long.Dates, dayfirst=True)

a1=[]
for i in range(0,16):
    t=df.iloc[i];
    a1.append(t)
a2=[]
for i in range(0,16):
    t=df_long.iloc[i];
    a2.append(t)

#---plot1----
mean = df.mean().sort_values(ascending=False).reset_index().rename(columns = {"index": "state", 0 : "average consumption"})
state_code = ['MH', 'GJ', 'UP', 'TN', 'RJ', 'MP', 'KA', 'TG', 'AP', 'PH', 'WB', 'HR', 'CT', 'DL', 'BR', 'OR', 'KL', 'J&K', 'UK', 'HP', 'AS', 'JH', 'DNH', 'GA', 'PY', 'ML', 'CH', 'TR', 'MN', 'NL', 'AR', 'MZ', 'SK']
mean.state = state_code
plt.figure(figsize = (20,10))
sns.barplot(x= "state", y = "average consumption", data = mean)
plt.savefig('static/images/plot1.png')
#---plot2---
ax=sns.relplot(x="Regions",y="Usage", data=df_long, kind="line", markers=True)
plt.savefig("static/images/plot2.png")
plt.clf()
df['Date'] = pd.to_datetime(df.Date, dayfirst=True)

#---plot3---
grp=df_long.groupby('Regions')
re=grp.agg(np.mean)
regine=re[['Usage']]
regine.reset_index(inplace=True)
fig = plt.figure(figsize= (5,5))
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
rgn = regine['Regions']
use = regine['Usage']
ax.pie(use, labels = rgn,autopct='%1.2f%%')
plt.savefig("static/images/plot4.png")
plt.clf()
#---plot4---
df1=df[0:359]
df2=df[359:]
consumption = df1.sum(axis=0).sort_values(ascending=False).reset_index().rename(columns={"index": "state", 0: "Annual consumption 2019"})
consumption.state = state_code
plt.figure(figsize=(20, 10))
sns.barplot(x="state", y="Annual consumption 2019", data=consumption, color='green')
plt.savefig("static/images/plot5.png")
#---plot5---
consumption = df2.sum(axis=0).sort_values(ascending=False).reset_index().rename(columns={"index": "state", 0: "Annual consumption 2020"})
consumption.state = state_code
plt.figure(figsize=(20, 10))
sns.barplot(x="state", y="Annual consumption 2020", data=consumption, color='blue')
plt.savefig("static/images/plot6.png")
#---plot6---
df2 = df.copy()
df2.set_index('Date')
df2['NR'] = df2['Punjab']+ df2['Haryana']+ df2['Rajasthan']+ df2['Delhi']+df2['UP']+df2['Uttarakhand']+df2['HP']+df2['J&K']+df2['Chandigarh']
df2['WR'] = df2['Chhattisgarh']+df2['Gujarat']+df2['MP']+df2['Maharashtra']+df2['Goa']+df2['DNH']
df2['SR'] = df2['Andhra Pradesh']+df2['Telangana']+df2['Karnataka']+df2['Kerala']+df2['Tamil Nadu']+df2['Pondy']
df2['ER'] = df2['Bihar']+df2['Jharkhand']+ df2['Odisha']+df2['West Bengal']+df2['Sikkim']
df2['NER'] =df2['Arunachal Pradesh']+df2['Assam']+df2['Manipur']+df2['Meghalaya']+df2['Mizoram']+df2['Nagaland']+df2['Tripura']
df_new = pd.DataFrame({"Northern Region": df2["NR"].values,
                        "Southern Region": df2["SR"].values,
                        "Eastern Region": df2["ER"].values,
                        "Western Region": df2["WR"].values,
                        "North Eastern Region": df2["NER"].values},index=df2.index)
plt.figure(figsize=(10,10))
sns.heatmap(df_new.corr(),annot=True)
plt.savefig("static/images/plot7.png")
#---plot7---

plt.figure(figsize=(20,10))
x=df['Date']
y1=df_new['Northern Region']
y2=df_new['Southern Region']
y3=df_new['Eastern Region']
y4=df_new['Western Region']
y5=df_new['North Eastern Region']
plt.plot(x, y1, label="NR")
plt.plot(x, y2, label="SR")
plt.plot(x, y3, label="ER")
plt.plot(x, y4, label="WR")
plt.plot(x, y5, label="NER")
plt.legend()
plt.savefig("static/images/plot8.png")
#---plot8---
df3=df[357:430]
df4=df[431:]
before = df3.sum(axis=0)
after = df4.sum(axis=0)
df5 = before.compare(after)

df5.plot.bar(figsize=(20, 10))
plt.legend('', '')
plt.savefig("static/images/plot9.png")

#---plot9---
plt.figure(figsize=(20,20))
fig = px.scatter_geo(df_long,'latitude','longitude', color="Regions",
                     hover_name="States", size="Usage",
                      scope='asia')
fig.update_geos(lataxis_range=[5,35], lonaxis_range=[65, 100])





app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html',headings1=df.columns[:13],headings2=df_long.columns,data1=a1,data2=a2)

if __name__ == "__main__":
   app.run(debug=True)

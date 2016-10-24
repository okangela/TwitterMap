from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
from elasticsearch import Elasticsearch
#from elasticsearch import Elasticsearch
import time

import urllib, json

es = Elasticsearch([{'host': '54.163.11.20', 'port': 9200}])
es.indices.delete(index='twitter')
time.sleep(3)

application = Flask(__name__, template_folder="templates")


# you can set key as config
application.config['GOOGLEMAPS_KEY'] = "AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4"

# you can also pass key here
GoogleMaps(application, key="AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4")

t=0 
t1=0    
t2=0
t3=0
t4=0
t5=0
t6=0
t7=0
t8=0
t9=0   
@application.route('/twittmap',methods=["GET"])
#t=0
def fullmap():
    global t
    try:
        #url='http://54.163.11.20:9200/twitter/_search?pretty=true&size=1000'
        url='http://54.163.11.20:9200/twitter/_search?sort=@timestamp:desc&size=1000'
        response=urllib.urlopen(url)
        x=[]
        #t=len(x)
        #while(1):
        #time.sleep(1)
        data = json.loads(response.read())
        for i in range(len(data['hits']['hits'])):
            if(data['hits']['hits'][i]['_source']['geo']!=None):
                x.append( data['hits']['hits'][i]['_source']['geo']['coordinates'])
        #if len(x)>100:
         #   es = Elasticsearch([{'host': '54.163.11.20', 'port': 9200}])
          #  es.indices.delete(index='twitter')
           # t=0
           # time.sleep(1)

        temp=[]
        if t<len(x):
            for j in range(len(x)-t):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/red-dot.png',
                'lat': x[j][0],#37.4419,
                'lng': x[j][1],#-122.1419,
                'infobox': "Hello I am a new <b style='color:red;'>Tweet</b>!"})
            for k in range(len(x)-t,len(x)):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': x[k][0],#37.4419,
                'lng': x[k][1],#-122.1419,
                'infobox': "Hello I am a <b style='color:green;'>Tweet</b>!"})
            t=len(x)
        else:
            for j in range(len(x)/10):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/red-dot.png',
                'lat': x[j][0],#37.4419,
                'lng': x[j][1],#-122.1419,
                'infobox': "Hello I am a new <b style='color:red;'>Tweet</b>!"})
            for k in range(len(x)/10,len(x)):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': x[k][0],#37.4419,
                'lng': x[k][1],#-122.1419,
                'infobox': "Hello I am a <b style='color:green;'>Tweet</b>!"})


        #print temp
        fullmap = Map(
            identifier="fullmap",
            varname="fullmap",
            style=(
                "height:85%;"
                "width:100%;"
                "top:15%;"
                "left:0;"
                "position:absolute;"
                "z-index:200;"
            ),
            lat=30,
            lng=-90,
            markers=temp,zoom="2")
 
        return render_template('example_fullmap.html', fullmap=fullmap,response=response) 
    except Exception as e:
        application.run(debug=True, use_reloader=True)



@application.route('/hillary',methods=["GET"])

def fullmap1():
    global t1
    try:
        x1=[]
        url1='http://54.163.11.20:9200/twitter/_search?sort=@timestamp:desc&q=hillary&size=1000'
        response1=urllib.urlopen(url1)
        
        data1 = json.loads(response1.read())
        for i in range(len(data1['hits']['hits'])):
            if(data1['hits']['hits'][i]['_source']['geo']!=None):
                x1.append( data1['hits']['hits'][i]['_source']['coordinates']['coordinates'])
            else:
                x1.append(data1['hits']['hits'][i]['_source']['place']['bounding_box']['coordinates'][0][0])
        

        temp=[]
        if t1<len(x1):
            for j in range(len(x1)-t1):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/orange-dot.png',
                'lat': x1[j][1],#37.4419,
                'lng': x1[j][0],#-122.1419,
                'infobox': "Hello I am a new <b style='color:orange;'>Tweet</b>!"})
            for k in range(len(x1)-t1,len(x1)):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': x1[k][1],#37.4419,
                'lng': x1[k][0],#-122.1419,
                'infobox': "Hello I am a <b style='color:blue;'>Tweet</b>!"})
            t1=len(x1)
        else:
            for j in range(len(x1)/10):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/orange-dot.png',
                'lat': x1[j][1],#37.4419,
                'lng': x1[j][0],#-122.1419,
                'infobox': "Hello I am a new <b style='color:orange;'>Tweet</b>!"})
            for k in range(len(x1)/10,len(x1)):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': x1[k][1],#37.4419,
                'lng': x1[k][0],#-122.1419,
                'infobox': "Hello I am a <b style='color:blue;'>Tweet</b>!"})
        #t1=len(x1)

        #print temp
        fullmap1 = Map(
            identifier="fullmap1",
            varname="fullmap1",
            style=(
                "height:85%;"
                "width:100%;"
                "top:15%;"
                "left:0;"
                "position:absolute;"
                "z-index:200;"
            ),
            lat=30,
            lng=-90,
            markers=temp,zoom="2")
        return render_template('example_fullmap1.html', fullmap1=fullmap1,response1=response1)
    except Exception as e:
        application.run(debug=True, use_reloader=True)

@application.route('/trump',methods=["GET"])

def fullmap2():
    global t2
    try:
        x2=[]
        url2='http://54.163.11.20:9200/twitter/_search?sort=@timestamp:desc&q=trump&size=1000'
        response2=urllib.urlopen(url2) 
        data2 = json.loads(response2.read())
        for i in range(len(data2['hits']['hits'])):
            if(data2['hits']['hits'][i]['_source']['geo']!=None):
                x2.append( data2['hits']['hits'][i]['_source']['coordinates']['coordinates'])
            else:
                x2.append(data2['hits']['hits'][i]['_source']['place']['bounding_box']['coordinates'][0][0])
        temp=[]
        if t2<len(x2):
            for j in range(len(x2)-t2):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/yellow-dot.png',
                'lat': x2[j][1],#37.4419,
                'lng': x2[j][0],#-122.1419,
                'infobox': "Hello I am a new <b style='color:yellow;'>Tweet</b>!"})
            for k in range(len(x2)-t2,len(x2)):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/purple-dot.png',
                'lat': x2[k][1],#37.4419,
                'lng': x2[k][0],#-122.1419,
                'infobox': "Hello I am a <b style='color:purple;'>Tweet</b>!"})
            t2=len(x2)
        else:
            for j in range(len(x2)/10):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/yellow-dot.png',
                'lat': x2[j][1],#37.4419,
                'lng': x2[j][0],#-122.1419,
                'infobox': "Hello I am a new <b style='color:yellow;'>Tweet</b>!"})
            for k in range(len(x2)/10,len(x2)):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/purple-dot.png',
                'lat': x2[k][1],#37.4419,
                'lng': x2[k][0],#-122.1419,
                'infobox': "Hello I am a <b style='color:purple;'>Tweet</b>!"})
        #print temp
        fullmap2 = Map(
            identifier="fullmap2",
            varname="fullmap2",
            style=(
                "height:85%;"
                "width:100%;"
                "top:15%;"
                "left:0;"
                "position:absolute;"
                "z-index:200;"
            ),
            lat=30,
            lng=-90,
            markers=temp,zoom="2")
        return render_template('example_fullmap2.html', fullmap2=fullmap2,response2=response2) 
    except Exception as e:
        application.run(debug=True, use_reloader=True)

@application.route('/birthday',methods=["GET"])

def fullmap3():
    global t3
    try:
        x3=[]
        url3='http://54.163.11.20:9200/twitter/_search?sort=@timestamp:desc&q=birthday&size=1000'
        response3=urllib.urlopen(url3)
        
        data3 = json.loads(response3.read())
        for i in range(len(data3['hits']['hits'])):
            if(data3['hits']['hits'][i]['_source']['geo']!=None):
                x3.append( data3['hits']['hits'][i]['_source']['coordinates']['coordinates'])
            else:
                x3.append(data3['hits']['hits'][i]['_source']['place']['bounding_box']['coordinates'][0][0])
        temp=[]
        if t3<len(x3):
            for j in range(len(x3)-t3):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/red-dot.png',
                'lat': x3[j][1],#37.4419,
                'lng': x3[j][0],#-122.1419,
                'infobox': "Hello I am a new <b style='color:red;'>Tweet</b>!"})
            for k in range(len(x3)-t3,len(x3)):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': x3[k][1],#37.4419,
                'lng': x3[k][0],#-122.1419,
                'infobox': "Hello I am a <b style='color:blue;'>Tweet</b>!"})
            t3=len(x3)
        else:
            for j in range(len(x3)/10):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/red-dot.png',
                'lat': x3[j][1],#37.4419,
                'lng': x3[j][0],#-122.1419,
                'infobox': "Hello I am a new <b style='color:red;'>Tweet</b>!"})
            for k in range(len(x3)/10,len(x3)):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': x3[k][1],#37.4419,
                'lng': x3[k][0],#-122.1419,
                'infobox': "Hello I am a <b style='color:blue;'>Tweet</b>!"})
        #print temp
        fullmap3 = Map(
            identifier="fullmap3",
            varname="fullmap3",
            style=(
                "height:85%;"
                "width:100%;"
                "top:15%;"
                "left:0;"
                "position:absolute;"
                "z-index:200;"
            ),
            lat=30,
            lng=-90,
            markers=temp,zoom="2")
        return render_template('example_fullmap3.html', fullmap3=fullmap3,response3=response3) 
    except Exception as e:
        application.run(debug=True, use_reloader=True)

@application.route('/world',methods=["GET"])

def fullmap4():
    global t4
    try:
        x4=[]
        url4='http://54.163.11.20:9200/twitter/_search?sort=@timestamp:desc&q=world&size=1000'
        response4=urllib.urlopen(url4)
        
        data4 = json.loads(response4.read())
        for i in range(len(data4['hits']['hits'])):
            if(data4['hits']['hits'][i]['_source']['geo']!=None):
                x4.append( data4['hits']['hits'][i]['_source']['coordinates']['coordinates'])
            else:
                x4.append(data4['hits']['hits'][i]['_source']['place']['bounding_box']['coordinates'][0][0])
        temp=[]
        if t4<len(x4):
            for j in range(len(x4)-t4):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/orange-dot.png',
                'lat': x4[j][1],#37.4419,
                'lng': x4[j][0],#-122.1419,
                'infobox': "Hello I am a new <b style='color:orange;'>Tweet</b>!"})
            for k in range(len(x4)-t4,len(x4)):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/purple-dot.png',
                'lat': x4[k][1],#37.4419,
                'lng': x4[k][0],#-122.1419,
                'infobox': "Hello I am a <b style='color:purple;'>Tweet</b>!"})
            t4=len(x4)
        else:
            for j in range(len(x4)/10):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/orange-dot.png',
                'lat': x4[j][1],#37.4419,
                'lng': x4[j][0],#-122.1419,
                'infobox': "Hello I am a new <b style='color:orange;'>Tweet</b>!"})
            for k in range(len(x4)/10,len(x4)):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/purple-dot.png',
                'lat': x4[k][1],#37.4419,
                'lng': x4[k][0],#-122.1419,
                'infobox': "Hello I am a <b style='color:purple;'>Tweet</b>!"})
        #print temp
        fullmap4 = Map(
            identifier="fullmap4",
            varname="fullmap4",
            style=(
                "height:85%;"
                "width:100%;"
                "top:15%;"
                "left:0;"
                "position:absolute;"
                "z-index:200;"
            ),
            lat=30,
            lng=-90,
            markers=temp,zoom="2")
        return render_template('example_fullmap4.html', fullmap4=fullmap4,response4=response4)  
    except Exception as e:
        application.run(debug=True, use_reloader=True)

@application.route('/game',methods=["GET"])

def fullmap5():
    global t5
    try:
        x5=[]
        url5='http://54.163.11.20:9200/twitter/_search?sort=@timestamp:desc&q=game&size=1000'
        response5=urllib.urlopen(url5)
        
        data5 = json.loads(response5.read())
        for i in range(len(data5['hits']['hits'])):
            if(data5['hits']['hits'][i]['_source']['geo']!=None):
                x5.append( data5['hits']['hits'][i]['_source']['coordinates']['coordinates'])
            else:
                x5.append(data5['hits']['hits'][i]['_source']['place']['bounding_box']['coordinates'][0][0])
        temp=[]
        if t5<len(x5):
            for j in range(len(x5)-t5):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/yellow-dot.png',
                'lat': x5[j][1],#37.4419,
                'lng': x5[j][0],#-122.1419,
                'infobox': "Hello I am a new <b style='color:yellow;'>Tweet</b>!"})
            for k in range(len(x5)-t5,len(x5)):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': x5[k][1],#37.4419,
                'lng': x5[k][0],#-122.1419,
                'infobox': "Hello I am a <b style='color:green;'>Tweet</b>!"})
            t5=len(x5)
        else:
            for j in range(len(x5)/10):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/yellow-dot.png',
                'lat': x5[j][1],#37.4419,
                'lng': x5[j][0],#-122.1419,
                'infobox': "Hello I am a new <b style='color:yellow;'>Tweet</b>!"})
            for k in range(len(x5)/10,len(x5)):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': x5[k][1],#37.4419,
                'lng': x5[k][0],#-122.1419,
                'infobox': "Hello I am a <b style='color:green;'>Tweet</b>!"})
        #print temp
        fullmap5 = Map(
            identifier="fullmap5",
            varname="fullmap5",
            style=(
                "height:85%;"
                "width:100%;"
                "top:15%;"
                "left:0;"
                "position:absolute;"
                "z-index:200;"
            ),
            lat=30,
            lng=-90,
            markers=temp,zoom="2")
        return render_template('example_fullmap5.html', fullmap5=fullmap5,response5=response5)  
    except Exception as e:
        application.run(debug=True, use_reloader=True)

@application.route('/love',methods=["GET"])

def fullmap6():
    global t6
    try:
        x6=[]
        url6='http://54.163.11.20:9200/twitter/_search?sort=@timestamp:desc&q=love&size=1000'
        response6=urllib.urlopen(url6)
        
        data6 = json.loads(response6.read())
        for i in range(len(data6['hits']['hits'])):
            if(data6['hits']['hits'][i]['_source']['geo']!=None):
                x6.append( data6['hits']['hits'][i]['_source']['coordinates']['coordinates'])
            else:
                x6.append(data6['hits']['hits'][i]['_source']['place']['bounding_box']['coordinates'][0][0])
        temp=[]
        if t6<len(x6):
            for j in range(len(x6)-t6):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/red-dot.png',
                'lat': x6[j][1],#37.4419,
                'lng': x6[j][0],#-122.1419,
                'infobox': "Hello I am a new <b style='color:red;'>Tweet</b>!"})
            for k in range(len(x6)-t6,len(x6)):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/purple-dot.png',
                'lat': x6[k][1],#37.4419,
                'lng': x6[k][0],#-122.1419,
                'infobox': "Hello I am a <b style='color:purple;'>Tweet</b>!"})
            t6=len(x6)
        else:
            for j in range(len(x6)/10):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/red-dot.png',
                'lat': x6[j][1],#37.4419,
                'lng': x6[j][0],#-122.1419,
                'infobox': "Hello I am a new <b style='color:red;'>Tweet</b>!"})
            for k in range(len(x6)/10,len(x6)):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/purple-dot.png',
                'lat': x6[k][1],#37.4419,
                'lng': x6[k][0],#-122.1419,
                'infobox': "Hello I am a <b style='color:purple;'>Tweet</b>!"})
        #print temp
        fullmap6 = Map(
            identifier="fullmap6",
            varname="fullmap6",
            style=(
                "height:85%;"
                "width:100%;"
                "top:15%;"
                "left:0;"
                "position:absolute;"
                "z-index:200;"
            ),
            lat=30,
            lng=-90,
            markers=temp,zoom="2")
        return render_template('example_fullmap6.html', fullmap6=fullmap6,response6=response6)  
    except Exception as e:
        application.run(debug=True, use_reloader=True)

@application.route('/football',methods=["GET"])

def fullmap7():
    global t7
    try:
        x7=[]
        url7='http://54.163.11.20:9200/twitter/_search?sort=@timestamp:desc&q=football&size=1000'
        response7=urllib.urlopen(url7)
        
        data7 = json.loads(response7.read())
        for i in range(len(data7['hits']['hits'])):
            if(data7['hits']['hits'][i]['_source']['geo']!=None):
                x7.append( data7['hits']['hits'][i]['_source']['coordinates']['coordinates'])
            else:
                x7.append(data7['hits']['hits'][i]['_source']['place']['bounding_box']['coordinates'][0][0])
        temp=[]
        if t7<len(x7):
            for j in range(len(x7)-t7):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/orange-dot.png',
                'lat': x7[j][1],#37.4419,
                'lng': x7[j][0],#-122.1419,
                'infobox': "Hello I am a new <b style='color:orange;'>Tweet</b>!"})
            for k in range(len(x7)-t7,len(x7)):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': x7[k][1],#37.4419,
                'lng': x7[k][0],#-122.1419,
                'infobox': "Hello I am a <b style='color:green;'>Tweet</b>!"})
            t7=len(x7)
        else:
            for j in range(len(x7)/10):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/orange-dot.png',
                'lat': x7[j][1],#37.4419,
                'lng': x7[j][0],#-122.1419,
                'infobox': "Hello I am a new <b style='color:orange;'>Tweet</b>!"})
            for k in range(len(x7)/10,len(x7)):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': x7[k][1],#37.4419,
                'lng': x7[k][0],#-122.1419,
                'infobox': "Hello I am a <b style='color:green;'>Tweet</b>!"})
        #print temp
        fullmap7 = Map(
            identifier="fullmap7",
            varname="fullmap7",
            style=(
                "height:85%;"
                "width:100%;"
                "top:15%;"
                "left:0;"
                "position:absolute;"
                "z-index:200;"
            ),
            lat=30,
            lng=-90,
            markers=temp,zoom="2")
        return render_template('example_fullmap7.html', fullmap7=fullmap7,response7=response7)  
    except Exception as e:
        application.run(debug=True, use_reloader=True)

@application.route('/university',methods=["GET"])

def fullmap8():
    global t8
    try:
        x8=[]
        url8='http://54.163.11.20:9200/twitter/_search?sort=@timestamp:desc&q=university&size=1000'
        response8=urllib.urlopen(url8)
        
        data8 = json.loads(response8.read())
        for i in range(len(data8['hits']['hits'])):
            if(data8['hits']['hits'][i]['_source']['geo']!=None):
                x8.append( data8['hits']['hits'][i]['_source']['coordinates']['coordinates'])
            else:
                x8.append(data8['hits']['hits'][i]['_source']['place']['bounding_box']['coordinates'][0][0])
        temp=[]
        if t8<len(x8):
            for j in range(len(x8)-t8):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/yellow-dot.png',
                'lat': x8[j][1],#37.4419,
                'lng': x8[j][0],#-122.1419,
                'infobox': "Hello I am a new <b style='color:yellow;'>Tweet</b>!"})
            for k in range(len(x8)-t8,len(x8)):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': x8[k][1],#37.4419,
                'lng': x8[k][0],#-122.1419,
                'infobox': "Hello I am a <b style='color:blue;'>Tweet</b>!"})
            t8=len(x8)
        else:
            for j in range(len(x8)/10):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/yellow-dot.png',
                'lat': x8[j][1],#37.4419,
                'lng': x8[j][0],#-122.1419,
                'infobox': "Hello I am a new <b style='color:yellow;'>Tweet</b>!"})
            for k in range(len(x8)/10,len(x8)):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': x8[k][1],#37.4419,
                'lng': x8[k][0],#-122.1419,
                'infobox': "Hello I am a <b style='color:blue;'>Tweet</b>!"})
        #print temp
        fullmap8 = Map(
            identifier="fullmap8",
            varname="fullmap8",
            style=(
                "height:85%;"
                "width:100%;"
                "top:15%;"
                "left:0;"
                "position:absolute;"
                "z-index:200;"
            ),
            lat=30,
            lng=-90,
            markers=temp,zoom="2")
        return render_template('example_fullmap8.html', fullmap8=fullmap8,response8=response8)  
    except Exception as e:
        application.run(debug=True, use_reloader=True)


@application.route('/swift',methods=["GET"])

def fullmap9():
    global t9
    try:
        x9=[]
        url9='http://54.163.11.20:9200/twitter/_search?sort=@timestamp:desc&q=taylor&size=1000'
        response9=urllib.urlopen(url9)
        
        data9 = json.loads(response9.read())
        for i in range(len(data9['hits']['hits'])):
            if(data9['hits']['hits'][i]['_source']['geo']!=None):
                x9.append( data9['hits']['hits'][i]['_source']['coordinates']['coordinates'])
            else:
                x9.append(data9['hits']['hits'][i]['_source']['place']['bounding_box']['coordinates'][0][0])
        temp=[]
        if t9<len(x9):
            for j in range(len(x9)-t9):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/red-dot.png',
                'lat': x9[j][1],#37.4419,
                'lng': x9[j][0],#-122.1419,
                'infobox': "Hello I am a new <b style='color:red;'>Tweet</b>!"})
            for k in range(len(x9)-t9,len(x9)):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': x9[k][1],#37.4419,
                'lng': x9[k][0],#-122.1419,
                'infobox': "Hello I am a <b style='color:green;'>Tweet</b>!"})
            t9=len(x9)
        else:
            for j in range(len(x9)/10):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/red-dot.png',
                'lat': x9[j][1],#37.4419,
                'lng': x9[j][0],#-122.1419,
                'infobox': "Hello I am a new <b style='color:red;'>Tweet</b>!"})
            for k in range(len(x9)/10,len(x9)):
                temp.append({'icon': '//maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': x9[k][1],#37.4419,
                'lng': x9[k][0],#-122.1419,
                'infobox': "Hello I am a <b style='color:green;'>Tweet</b>!"})
        #print temp
        fullmap9 = Map(
            identifier="fullmap9",
            varname="fullmap9",
            style=(
                "height:85%;"
                "width:100%;"
                "top:15%;"
                "left:0;"
                "position:absolute;"
                "z-index:200;"
            ),
            lat=30,
            lng=-90,
            markers=temp,zoom="2")
        return render_template('example_fullmap9.html', fullmap9=fullmap9,response9=response9)
    except Exception as e:
        application.run(debug=True, use_reloader=True)

if __name__ == "__main__":
    application.run(debug=True, use_reloader=True)

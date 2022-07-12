import json
import numpy as np
uniques_values = []
uniques_values_en = []
uniques_values_cn = []
uniques_values_pl = []
uniques_values_ru = []
uniques_values_el = []
uniques_values_fr = []
uniques_values_es = []
uniques_values_pt = []
uniques_values_zh = []
mydict = json.load(open("C:\\Users\\HP\\Desktop\\Downloads\\event-detection\\event-detection-master\\event-detection-daniel\\Corpus_Daniel\\multilingual_relevant.json","r",encoding='utf-8'))
mydict2 = json.load(open("C:\\Users\HP\\Desktop\\Downloads\\event-detection\\event-detection-master\\event-detection-daniel\\Corpus_Daniel\\multilingual_relevant.json_lang=all_minStr=1_ratio=0.8.results","r",encoding='utf-8'))

diseases1 = json.load(open("C:\\Users\\HP\\Desktop\\Downloads\\event-detection\\event-detection-master\\event-detection-daniel\\resources\\diseases_all.json","r",encoding='utf-8'))
locations1 = json.load(open("C:\\Users\\HP\\Desktop\\Downloads\\event-detection\\event-detection-master\\event-detection-daniel\\resources\\locations_all.json","r",encoding='utf-8'))
diseases = {k.lower(): diseases1[k].lower() for k,v in diseases1.items()}
locations = {k.lower(): locations1[k].lower() for k,v in locations1.items()}
for key, d in mydict.items():
   
  
    
   if mydict[key]["annotations"][0][0]!="N" and mydict[key]["annotations"][0][1]!="N":
    
    T=tuple((mydict[key]["annotations"][0][0],mydict[key]["annotations"][0][1],mydict[key]["language"]))
   #print(T)
    
   
    if T not in uniques_values:
      uniques_values.append(T)
    
   
       
        # print(uniques_values[i]) 
      #print(diseases[mydict[key]["annotations"][0][0]])
            
    if mydict[key]["language"]=="en":
     if T not in uniques_values_en:
      uniques_values_en.append(T)
    if mydict[key]["language"]=="cn":
     if T not in uniques_values_cn:
      uniques_values_cn.append(T)
    if mydict[key]["language"]=="pl":
     if T not in uniques_values_pl:
      uniques_values_pl.append(T)
    if mydict[key]["language"]=="ru":
     if T not in uniques_values_ru:
      uniques_values_ru.append(T)
    if mydict[key]["language"]=="el":
     if T not in uniques_values_el:
      uniques_values_el.append(T)
    if mydict[key]["language"]=="fr":
     if T not in uniques_values_fr:
      uniques_values_fr.append(T)
    if mydict[key]["language"]=="es":
     if T not in uniques_values_es:
      uniques_values_es.append(T)
    if mydict[key]["language"]=="pt":
     if T not in uniques_values_pt:
      uniques_values_pt.append(T)
    if mydict[key]["language"]=="zh":
     if T not in uniques_values_zh:
      uniques_values_zh.append(T)
   
print("Unique events in English",len(uniques_values_en),"\n Unique events in Chinese cn",len(uniques_values_cn),"\n Unique events in Chinese zh",len(uniques_values_zh),"\n Unique events in Polish",len(uniques_values_pl)," \n Unique events in Russian",len(uniques_values_ru),"\n Unique events in Greek",len(uniques_values_el),"\n Unique events in French",len(uniques_values_fr),"\n Unique events in Espagnol",len(uniques_values_es),"\n Unique events in Portiguese",len(uniques_values_pt))
   
shared_items = {k: (mydict2[k]["annotations"],mydict2[k]["language"])
                    for k in mydict.keys() if k in mydict2.keys() and (mydict[k]["annotations"][0][0]).lower() == (mydict2[k]["annotations"][0][0]).lower() and (mydict[k]["annotations"][0][1]).lower() == (mydict2[k]["annotations"][0][1]).lower()  and mydict[k]["annotations"][0][0] != "N" and mydict[k]["annotations"][0][1] != "N"} #and mydict[k]["language"] == "en"}
#print (len(shared_items))
detected=[]
detected_en = []
detected_cn = []
detected_pl = []
detected_ru = []
detected_el = []
detected_fr = []
detected_es = []
detected_pt = []
detected_zh = []
for key, d in shared_items.items():
  if shared_items[key][0] not in detected:  
     detected.append(shared_items[key][0])

  if shared_items[key] not in detected_en and d[1]=="en":  
     detected_en.append(shared_items[key])
  if shared_items[key] not in detected_en and d[1]=="cn":
     detected_cn.append(shared_items[key])
  if shared_items[key] not in detected_pl and d[1]=="pl":
     detected_pl.append(shared_items[key])
  if shared_items[key] not in detected_pl and d[1]=="ru":
     detected_ru.append(shared_items[key])
  if shared_items[key] not in detected_el and d[1]=="el":
     detected_el.append(shared_items[key])
  if shared_items[key] not in detected_fr and d[1]=="fr":
     detected_fr.append(shared_items[key])
  if shared_items[key] not in detected_es and d[1]=="es":
     detected_es.append(shared_items[key])
  if shared_items[key] not in detected_pt and d[1]=="pt":
     detected_pt.append(shared_items[key])
  if shared_items[key] not in detected_zh and d[1]=="zh":
     detected_zh.append(shared_items[key])
print("Events detected in English",len(detected_en),"\n Events detected in Chinese cn",len(detected_cn),"\n Events detected in Chinese zh",len(detected_zh),"\n Events detected in Polish",len(detected_pl),"\n Events detected in Russian",len(detected_ru),"\n Events detected in Greek",len(detected_el),"\n Events detected in French",len(detected_fr),"\n Events detected in Spanich",len(detected_es),"\n Events detected in Portuguese",len(detected_pt))

#liste = list(t[0] for t in uniques_values )
#print(uniques_values)
cum=[]
cum1=[]
for t in uniques_values:
   if t[0].lower() in diseases.keys() and t[1].lower() in locations.keys() :
     A=tuple((diseases[t[0].lower()],locations[t[1].lower()]))
     #print(A)
     cum.append(A)
#print(cum)
s=0
for i in cum:
   if cum.count(i)>1 and i not in cum1:
      cum1.append(i)
      s=s+cum.count(i)
      #print(i,cum.count(i), len(cum), len(cum1),s,len(uniques_values) )
print ("unique event in cumulated files",len(uniques_values)-(s-len(cum1)))
   
cum_det=[]
cum1_det=[]
for t in detected:
   if (t[0][0]).lower() in diseases.keys() and (t[0][1]).lower() in locations.keys() :
     A=tuple((diseases[(t[0][0]).lower()],locations[(t[0][1]).lower()]))
     #print(A)
     cum_det.append(A)
s=0
for i in cum_det:
   if cum_det.count(i)>1 and i not in cum1_det:
      cum1_det.append(i)
      s=s+cum_det.count(i)
      #print(i,cum_det.count(i), len(cum_det), len(cum1_det),s,len(detected))
print ("detected event in cumulated files",len(detected)-(s-len(cum1_det)))


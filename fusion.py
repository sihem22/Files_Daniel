import json

mydict = json.load(open("C:\\Users\\HP\\Desktop\\Downloads\\event-detection\\event-detection-master\\event-detection-daniel\\Corpus_Daniel\\recent.json","r",encoding='utf-8'))

data = json.load(open("C:\\Users\\HP\\Desktop\\Downloads\\event-detection\\event-detection-master\\event-detection-daniel\\corpus_daniel0\\daniel.json","r",encoding='utf-8'))
data.update(mydict)
json.dump(data, open("C:\\Users\\HP\\Desktop\\Downloads\\event-detection\\event-detection-master\\event-detection-daniel\\Corpus_Daniel\\Fusion.json", "w"))

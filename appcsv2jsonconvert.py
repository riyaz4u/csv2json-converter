from flask import Flask ,request,jsonify
app=Flask(__name__)
@app.route('/',methods=['GET'])
@app.route('/openfile',methods=['POST','GET'])


def openfile():
    file = askopenfilename(defaultextension=".csv",
                           filetypes=[("csv files", "*.csv")])
    if file == "":
        file = None
    else:
        fileEntry.delete(0, END)
        fileEntry.config(fg="blue")
        fileEntry.insert(0, file)
    return "openfile"
import csv
import json
def uploadcsv():
 with open('data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    fieldnames = reader.fieldnames
    output = []
    for row in reader:
        j = {}
        for i, _ in enumerate(fieldnames):
            j[fieldnames[i]] = row[fieldnames[i]]
        output.append(j)
    return "uploadcsv"
def makejson():
 with open('data.json','w') as jsonfile:
        jsonfile.write(json.dumps(output))
        save2json = output
        return "makejson"


if __name__ == "__main__":
    app.debug = True
    app.run()
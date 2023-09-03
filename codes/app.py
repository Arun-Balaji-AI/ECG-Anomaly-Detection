from flask import Flask, render_template, request,jsonify
import ECG_Anomaly_Detection

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    answer = None
    if request.method=="POST":
        data=request.form
        values = data['ecg_data']
        if len(values)==0:
            answer="Enter the required values to get the Report"
        else:
            data_list = values.split(',')
            my_int_list = []
            for i in data_list:
                my_int_list.append(float(i))
            if len(my_int_list)<187:
                answer="The Data is Insufficient"
            elif len(my_int_list)>187:
                answer="The data is More"
            else:
                answer = ECG_Anomaly_Detection.model_ecg(my_int_list)
    return render_template('home.html',answer=answer)

if __name__=="__main__":
    app.run(debug=True)
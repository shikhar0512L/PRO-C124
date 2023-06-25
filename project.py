from flask import Flask, jsonify, request

app=Flask(__name__)

tasks=[
    {
        'id':1,
        'Name':'Shikhar',
        'Contact':'I love coding',
        'done':False
    },
    {
        'id':2,
        'Name':'Shrutika mam',
        'Contact':'I am a coding teacher',
        'done':False
    }

]

@app.route('/add-data',methods=['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'please provide the data'
        },400)
    contact={
        'id':tasks[-1]['id']+1,
        'Name':request.json['Name'],
        'Contact':request.json.get('Contact',""),
        'done':False
        
    }
    tasks.append(contact)
    return jsonify({
        'status':'succsses',
        'message':'task add successfully'
    })

@app.route('/get-data')
def get_task():
    return jsonify({
        'data':tasks
    })

if __name__=='__main__':
    app.run()
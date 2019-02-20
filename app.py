from flask_api import FlaskAPI


app = FlaskAPI(__name__)

employees = [
             {
                'id':1,
                'name':'Yasser',
                'age':23,
                'job':'Python Developer'
             },
              {
                 'id':2,
                 'name':'omar',
                 'age':25,
                 'job':'Java Developer'
              },
               {
                  'id':3,
                  'name':'Ahmed',
                  'age':27,
                  'job':'C++ Developer'
               }]

@app.route('/api/v1/employees',methods=['GET'])
def get():
    return {'employees':employees}

if __name__ == "__main__":
    app.run(debug=True)

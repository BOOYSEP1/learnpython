from flask import Flask, render_template, jsonify

app = Flask("__name__")
JOBS = [
{
    'id':1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
},
{
    'id':2,
    'title': 'Data Sceintist',
    'location': 'Mumbai, India',
    'salary': 'Rs. 15,00,000'
},
{
    'id':3,
    'title': 'Frontend Engineer',
    'location': 'Remote'
    
},
    
{
    'id':4,
    'title': 'Backend Engineer',
    'location': 'New-York, USA',
    'salary': '$12,00,000'
}
]

@app.route("/")
def Learn_Python():
    return render_template ('home.html', jobs=JOBS,
                          company_name='Learn Python')


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

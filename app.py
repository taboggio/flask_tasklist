from flask import Flask, render_template, request, redirect

app = Flask (__name__)

tareas = []

@app.route('/')
def home():
    return render_template('index.html', tareas=tareas)

@app.route('/agregar', methods=['GET', 'POST']) #Uno es donde visitamos la pag y otro donde enviamos la info
def agregar():
    if request.method == 'GET':
        return render_template('agregar.html')
    else:
        tarea = request.form.get('tarea')
        tareas.append(tarea) #A la LISTA se le agregan TAREAS
        return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)

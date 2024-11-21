from flask import Blueprint, render_template, request, redirect, url_for
from myapp.task import operationsCRUD

taskRoute = Blueprint('task', __name__, url_prefix='/task') #conjunto de rutas definidas que van a estar dentro del modulo

task_list = ['tasks 1', 'tasks 2', 'tasks 3']

#Creacion de rutas en el modulo rutas, todas estas son rutas que definimos 
@taskRoute.route('/') #aqui muestra todo el contenido de la tabla "task"
def index():
    #print(operationsCRUD.getById(2).name)
    #print(operationsCRUD.getAll()[1].name)
    #print(operationsCRUD.delete(1))
    print(operationsCRUD.pagination().items)
    return render_template('dashboard/task/index.html', tasks=task_list)

@taskRoute.route('/<int:id>') # solo muestra la que tenga este id previo seleccionado
def show(id:int):
    return 'Show ' +str(id)

@taskRoute.route('/delete/<int:id>')
def delete(id:int):
    #aqui podemos meter la funcion de borrar y posterior la pagina
    if id != None and id != "":
        del task_list[id]
        return redirect(url_for('task.index'))

@taskRoute.route('/create', methods=('GET','POST'))#crear pagina que tenga un formulario, usar get y post sirven para enviar info, get para info x y post para info sensible
def create():
    task = request.form.get('task')
    if task != None and task != "":
        task_list.append(task)
        return redirect(url_for('task.index'))
    return render_template('dashboard/task/create.html')

@taskRoute.route('/update/<int:id>', methods=['GET','POST']) 
def update(id:int):
    task = request.form.get('task')
    if task != None and task != "":
        task_list[id] = task
        return redirect(url_for('task.index'))
        
    return render_template('dashboard/task/update.html')
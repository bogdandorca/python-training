from flask import Flask, jsonify, request, make_response

from modules.tasks_controller import TasksController

app = Flask(__name__)

taskController = TasksController()


@app.route('/task', methods=['GET', 'POST'])
def task_index():
    if request.method == 'GET':
        return taskController.get_tasks()
    elif request.method == 'POST':
        return taskController.create_task()


@app.route('/task/<int:task_id>', methods=['GET', 'PUT', 'DELETE'])
def task_with_id_index(task_id):
    if request.method == 'GET':
        return taskController.get_task(task_id)
    elif request.method == 'DELETE':
        return taskController.delete_task(task_id)
    elif request.method == 'PUT':
        req_data = request.get_json()
        if req_data and req_data['name']:
            return taskController.update_task(task_id, req_data['name'])
        else:
            return make_response(jsonify({
                'message': 'You should send the ID for the task you want to upgrade'
            }), 400)


if __name__ == '__main__':
    app.run(debug=True)

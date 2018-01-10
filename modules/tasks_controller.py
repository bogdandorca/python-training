from flask import jsonify, request, make_response


class TasksController:
    def __init__(self):
        self.tasks = [
            {
                'id': 0,
                'name': 'doThis'
            },
            {
                'id': 1,
                'name': 'do That'
            },
            {
                'id': 2,
                'name': 'Do the other thing'
            }
        ]

    def get_tasks(self):
        return jsonify(self.tasks)

    def create_task(self):
        req_data = request.get_json()
        if req_data and req_data['name']:
            new_task = {
                'id': len(self.tasks),
                'name': req_data['name']
            }
            self.tasks.append(new_task)
            return jsonify(new_task)

        return make_response(jsonify({
            'message': 'You should assign a name for your new task'
        }), 404)

    def get_task(self, task_id):
        task = [task for task in self.tasks if task['id'] == task_id]
        if task:
            return jsonify(task[0])
        return make_response(jsonify({'message': 'The task was not found'}), 404)

    def update_task(self, task_id, task_name):
        selected_task_index = self.get_task_index_by_id(task_id)
        if selected_task_index > 0:
            self.tasks[selected_task_index]['name'] = task_name
            return jsonify(self.tasks)
        return make_response(jsonify({
            'message': 'The selected task does not exist'
        }), 404)

    def delete_task(self, task_id):
        selected_task_index = self.get_task_index_by_id(task_id)
        if selected_task_index >= 0:
            del self.tasks[selected_task_index]
            return jsonify(self.tasks)
        return make_response(jsonify({
            'message': 'The element does not exist'
        }), 400)

    def get_task_index_by_id(self, task_id):
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                return i
        return -1

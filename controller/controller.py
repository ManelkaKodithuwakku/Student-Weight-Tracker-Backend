from flask import request

from service.service import Service


class Controller:
    def __init__(self,app):
        app.add_url_rule('/api/add/userDetail', 'add data', self.add_student_details, methods=['POST'])
        app.add_url_rule('/api/get/userDetail', 'get data', self.get_student_details, methods=['Get'])
        self.service = Service()

    def add_student_details(self):
        data = request.json
        print(data)
        name = data.get('name')
        weight = data.get('weight')

        return self.service.save_data_to_db(name, weight)

    def get_student_details(self):
        return self.service.get_student_data()




from database.mongo_manger import MongoDBManager


class Service:
    def __init__(self):
        self.student_details_db = MongoDBManager("StudentDetail")

    def save_data_to_db(self, name, weight):
        data = {
            "student_name" : name,
            "student_weight" : weight
        }

        try:
            self.student_details_db.save_to_db(data)
        except Exception as e:
            print("Failed to insert student details")
            return {
                'success' : False
            }
        return {
            'success': True
        }

    def get_student_data(self):
        try:
            cursor = self.student_details_db.get_document({})
            document_list = list(cursor)
            for doc in document_list:
                doc['_id'] = str(doc['_id'])
            return document_list
        except Exception as e:
            print(e)
            print("Failed to fetch student details")


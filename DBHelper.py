class ScoresCollectionHelper:
    def __init__(self, mongocollection):
        self.mongocollection = mongocollection


    def appendScore(self, subjectname, date, score):
        self.mongocollection.find_one_and_update\
            ({"name": subjectname}, {"$push":{"scores": [date, score]}})

    def getAllSubjects(self):
        cursor = self.mongocollection.find({})
        subjects =[]
        for document in cursor:
            subjects.append(document.get("name"))

        return subjects
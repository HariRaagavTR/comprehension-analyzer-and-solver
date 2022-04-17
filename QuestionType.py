'''
TBDL: Train a model that predicts question type.
'''

class QuestionType:
    def __init__(self):
        self.boolenTypes = ['am', 'is', 'are', 'was', 'were', 'can',
                            'could', 'may', 'might', 'shall', 'should',
                            'will', 'would', 'must', 'ought', 'do',
                            'does', 'did', 'have', 'has', 'had']
        self.numericalTypes = ['how much more', 'how much lesser', 'how many', 'how much',
                               'what were the',]

    def __isBoolean(self, question):
        if question.split()[0].lower() in self.boolenTypes:
            return True
        return False
    
    def __isNumerical(self, question):
        v1 = question.split()
        q1 = v1[0].lower() + v1[1] + v1[2]
        q2 = v1[0].lower() + v1[1]
        if q1 in self.numericalTypes or q2 in self.numericalTypes:
            return True
        return False

    def predict(self, question):
        if self.__isBoolean(question):
            return 'boolean'
        elif self.__isNumerical(question):
            return 'numerical'
        else:
            return 'textual'

'''
TBDL: Train a model that predicts question type.
'''

class QuestionType:
    def __init__(self):
        self.boolenTypes = ['am', 'is', 'are', 'was', 'were', 'can',
                            'could', 'may', 'might', 'shall', 'should',
                            'will', 'would', 'must', 'ought', 'do',
                            'does', 'did', 'have', 'has', 'had']
        # Add more here!

    def __isBoolean(self, question):
        if question.split()[0].lower() in self.boolenTypes:
            return True
        return False
    
    def __isNumerical(self, question):
        # Add logic here
        return False

    def predict(self, question):
        if self.__isBoolean(question):
            return 'boolean'
        elif self.__isNumerical(question):
            return 'numerical'
        else:
            return 'textual'

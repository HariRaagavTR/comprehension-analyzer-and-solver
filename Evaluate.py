import csv
from QuestionType import QuestionType
from BooleanQAModel import BooleanQAModel
from TextualQAModel import BERTModel
from NumericalQAModel import NumericalQAModel

questionType = QuestionType()
booleanQAModel = BooleanQAModel('./resources/models/BooleanQAModel.pth')
textualModel = BERTModel()
numberModel = NumericalQAModel()

class Evaluate:
    def __init__(self, datasetPath):
        file = open(datasetPath, encoding="utf8")
        self.csvreader = csv.reader(file)
        self.X = []
        self.y = []
        self.y_pred = []

    def __setCommonWords(self, y_pred, y):
        y_dict = {}
        y_pred_dict = {}
        self.lenPrediction = 0
        self.lenActual = 0
        self.commonWords = 0

        for word in y_pred.split():
            if word not in y_pred_dict:
                y_pred_dict[word] = 0
            y_pred_dict[word] += 1
            self.lenPrediction += 1

        for word in y.split():
            if word not in y_dict:
                y_dict[word] = 0
            y_dict[word] += 1
            self.lenActual += 1
        
        for word in y_pred_dict:
            if word in y_dict:
                self.commonWords += min(y_pred_dict[word], y_dict[word])

    # Number of tokens that are shared between the correct answer and the prediction.
    def __getTruePositive(self):
        return self.commonWords

    # Number of tokens that are in the prediction but not in the correct answer.
    def __getFalsePositive(self):
        return self.lenPrediction - self.commonWords

    # Number of tokens that are in the correct answer but not in the prediction.
    def __getFalseNegative(self):
        return self.lenActual - self.commonWords

    def __getConfusionMatrix(self, Y_pred, Y):
        confusionMatrix = [0, 0, 0] # TP, FP, FN
        for y_pred, y in zip(Y_pred, Y):
            self.__setCommonWords(y_pred, y)
            confusionMatrix[0] += self.__getTruePositive()
            confusionMatrix[1] += self.__getFalsePositive()
            confusionMatrix[2] += self.__getFalseNegative()
        return confusionMatrix
        
    def f1_score(self, Y_pred, Y):
        truePositive, falsePositive, falseNegative = self.__getConfusionMatrix(Y_pred, Y)
        precision = truePositive / (truePositive + falsePositive)
        recall = truePositive / (truePositive + falseNegative)
        return (2 * precision * recall) / (precision + recall)
    
    def __generateParameters(self):
        headers = next(self.csvreader)
        print(headers)
        for row in self.csvreader:
            context, question = row[0], row[1]
            qType = questionType.predict(question)
            if qType == 'boolean':
                answer = booleanQAModel.predict(context, question)
            elif qType == 'numerical':
                answer = numberModel.predict(context, question)
                if not answer:
                    answer = textualModel.predict(context, question)
            else:
                answer = textualModel.predict(context, question)
            self.y.append(str(row[2]))
            self.y_pred.append(str(answer))

    def evaluate(self):
        self.__generateParameters()
        print('INFO: Evauation Complete. F1 Score:', self.f1_score(self.y_pred, self.y))

Evaluate('./resources/datasets/test_dataset.csv').evaluate()
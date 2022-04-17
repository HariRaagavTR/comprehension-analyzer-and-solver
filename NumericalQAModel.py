from allennlp_models import pretrained

class NumericalQAModel:
    def __init__(self):
        self.model = pretrained.load_predictor("rc-naqanet")
    
    def predict(self, context, question):
        answer = self.model.predict(question, context)
        finalAnswer = answer["answer"]["value"]
        return finalAnswer
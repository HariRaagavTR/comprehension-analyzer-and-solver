import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

class BooleanQAModel:
    def __init__(self, modelPath):
        self.__initDevice()
        self.__initTokenizer()
        self.__initModel(modelPath)

    def __initDevice(self):
        if torch.cuda.is_available():
            print('INFO: Device is set to CUDA.')
        else:
            print('INFO: CUDA is not available. Device is set to CPU.')
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    def __initTokenizer(self):
        self.tokenizer = AutoTokenizer.from_pretrained('roberta-base')

    def __initModel(self, modelPath):
        self.model = AutoModelForSequenceClassification.from_pretrained("roberta-base")
        self.model.to(self.device)
        self.model.load_state_dict(torch.load(modelPath, map_location=self.device))
    
    def getProbailities(self, context, question):
        sequence = self.tokenizer.encode_plus(question, context, return_tensors="pt")['input_ids'].to(self.device)
        probabilities = torch.softmax(self.model(sequence)[0], dim=1).detach().cpu().tolist()[0]
        p_yes = round(probabilities[1], 2)
        p_no = round(probabilities[0], 2)
        return (p_yes, p_no)

    def predict(self, context, question):
        p_yes, p_no = self.getProbailities(context, question)
        return "Yes" if p_yes > p_no else "No"

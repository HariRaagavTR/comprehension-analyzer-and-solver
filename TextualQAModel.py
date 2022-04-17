import torch
from transformers import BertForQuestionAnswering
from transformers import BertTokenizer

class BERTModel:
  def __init__(self):
    self.model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
    self.tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

  def geto(self,context,question):
    input_ids = self.tokenizer.encode(question, context)
    tokens = self.tokenizer.convert_ids_to_tokens(input_ids)
    sep_index = input_ids.index(self.tokenizer.sep_token_id)
    num_seg_a = sep_index + 1
    num_seg_b = len(input_ids) - num_seg_a
    segment_ids = [0]*num_seg_a + [1]*num_seg_b
    assert len(segment_ids) == len(input_ids)
    outputs = self.model(torch.tensor([input_ids]), token_type_ids=torch.tensor([segment_ids]), return_dict=True) 
    return outputs,tokens

  def predict(self, context, question):
    outputs,tokens = self.geto(context,question)
    start_scores = outputs.start_logits
    end_scores = outputs.end_logits
    answer_start = torch.argmax(start_scores)
    answer_end = torch.argmax(end_scores)
    answer = tokens[answer_start]
    for i in range(answer_start + 1, answer_end + 1):
        if tokens[i][0:2] == '##':
            answer += tokens[i][2:]
        else:
            answer += ' ' + tokens[i]
    return answer
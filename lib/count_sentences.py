#!/usr/bin/env python3

class MyString:
    def __init__(self,value = ''):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, stringVal):
        if isinstance(stringVal, str):
            self._value = stringVal
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith('.')
    
    def is_question(self):
        return self._value.endswith('?')
    
    def is_exclamation(self):
        return self._value.endswith('!')
    
    def count_sentences(self):
        value = self.value
        for punc in ['!','?']:
            value = value.replace(punc, '.')
        
        sentences = [s for s in value.split('.') if s]
        
        return len(sentences)
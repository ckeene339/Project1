from tkinter import *
import csv
from Project1_gui import *
#from typing import 

class SAVE:
    total = 0
    john = 0
    brett = 0
    kate = 0
    
    def test_data(self, votes, candidate, candidate_text, label_info):
        self.votes = votes
        self.candidate = candidate
        self.candidate_text = candidate_text
        
        
        
        '''
        if statement below tests to make sure a candidate was selected.
        '''
        if self.candidate > 0:
            '''
            if statement below tests to make sure a valid input was given in the entry widget. This means
            no empty space and numbers only.
            '''
            if self.votes.strip() and self.votes.isdigit() and int(self.votes) > 0:
                return True
            else:
                label_info.config(text='Invalid input:\nplease enter a valid\nnumber of votes')
                return False
        else:
            label_info.config(text='Please select a candidate')
            return False
        
        
        
    def save_data(self, candidate, candidate_text, label_info, radio_answer, entry_widget):
        self.radio_answer = radio_answer
        self.radio_answer.set(0)
        entry_widget.delete(0, END)
        
        
        
        '''
        Code below adds votes to specified candidate and the total
        '''
        SAVE.total += int(self.votes)
        if candidate_text[candidate] == 'John':
            SAVE.john += int(self.votes)
        elif candidate_text[candidate] == 'Brett':
            SAVE.brett += int(self.votes)
        elif candidate_text[candidate] == 'Kate':
            SAVE.kate += int(self.votes)
        
        
        
        '''
        Code below prints updated data to the window. This updates all candidate's votes and total votes.
        '''
        label_info.config(text=f'{self.candidate_text[candidate]} recieved {self.votes} vote(s)!\n'
                               f'_________________________\n'
                               f'{self.candidate_text[1]} - {SAVE.john}\n'
                               f'{self.candidate_text[2]} - {SAVE.brett}\n'
                               f'{self.candidate_text[3]} - {SAVE.kate}\n'
                               f'Total - {SAVE.total}\n'
                               f'_________________________\n'
                               f'csv file updated!')
        
        
        
        '''
        Code Below Saves data to csv file. File is created in the same folder as the project.
        '''
        with open('data.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Candidates', 'Votes'])
            writer.writerow([self.candidate_text[1], SAVE.john])
            writer.writerow([self.candidate_text[2], SAVE.brett])
            writer.writerow([self.candidate_text[3], SAVE.kate])
            writer.writerow(['Total', SAVE.total])
            csv_file.close()

import pandas as pd
import random 

def load_questions():
	# Load data from csv file
	data = pd.read_csv('code_questions.csv')
	G1,G2,G3,G5 = data['G1'].tolist(), data['G2'].tolist(), data['G3'].tolist(), data['G5'].tolist()
	G4 = [ elm for elm in data['G4 '].tolist() if type(elm) is str]
	random.shuffle(G1)
	random.shuffle(G2)
	random.shuffle(G3)
	random.shuffle(G4)
	random.shuffle(G5)
	return (G1,G2,G3,G4,G5)

def save_contest(contest,day,idx):
	with open("contest/"+'Day_'+str(day)+"_Contest_"+str(idx)+'.txt', 'w') as f:
		for item in contest:
			f.write("%s\n" % item)

def contest_builder():
	# Load questions
	G1,G2,G3,G4,G5 = load_questions()
	# Build contest
	st=0
	contests = []
	for i in range(0,20):
		contest = []
		contest.extend(G1[st:st+2])
		contest.extend(G2[st:st+2])
		contest.extend(G4[i:i+1])
		contest.extend(G3[st:st+2])
		contest.extend(G5[st:st+2])
		random.shuffle(contest)
		save_contest(contest[:3],i+1,i%3 + 1)
		save_contest(contest[3:6],i+1,(i+1)%3 + 1)
		save_contest(contest[6:],i+1,(i+2)%3 + 1)
		st+=2

if __name__ == '__main__':
	random.seed(43)
	contest_builder()
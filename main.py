# echo build up
# écrire que Benjamin était absent dans le compte rendu

from flask import Flask, request
import pandas as pd

app = Flask(__name__)

class Transaction:
    def __init__(self, P1, P2, t, s):
        self.P1 = P1
        self.P2 = P2
        self.t = t
        self.s = s

class Personne:
    def __init__(self, solde, transactions):
        self.solde = solde
        self.transactions = transactions

transactions = []
personnes = []

personnesData = pd.read_csv('personnes.csv', names= ['solde', 'transactions'],engine='python', sep=';')
personnes = list(personnesData.to_dict('index').values())

transactionsData = pd.read_csv('transactions.csv', names= ['P1', 'P2', 's', 't'],engine='python', sep=';')
transactions = list(transactionsData.to_dict('index').values())

@app.route('/')
def listeTransactions():
    transactions.sort(key=lambda tr: tr['t'])
    return transactions

@app.route('/personnes')
def listPersonnes():
    return personnes

@app.route('/personnes/transactions/<personne>')
def transactionsPersonne(personne):
    if request.method == 'GET':
        return personnes[int(personne)]['transactions']

@app.route('/personnes/solde/<personne>')
def soldePersonne(personne):
    if request.method == 'GET':
        return personnes[int(personne)]['solde']


@app.route('/addPersonne', methods=["POST"])
def addPersonne():
    if request.method == 'POST':
        solde = request.form.get('solde')
        personnes.append({'solde': solde, 'transactions': []})
        return listPersonnes()

@app.route('/addTransaction', methods=["POST"])
def addTransaction():
    if request.method == 'POST':
        P1_index = int(request.form.get('P1'))
        P2_index = int(request.form.get('P2'))
        P1_data = personnes[P1_index]
        P2_data = personnes[P2_index]
        P1 = Personne(P1_data['solde'], P1_data['transactions'])
        P2 = Personne(P2_data['solde'], P2_data['transactions'])
        t = int(request.form.get('t'))
        s = int(request.form.get('s'))
        s1 = int(P1.solde)
        s2 = int(P2.solde)
        s1 -= s
        s2 += s
        P1.solde = str(s1)
        P2.solde = str(s2)
        tr = {'P1': P1_index, 'P2': P2_index, 't': t, 's': s}
        transactions.append(tr)
        P1.transactions.append(tr)
        P2.transactions.append(tr)
        personnes[P1_index] = {'solde': P1.solde, 'transactions': P2.transactions}
        personnes[P2_index] = {'solde': P2.solde, 'transactions': P2.transactions}
        return listeTransactions()
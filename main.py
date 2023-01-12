from flask import Flask, request
import json
from collections import namedtuple

app = Flask(__name__)

class Transaction:
    def __init__(self, P1, P2, t, s):
        self.P1 = P1
        self.P2 = P2
        self.t = t
        self.s = s
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class Personne:
    def __init__(self, solde, transactions):
        self.solde = solde
        self.transactions = transactions
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def JSONDecoder(dict):
    return namedtuple('X', dict.keys())(*dict.values())

transactions = []
personnes = []

@app.route('/')
def listPersonnes():
    return personnes
def listeTransactions() :
    return transactions

@app.route('/addPersonne', methods=["POST"])
def addPersonne():
    if request.method == 'POST':
        solde = request.form.get('solde')
        personnes.append(Personne(solde, []).toJSON())
        return listPersonnes()

@app.route('/addTransaction', methods=["POST"])
def addTransaction():
    if request.method == 'POST':
        P1_index = int(request.form.get('P1'))
        P2_index = int(request.form.get('P2'))
        P1_data = personnes[P1_index]
        P2_data = personnes[P2_index]
        P1_decoded = json.loads(P1_data, object_hook=JSONDecoder)
        P2_decoded = json.loads(P2_data, object_hook=JSONDecoder)
        P1 = Personne(P1_decoded.solde, P1_decoded.transactions)
        P2 = Personne(P2_decoded.solde, P2_decoded.transactions)
        t = int(request.form.get('t'))
        s = int(request.form.get('s'))
        s1 = int(P1.solde)
        s2 = int(P2.solde)
        s1 -= s
        s2 += s
        P1.solde = str(s1)
        P2.solde = str(s2)
        transaction = Transaction(P1, P2, t, s)
        transactions.append(transaction.toJSON())
        P1.transactions.append(transaction.toJSON())
        P2.transactions.append(transaction.toJSON())
        personnes[P1_index] = P1.toJSON()
        personnes[P2_index] = P2.toJSON()
        return listeTransactions()
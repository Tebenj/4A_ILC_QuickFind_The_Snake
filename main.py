# echo build up
# écrire que Benjamin était absent dans le compte rendu

from flask import Flask, request
import pandas as pd
import hashlib

app = Flask(__name__)

class Transaction:
    def __init__(self, P1, P2, t, s):
        self.P1 = P1
        self.P2 = P2
        self.t = t
        self.s = s
        self.h = hashTransaction(P1, P2, t, s)

class Personne:
    def __init__(self, solde, transactions):
        self.solde = solde
        self.transactions = transactions

transactions = [] # liste des transactions
personnes = [] # liste des personnes

#
# importation des données des fichiers csv
#
personnesData = pd.read_csv('personnes.csv', names= ['solde', 'transactions'],engine='python', sep=';')
personnes = list(personnesData.to_dict('index').values())

transactionsData = pd.read_csv('transactions.csv', names= ['P1', 'P2', 's', 't', 'h'],engine='python', sep=';')
transactions = list(transactionsData.to_dict('index').values())

@app.route('/')
def listeTransactions(): # retourne la liste des transactions
    transactions.sort(key=lambda tr: tr['t'])
    return transactions

@app.route('/personnes')
def listPersonnes(): # retourne la liste des personnes
    return personnes

@app.route('/personnes/transactions/<personne>')
def transactionsPersonne(personne): # retourne la liste des transactions d'une personne
    if request.method == 'GET':
        return personnes[int(personne)]['transactions']

@app.route('/personnes/solde/<personne>')
def soldePersonne(personne): # retourne le solde d'une personne
    if request.method == 'GET':
        return personnes[int(personne)]['solde']


@app.route('/addPersonne', methods=["POST"])
def addPersonne(): # ajoute une nouvelle personne
    if request.method == 'POST':
        solde = request.form.get('solde')
        personnes.append({'solde': solde, 'transactions': []})
        return listPersonnes()

@app.route('/addTransaction', methods=["POST"])
def addTransaction(): # ajoute une nouvelle transaction
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
        transaction = Transaction(P1_index, P2_index, t, s)
        tr = {'P1': transaction.P1, 'P2': transaction.P2, 't': transaction.t, 's': transaction.s, 'h': transaction.h}
        transactions.append(tr)
        P1.transactions.append(tr)
        P2.transactions.append(tr)
        personnes[P1_index] = {'solde': P1.solde, 'transactions': P2.transactions}
        personnes[P2_index] = {'solde': P2.solde, 'transactions': P2.transactions}
        return listeTransactions()

@app.route('/verification', methods=["GET"])
def verification():
    if request.method == 'GET':
        verify = True
        for transaction in transactions:
            if(hashTransaction(transaction['P1'], transaction['P2'], transaction['t'], transaction['s']) != transaction['h']):
                verify = False
        return "Données vérifiées" if verify else "Données corrompues"


def hashTransaction(P1, P2, t, s):
    sha256 = hashlib.sha256()
    sha256.update((str(P1) + str(P2) + str(t) + str(s)).encode())
    return sha256.hexdigest()
# given a list of transactions, consolidate amount for same payee and payer

transactions = [
  {"payee": "BoA", "amount": 132, "payer": "Chase"},
  {"payee": "BoA", "amount": 827, "payer": "Chase"},
  {"payee": "Wells Fargo", "amount": 751, "payer": "BoA"},
  {"payee": "BoA", "amount": 585, "payer": "Chase"},
  {"payee": "Chase", "amount": 877, "payer": "Wells Fargo"},
  {"payee": "Wells Fargo", "amount": 157, "payer": "Chase"},
  {"payee": "Wells Fargo", "amount": 904, "payer": "Chase"},
  {"payee": "Chase", "amount": 548, "payer": "Wells Fargo"},
  {"payee": "Chase", "amount": 976, "payer": "BoA"},
  {"payee": "BoA", "amount": 872, "payer": "Wells Fargo"},
  {"payee": "Wells Fargo", "amount": 571, "payer": "Chase"}
]



def findElemAm(transactions, element):
	if transactions == []:
		return False
	for t in transactions:
		if element['payee'] is t['payee'] and element['payer'] is t['payer']:
			#print(t['amount'])
			#return True
			return t['amount'], transactions.index(t)
		return False

def consolidate(transactions):
	tr = []
	for t in transactions:
		e = findElemAm(tr, t)
		if not e:
			tr.append(t)
		else:
			t['amount'] += e[0]
			tr[e[1]] = t
	return tr

print(consolidate(transactions))




import bitcoinrpc
# from bitcoinrpc.exceptions import InsufficientFunds
# from bitcoinrpc import connection
# from bitcoinrpc.proxy import AuthServiceProxy
import json
import decimal
import pprint
import time
# from blockchain import *
import blockchain
from blockchain import createwallet

pp = pprint.PrettyPrinter(depth=30)
conn = bitcoinrpc.connect_to_local()
print conn
# bitcoin = bitcoinrpc.connection.BitcoinConnection('cjn', 'cjn','localhost', '8332',False)
# print bitcoin
# print conn.getinfo()


#information coming from the bitcoin server
info = conn.getinfo()
balance =  info.balance
print info
# print bala`nce
# print info
print "Blocks: %i" % info.blocks
print "Connections: %i" % info.connections
print "Difficulty: %f" % info.difficulty
# print info.txid

# print conn.generate('101')
print "Your balance is %f" % (conn.getbalance(),)
# print conn.getbalance()

#to get address,initialize with a new account named "cjn"
addr = conn.getnewaddress("testnet")
addr1 = conn.getnewaddress("cjn")
print addr
print addr1

# print conn.getgenerate()
# conn.setgenerate(True,None)
# print conn.getgenerate()

# txid = conn.sendtoaddress(addr, 20.0)
# print txid
# account = conn.getaccount(addr)
# account1 = conn.getaccount(addr1)
# print account
# print account1

# balance = conn.getbalance(account,minconf=None)
# print "Your balance is %s" % (conn.getbalance(account,None),)
# balance1 = conn.getbalance('cjn',minconf=None)
# print balance
# print balance1
# balance = json.dumps({'x': decimal.Decimal(50000)}, default=decimal_default)
balance = json.dumps({'amount':str(500)})
b = json.loads(balance)
balance1 = json.dumps({'amount':str(100)})
b1 = json.loads(balance1)
# print b['amount']
# for key,value in b.item():
# 	print key,value
# print balance[0]+balance[1]
print "Your balance is %f" % (conn.getbalance('testnet',None),)
print "Your balance is %f" % (conn.getbalance('cjn',None),)
try:
	txid = conn.sendtoaddress(addr,str(b['amount']),None,None)
# 	txid1 = conn.sendtoaddress(addr1,str(b['amount']),None,None)
# 	print txid,txid1 
	# txid = conn.sendfrom('testnet',addr1,str(b['amount']),1,None,None)
	print txid
except InsufficientFunds,e:
	print "Insufficient amount"

info = conn.gettransaction(txid)
# print "blockhash = ",info.blockhash
# print pp.pprint(info)
# print pp.pprint(conn.gettransaction(txid1))
# print pp.pprint(conn.listunspent())
# print conn.getbalance("cjn",None)


# print len((conn.listtransactions('testnet')))
# print conn.listtransactions('cjn')

# print conn.getreceivedbyaccount("cjn",1)
# index = conn.getblocknumber()
# print index
# pp = pprint.PrettyPrinter(depth=6)
# print pp.pprint(conn.getblock(conn.getblockhash(index)))



time.sleep(2)
print "Your balance is %f" % (conn.getbalance('testnet',None),)
print "Your balance is %f" % (conn.getbalance('cjn',None),)

# time.sleep(2)

# print str(a914 dda4 521a 9cd9 9e92 323a e476 2467)
# print conn.get_address(addr,None)
# user = '22a3b8a4-f127-47a5-8d29-8f40f91ddded'
# password = 'cjnngrabcd9571'
# wallet = createwallet.CreateWalletResponse(user,"1Qe54fESA8CVZJs4y5feXP9sXSToNwSfH","teramatixisnone")
# print wallet.create_wallet()
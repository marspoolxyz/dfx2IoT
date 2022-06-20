from ic.canister import Canister
from ic.client import Client
from ic.identity import Identity
from ic.agent import Agent
from ic.candid import Types

iden = Identity()
client = Client()
agent = Agent(iden, client)
# read governance candid from file
governance_did = open("carrots.did").read()
# create a governance canister instance
governance = Canister(agent=agent, canister_id="2qrsq-uiaaa-aaaai-aa3zq-cai", candid=governance_did)
# call canister method with instance
res = governance.holders()
print(res)
res = governance.totalsupply()
print(res)
res = governance.wallet_balance()
print(res)

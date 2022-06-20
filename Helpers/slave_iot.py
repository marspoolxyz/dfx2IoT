from ic.canister import Canister
from ic.client import Client
from ic.identity import Identity
from ic.agent import Agent
from ic.candid import Types

iden = Identity()
client = Client()
agent = Agent(iden, client)
# read governance candid from file
governance_did = open("slave_iot.did").read()
# create a governance canister instance
governance = Canister(agent=agent, canister_id="e6v3r-ciaaa-aaaaf-qaebq-cai", candid=governance_did)
# call canister method with instance
res = governance.sizeData()
print(res)
 
from ic.client import Client
from ic.identity import Identity
from ic.agent import Agent
from ic.candid import encode, decode, Types
import time

# Identity and Client are dependencies of Agent
iden = Identity()
client = Client()
agent = Agent(iden, client)


params = [
	{'type': Types.Nat, 'value': 463}
]
#result = agent.update_raw("uca7j-eqaaa-aaaah-qbiha-cai", "addIoTData", encode(params))

i=0
while i <= 10:
    name = agent.query_raw("uca7j-eqaaa-aaaah-qbiha-cai", "getLatestIoTData", encode([]))
    print(name)
    time.sleep(10)

from demo import app as application

def initialize_database():
    import json
    import requests
    from time import sleep
    from pymongo import MongoClient

    print('********************************************************************************')
    print('*** INITIALIZING DATABASE                                                    ***')
    print('********************************************************************************')

    # give mongo a second to start up
    sleep(1)

    # initialize the "demo" database
    client = MongoClient('mongo')
    db = client.demo
    coll = db.launches

    res = requests.get('https://api.spacexdata.com/v1/launches')
    launches = json.loads(res.content)
    count = 0
    for launch in launches:
        count += 1
        print('importing {}/{}'.format(count, len(launches)))
        coll.insert_one(launch)

if __name__ == '__main__':
    application.run()
else:
    initialize_database()

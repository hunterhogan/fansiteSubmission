import hashlib
import json
import os
import re
import subprocess
import sys
import time
import traceback

from fansiteSimulator import FansiteSimulator
import fansiteConfig
import fansiteHttp
import testRepo
import tyrantData

def askToUpdateDataFiles():
    input_var = raw_input("Would you like to download the latest Tyrant xml files (y/n)? ")
    if(input_var == "Y" or input_var == "y"):
        tyrantData.updateDataFiles()

def startSession(token, version, check = None):
    if(check is None):
        check = tyrantData.getCheck()
    json_data = fansiteHttp.getSession(token, version, check)

    # TODO this is a bit of a hack
    if("errorCode" in json_data and json_data["errorCode"] >= 101 and json_data["errorCode"] <= 110):
        askToUpdateDataFiles()

    if(not "sessId" in json_data):
        return None

    return json_data["sessId"]

def loadSimulators():
    simulators = {}
    
    # add extra simulators here. don't forget to import any files you need
    from simulatorIteratedecks import SimulatorIteratedecks
    simulators[SimulatorIteratedecks.name] = SimulatorIteratedecks
    from simulatorTyrantOptimizer import SimulatorTyrantOptimizer
    simulators[SimulatorTyrantOptimizer.name] = SimulatorTyrantOptimizer

    return simulators

def simDeck(simulator, deck, args):
    deckId = deck["deckId"]

    start = time.time()
    results = simulator.simulate(deck, args)
    if results is None:
        return
    timeTaken = int(time.time() - start)
    results["time"] = max(1, timeTaken)

    return results

def fansiteTest():
    args = fansiteConfig.getArgs()
    print args
    simulators = loadSimulators()

    if hasattr(args, 'proxy'):
        import urllib2
        urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler({'http': args.proxy})))
    simulator = None
    if(args.simulator in simulators):
        simulator = simulators[args.simulator]()
    else:
        print("Unsupported simulator: " + args.simulator)
        return

    version = simulator.getVersion()

    if(args.test):
        args.numSims = 1000
        args.runForever = 0

    print("Using %s version %s with %s sims per deck" % (simulator.name, version, args.numSims))

    if(not args.test):
        print("Requesting session id...")
        sessId = startSession(args.token, version)
        if(sessId is None):
            print("No session started.")
            return
        print(" ... started session with id " + sessId)

    while 1:
        print("Getting decks...")
        if(not args.test):
            json_data = fansiteHttp.getDecks(sessId, args.limit)
            decks = json_data["decks"]
        else:
            decks = testRepo.loadTests(False)
        print(" ... " + str(len(decks)) + " decks retrieved")

        for deck in decks:
            deckId = deck["deckId"]
            try:
                results = simDeck(simulator, deck, args)
                if results is None:
                    print(" ... no result, skipped")
                if not args.test:
                    if(results.has_key("ard")):
                        print(" ... result: %(wins)s/%(total)s, ard=%(ard)s, time=%(time)s" % results)
                    else:
                        print(" ... result: %(wins)s/%(total)s, time=%(time)s" % results)
                    json_data = fansiteHttp.submitSimulation(deckId, sessId, results["total"], results["wins"], results["time"], results.get("ard"))
                else:
                    testRepo.testKey(deck, "winrate", 100 * int(results["wins"]) / int(results["total"] if(results.get("wins") is not None) else None))
                    testRepo.testKey(deck, "drawrate", 100 * int(results["draws"]) / int(results["total"] if(results.get("draws") is not None) else None))
                    testRepo.testKey(deck, "lossrate", 100 * int(results["losses"]) / int(results["total"] if(results.get("losses") is not None) else None))
                    testRepo.testKey(deck, "ard", float(results["ard"]) if(results.get("ard") is not None) else None, 5)
            except NotImplementedError, e:
                print("Error: Not Implemented: %s" % e)
            except Exception, e:
                traceback.print_exc()
        if not args.runForever:
            break

if __name__ == '__main__':
    fansiteTest()

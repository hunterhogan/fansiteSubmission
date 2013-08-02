#!/usr/bin/env python

import re
import subprocess

from fansiteSimulator import FansiteSimulator

class SimulatorTyrantOptimizer(FansiteSimulator):
    name = "Tyrant Optimizer"
    executable = "tyrant_optimize.exe"
    results_regex = re.compile(r"(?:kill|win)%: \S+ \((\d+) / (\d+)\)"
        r"\s+stall%: \S+ \((\d+) / \d+\)"
        r"\s+loss%: \S+ \((\d+) / \d+\)"
        r"(?:\s+(ard|achievement%): \S+ \((\d+) / \d+\))?")
    results_keys = ["wins", "total", "draws", "losses", "ard"]

    def loadVersion(self):
        commandArgs = [self.executable, "-version"]
        result = subprocess.check_output(commandArgs)
        return result.split()[2]

    def processResults(self, results):
        match = self.results_regex.search(results)
        if not match:
            print("ERROR: Cannot find results from output {{{\n", results, "}}}")
            return None
        wins, total, stalls, losses, points_type, points = match.groups()
        results = dict()
        if points_type == "achievement%":
            results["wins"] = points
        elif points_type == "ard":
            results["wins"] = int(wins) + int(stalls)
        else:
            results["wins"] = wins
        results["total"] = total
        results["draws"] = stalls
        results["losses"] = losses
        if points_type == "ard":
            results["ard"] = float(points) / int(total)
        return results

    def addAchievement(self, commandArgs, achievementId, missionId):
        commandArgs.append("Mission #%s" % missionId)
        commandArgs.extend(["-A", str(achievementId)])

    def addAttackingDeck(self, commandArgs, attackingDeck, attackingDeckCards):
        commandArgs.append(attackingDeck)

    def addBattlegroundId(self, commandArgs, battlegroundId):
        commandArgs.extend(["-e", str(battlegroundId)])

    def addCustom(self, commandArgs, custom):
        commandArgs.append(custom)

    def addDefendingExactOrdered(self, commandArgs):
        commandArgs.append("defender:exact-ordered")

    def addDefendingOrdered(self, commandArgs):
        commandArgs.append("defender:ordered")

    def addDelayed(self, commandArgs):
        commandArgs.append("tournament")

    def addExactOrdered(self, commandArgs):
        commandArgs.append("exact-ordered")

    def addExtraArgs(self, commandArgs, args):
        commandArgs.extend(["-t", str(getattr(args, "numThreads", 1))])
        commandArgs.extend(["sim", str(args.numSims)])

    def addMission(self, commandArgs, missionId):
        commandArgs.append("Mission #%s" % missionId)

    def addOrdered(self, commandArgs):
        commandArgs.append("ordered")

    def addQuest(self, commandArgs, questId):
        commandArgs.append("Quest #%s" % questId)

    def addRaid(self, commandArgs, raidId):
        commandArgs.append("Raid #%s" % raidId)

    def addSurge(self, commandArgs):
        commandArgs.append("-s")


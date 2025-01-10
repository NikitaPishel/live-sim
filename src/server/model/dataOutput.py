import json
import math

from configuration import config
import neuronCmd as nrnCmd
import genome as gnm

def makeGeneReadable(gene):
    readableGene = []

    cmdNameTable = {
        nrnCmd.constantOn: "ConstantOn",
        nrnCmd.tanhList: "tanhList",
        nrnCmd.reLU: "reLU",
        nrnCmd.invert: "invert",
        nrnCmd.outMoveNorth: "moveNorth",
        nrnCmd.outMoveSouth: "moveSouth",
        nrnCmd.outMoveEast: "moveEast",
        nrnCmd.outMoveWest: "moveWest"
        }

    for i in range(len(gene)):
        nrnjoints = []
        for ref in gene[i].joints:
            nrnjoints.append(gene.index(ref))

        nrnData = {}
        nrnData["id"] = i
        nrnData["command"] = cmdNameTable[gene[i].cmd]
        nrnData["joints"] = nrnjoints

        readableGene.append(nrnData)

    return readableGene

def saveGenome(dataOut, itrNum, itrData):
    if itrNum % config.savePassedGenomes == 0:
        dataOut[itrNum]['succGenomes'] = []

        for agentIndex in range(len(itrData)):
            slctGene = gnm.getGenome(itrData[agentIndex].gene, [])
            slctGene.pop(0)

            rdblGene = makeGeneReadable(slctGene)

            dataOut[itrNum]['succGenomes'].append(rdblGene)

def savePassedNum(dataOut, itrNum, itrData):
    if itrNum % config.savePassedNumber == 0:

        slctAmount = len(itrData)
        srv = math.floor((slctAmount / config.maxAgents) * 1000) / 10

        dataOut[itrNum]['passedAmount'] = slctAmount
        dataOut[itrNum]['survivability'] = f'{srv}%'

def saveRunData(data, filename):
    with open(f'{config.outputPath}/{filename}', 'w') as path:
        json.dump(data, path)
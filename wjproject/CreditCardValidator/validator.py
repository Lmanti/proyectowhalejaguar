def isAmericanExpress(cardNumber: str) -> bool:
    if len(cardNumber) != 15: return False
    elif cardNumber[:2] not in ["34", "37"]: return False
    return True

def isChinaTUnion(cardNumber: str) -> bool:
    if len(cardNumber) != 19: return False
    elif cardNumber[:2] != '31': return False
    return True

def isChinaUnionPay(cardNumber: str) -> bool:
    if len(cardNumber) not in range(16, 20): return False
    elif cardNumber[:2] != '62': return False
    return True

def isDinersClubInternational(cardNumber: str) -> bool:
    if len(cardNumber) not in range(14, 20): return False
    elif cardNumber[:2] != '36': return False
    return True

def isDinersClubUC(cardNumber: str) -> bool:
    if len(cardNumber) != 16: return False
    elif cardNumber[:2] != '54': return False
    return True

def isDiscoverCard(cardNumber: str) -> bool:
    if len(cardNumber) not in range(16, 20): return False
    elif int(cardNumber[:3]) not in range(644, 650) and int(cardNumber[:6]) not in range(622126, 622926) and cardNumber[:4] != '6011' and cardNumber[:2] != '65': return False
    return True

def isUkrCard(cardNumber: str) -> bool:
    if len(cardNumber) not in range(16, 20): return False
    elif int(cardNumber[:8]) not in range(60400100, 60420100): return False
    return True

def isRuPay(cardNumber: str) -> bool:
    if len(cardNumber) != 16: return False
    elif cardNumber[:2] != '60' and cardNumber[:4] != '6521' and cardNumber[:4] != '6522': return False
    return True

def isInterPayment(cardNumber: str) -> bool:
    if len(cardNumber) not in range(16, 20): return False
    elif cardNumber[:3] != '636': return False
    return True

def isInstaPayment(cardNumber: str) -> bool:
    if len(cardNumber) != 16: return False
    elif int(cardNumber[:3]) not in range(637, 640): return False
    return True

def isJCB(cardNumber: str) -> bool:
    if len(cardNumber) not in range(16, 20): return False
    elif int(cardNumber[:4]) not in range(3528, 3590): return False
    return True

def isMaestroUK(cardNumber: str) -> bool:
    if len(cardNumber) not in range(12, 20): return False
    elif cardNumber[:4] != '6759' and cardNumber[:6] != '676770' and cardNumber[:6] != '676774': return False
    return True

def isMaestro(cardNumber: str) -> bool:
    if len(cardNumber) not in range(12, 20): return False
    elif cardNumber[:4] not in ["5018", "5020", "5038", "5893", "6304", "6759", "6761", "6762", "6763"]: return False
    return True

def isDankort(cardNumber: str) -> bool:
    if len(cardNumber) != 16: return False
    elif cardNumber[:4] not in ["5019", "4571"]: return False
    return True

def isMIR(cardNumber: str) -> bool:
    if len(cardNumber) not in range(16, 20): return False
    elif int(cardNumber[:4]) not in range(2200, 2205): return False
    return True

def isNPSPridnestrovie(cardNumber: str) -> bool:
    if len(cardNumber) != 16: return False
    elif int(cardNumber[:7]) not in range(6054740, 6054745): return False
    return True

def isMastercard(cardNumber: str) -> bool:
    if len(cardNumber) != 16: return False
    elif int(cardNumber[:4]) not in range(2221, 2721) and int(cardNumber[:2]) not in range(51, 56): return False
    return True

def isTroy(cardNumber: str) -> bool:
    if len(cardNumber) != 16: return False
    elif cardNumber[:2] != '65' and cardNumber[:4] != '9792': return False
    return True

def isVisaElectron(cardNumber: str) -> bool:
    if len(cardNumber) != 16: return False
    elif cardNumber[:4] not in ["4026", "4508", "4844", "4913", "4917"] and cardNumber[:6] != '417500': return False
    return True

def isVisa(cardNumber: str) -> bool:
    if len(cardNumber) != 13 and len(cardNumber) != 16: return False
    elif cardNumber[0] != '4': return False
    return True
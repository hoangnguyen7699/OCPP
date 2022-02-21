from ocpp.v201.enums import AuthorizationStatusType


def isValidIdToken(id_token):

    #Read file and check if id in is that file
    with open('validtoken.txt') as f:
        lines = []
        for line in f:
            lines.append(line)
    print(lines)
    if id_token["id_token"] not in lines:
        return False
    return True

def isAllowedEVDriver(id_token, cpID):
    return True

def isAllowedIdToken_Any_EVSE(id_token, cpID):
    return True

def getAllowedListEVSE(id_token, cpID):
    return []

def isEnoughCredit(id_token):
    return True

def isExprired(id_token):
    return False

def isBlocked(id_token):
    return False

def isConcurrent(id_token):
    return False

def isAllowedAtThisTime(id_token):
    return False

def isAllowedAtThisLocation(id_token):
    return False



def getIdTokenInfo(id_token, cpID):
    if isValidIdToken(id_token):
        if not isEnoughCredit(id_token): return AuthorizationStatusType.no_credit

        elif not isAllowedEVDriver(id_token, cpID): return AuthorizationStatusType.not_allowed_type_evse
        else:
            if isAllowedAtThisTime(id_token): return AuthorizationStatusType.not_at_this_time
            elif isAllowedAtThisTime(id_token): return AuthorizationStatusType.not_at_this_location
        
        return AuthorizationStatusType.accepted
    elif isBlocked(id_token): return AuthorizationStatusType.blocked
    elif isExprired(id_token): return AuthorizationStatusType.expired
    elif isConcurrent(id_token): return AuthorizationStatusType.concurrent_tx
    elif not isValidIdToken(id_token) : return AuthorizationStatusType.invalid
    else:
        return AuthorizationStatusType.unknown


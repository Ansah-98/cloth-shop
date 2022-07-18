
def isValid(s):
        x = 1
        bol = "true"
        while x < len(s):
            if s[x] == ")" and x%2!=1:
                if s[x - 1] != "(" :
                    return "false"
                else :
                    bol = bol
            elif s[x] == "}":
                if s[x - 1] != "{":
                    return "false"
                else: 
                    bol
            else:
                if s[x-1] !="[":
                    return "false"
                else:
                    bol = bol
            x = x + 2 
        return bol
        
print(isValid('()('))
#Script To Sequintially Name Default Ghidra Functions
#@author: Euclid 
#@category: FunctionNaming

import ghidra.program.model.symbol.SourceType as SourceType

FirstDigit = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]  
BeforeTwenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]  
AfterTwenty = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]  
def ConvertToWords(num):  
    if num == 0:  
        return "Zero"  
    elif num< 0:  
        return "Minus " + ConvertToWords(abs(num))  
    elif num< 10:  
        return FirstDigit[num]  
    elif num< 20:  
        return BeforeTwenty[num - 10]  
    elif num< 100:  
        return AfterTwenty[num // 10] + ("" + ConvertToWords(num % 10) if num % 10 != 0 else "")  
    elif num< 1000:  
        return FirstDigit[num // 100] + "Hundred" + ("And" + ConvertToWords(num % 100) if num % 100 != 0 else "")  
    elif num< 1000000:  
        return ConvertToWords(num // 1000) + "Thousand" + ("" + ConvertToWords(num % 1000) if num % 1000 != 0 else "")  
    elif num< 1000000000:  
        return ConvertToWords(num // 1000000) + "Million" + ("" + ConvertToWords(num % 1000000) if num % 1000000 != 0 else "")  
    else:  
        return str(num) 

# Get the current program's function names
function = getFirstFunction()
name = ""
nameint = 2
while function is not None:
    name = "Func"+ConvertToWords(nameint)
    
    if "NoneType" in str(type(function)):    
        break
    
    if function == None:
        break
    
    symbol = function.getSymbol()
    if function.getName() != "entry" and function.getName() != "main":
        if symbol.getSource() == SourceType.DEFAULT:
            print function.getName() + " --> " + name
            symbol.setName(name, SourceType.USER_DEFINED)
            
        nameint = nameint + 1
        name = str(nameint)
    else:
        print function.getName()
    function = getFunctionAfter(function)
 

# Output to a popup window
popup("Renamed default function names")

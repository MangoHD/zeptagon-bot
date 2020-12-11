def multiply(arg5 : int, arg6 : int, n1 : int = '0', n2 : int = '0'):
    if n1 == '0':
        return (f"{arg5} × {arg6} = {arg5 * arg6}")
    if n2 == '0':
        return (f"{arg5} × {arg6} × {n1} = {arg5 * arg6 * n1}")
    return (f"{arg5} × {arg6} × {n1} × {n2} = {arg5 * arg6 * n1 * n2}")

def divide(arg7 : int, arg8 : int, n1 : int = '0', n2 : int = '0'):
    if n1 == '0':
        return (f"{arg7} ÷ {arg8} = {arg7 / arg8}")
    if n2 == '0':
        return (f"{arg7} ÷ {arg8} ÷ {n1} = {arg7 / arg8 / n1}")
    return (f"{arg7} ÷ {arg8} ÷ {n1} ÷ {n2} = {arg7 / arg8 / n1 / n2}")

def add(arg9 : int, arg10 : int, n1 : int = '0', n2 : int = '0'):
    if n1 == '0':
        return (f"{arg9} + {arg10} = {arg9 + arg10}")
    if n2 == '0':
        return (f"{arg9} + {arg10} + {n1} = {arg9 + arg10 + n1}")
    return (f"{arg9} + {arg10} + {n1} + {n2} = {arg9 + arg10 + n1 + n2}")

def substract(arg11 : int, arg12 : int, n1 : int = '0', n2 : int = '0'):
    if n1 == '0':
        return (f"{arg11} - {arg12} = {arg11 - arg12}")
    if n2 == '0':
        return (f"{arg11} - {arg12} - {n1} = {arg11 - arg12 - n1}")
    return (f"{arg11} - {arg12} - {n1} - {n2} = {arg11 - arg12 - n1 - n2}")

def square(arg34_1, arg34_2):
    return (f"{arg34_1} ^ {arg34_2} = {arg34_1 ** arg34_2}")

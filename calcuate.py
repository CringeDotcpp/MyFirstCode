import re
from fractions import Fraction

def calc(example, iterations = 10000):
    if(iterations == 0): raise()
    try:
        example = example.replace("\\bullet",'*')
        example = example.replace("\\cdot",'*')
        example = example.replace("\\",'')
        example = example.replace(" ",'')
    except Exception as e: pass
    try: return eval(example)
    except: pass
    # except: print("FUCK\t" + example + "\n"*5)

    sum_pattern = r"sum_{(?P<variable>\w*)=(?P<start>\d*)}\^{(?P<end>\d*)}{(?P<inside>[\w\+\-\*\/]*)}"
    prod_pattern = r'prod_{(?P<variable>\w*)=(?P<start>\d*)}\^{(?P<end>\d*)}{(?P<inside>[\w\+\-\*\/]*)}'
    frac_pattern = r'frac{(?P<v1>[\w\+\-\*]*)}{(?P<v2>[\w\+\-\*\/]*)}'


    
    matches = re.findall(sum_pattern, example)
    for variable, start, end, inside in matches:            
        start = int(start)
        end = int(end)
        sum_result = sum(calc(inside.replace(variable, str(i))) for i in range(start, end + 1))
        example = example.replace(f'sum_{{{variable}={start}}}^{{{end}}}{{{inside}}}', str(sum_result))
            
    
    matches = re.findall(prod_pattern, example)
    for variable, start, end, inside in matches:
        start = int(start)
        end = int(end)
        prod_result = 1
        for i in range(start, end + 1):
            prod_result *= calc(inside.replace(variable, str(i)))
        example = example.replace(f'prod_{{{variable}={start}}}^{{{end}}}{{{inside}}}', str(prod_result))
    
    matches = re.findall(frac_pattern, example)
    for numerator, denominator in matches:
        numerator_value = calc(numerator)
        denominator_value = calc(denominator)
        if denominator_value != 0:
            frac_result = Fraction(numerator_value, denominator_value)
        else:
            frac_result = 'undefined'
        example = example.replace(f'frac{{{numerator}}}{{{denominator}}}', str(frac_result))
    
    
    try: return eval(example)
    except: return calc(example, iterations - 1)
    

if __name__ == '__main__':
    a = '\\frac{\\sum_{i=1}^{6}{i}}{\\prod_{i=1}^{3}{i}}'
    # a="2\\cdot2"
    res = calc(a)
    print(res)
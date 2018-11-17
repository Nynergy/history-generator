'''
    History Generator by Ben Buchanan (2018)
'''

import random
from classes.Figure import Figure

# Generates a name
def GenerateName():
    bits = ['ada', 'aro', 'awi', 'ace', 'axe', 'azi', 'bo', 'buf', 'bir', 'bea', 'cro', 'cu', 'chi', 'cha', 'di', 'dha', 'dok', 'ei', 'edo', 'eta', 'for', 'fea', 'fin', 'gra', 'gub', 'go', 'ghi', 'hai', 'he', 'huz', 'hof', 'ie', 'ian', 'im', 'jul', 'jid', 'jag', 'jhe', 'kor', 'kri', 'kha', 'ku', 'lou', 'lea', 'lim', 'lev', 'min', 'mag', 'muck', 'mei', 'nil', 'nex', 'nar', 'nu', 'or', 'oan', 'ous', 'pre', 'par', 'pel', 'poa', 'piv', 'qu', 'qua', 'qi', 'qo', 're', 'ra', 'ri', 'ro', 'ru', 'rei', 'rum', 'rin', 'rav', 'sol', 'so', 'sar', 'sin', 'son', 'sep', 'sei', 'sen', 'szu', 'to', 'tu', 'tad', 'tea', 'ten', 'tru', 'tri', 'ua', 'uo', 'ui', 'ue', 'var', 'va', 'vop', 'vuh', 'vex', 'vir', 'wa', 'we', 'woa', 'win', 'wha', 'whe', 'who', 'whi', 'whu', 'wu', 'xe', 'xa', 'xi', 'xu', 'xo', 'xhi', 'ya', 'yu', 'yo', 'yi', 'ye', 'za', 'zu', 'zi', 'zo', 'ze', 'zeh', 'zhe', 'zha', 'zhi', 'zho']

    name = ""

    num_parts = random.randrange(2, 4)
    for i in range(num_parts):
        name += random.choice(bits)

    name = name.title()
    
    return name

def main():
    figure = Figure(GenerateName())
    year = random.randrange(100, 1000000)
    print("It is the year " + str(year) + ", and " + figure.name + " is the current ruler of the Kingdom.")

    return

main()

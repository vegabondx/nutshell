# python3 argparse_test.py 12 1 --choices 2 --two-var 2 3 --append 5 --append 9 
# Namespace(append=['5', '9'], choices=2, flag=False, positionalarg=[12, 1], store_const='left', two_var=['2', '3'], variable='defaultvalue')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='<description>')
    parser.add_argument('positionalarg', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
    parser.add_argument('--var', dest='variable', type=str, default="defaultvalue", help='value of a variable')
    parser.add_argument('--two-var', nargs=2, metavar=('VAR1', 'VAR2'), help='2 vars expected: VAR1 VAR2')
    parser.add_argument('--store-const',action='store_const', const="inner", default='left')
    parser.add_argument('--choice',type=int, choices=[0,1,2], help="only few choices are allowed")
    parser.add_argument('--flag', action='store_true', help="stores true else false")
    parser.add_argument('--append',action='append',help="appends values")
    parser.add_argument('--verbose', action='count', default=0,help="counts the number of times its used")
    args = parser.parse_args()
    

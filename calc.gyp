import sys
import math

def calc(term):
    term = term.replace(' ', '')
    term = term.replace('^', '**')
    term = term.replace('=', '')
    term = term.replace('?', '')
    term = term.replace('%', '/100.00')
    term = term.replace('rad', 'radians')
    term = term.replace('mod', '%')
    term = term.replace('aval', 'abs')
    functions = ['sin','cos','tan','pow','sqrt','sinh','cosh','tanh','radians','pi','e']
    term = term.lower()
    for func in functions:
        if func in term:
            withmath = 'math.' + func
            term = term.replace (func , withmath)

    try:
        term = eval(term)
    except ZeroDivisionError:
        print("Can't divide by zero . Please try again :)")
    except NameError:
        print("Invalid input . Please try again :)")
    except AttributeError:
        print("Please check usage method :)")
    except TypeError:
        print("Please enter inputs of correct datatype :)")
    except Exception:
        print("Wrong operator :)")
    return (term)
def result(term):
    print("\n" + str(calc(term)))
def main():
    while True:
        k = input("\nEnter your problem : ")
        if k == 'quit':
            break
        result(k)
    
if __name__ == '__main__':
    main()
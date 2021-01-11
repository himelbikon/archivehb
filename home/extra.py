#from home.forms import VH_Form
import os


def visitor_log(request):
    if not os.path.exists('logs'):
        os.mkdir('logs')
        print('creates new')

    file = open('logs/v_logs.txt', 'a')
    file.write(str(request) + '\n')
    file.close()
    print('------------------------------------------------------------------')

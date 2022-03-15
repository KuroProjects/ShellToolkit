import os

w = open('config.json', 'w+')
w.write('{')
w.write('\n')
w.write('    "authToken": "'+os.getenv('5201469616:AAHJyd_CVabmD8rNWNNW9IbH0jb0cMiZf24')+'",')
w.write('\n')
w.write('    "owner": '+os.getenv('2104912596'))
w.write('\n')
w.write('}')

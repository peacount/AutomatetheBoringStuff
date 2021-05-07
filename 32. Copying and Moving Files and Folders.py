import shutil
shutil.copy('C:\\Users\\jenny\\MyPythonScripts\\spam.txt', 'C:\\delicious\\spam.txt')
shutil.copy('C:\\Users\\jenny\\MyPythonScripts\\spam.txt', 'C:\\delicious\\spamspamspam.txt')

shutil.copytree('C:\\delicious', 'C:\\delicious_backup')

shutil.move('C:\\delicious\\walnut.txt', 'C:\\delicious\\walnut')

shutil.move('C:\\delicious\\walnut\\walnut.txt', 'C:\\delicious\\walnut\\eggs.txt')
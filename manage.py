import os
import sys
from subprocess import call, Popen

### compile parts
def make():
    call(['javac -d bin -sourcepath src src/main/core/ExcelLent.java'], shell=True)
    #call(['javac -d bin -sourcepath src -cp "lib/*" src/com/sample/DroolsTest.java'], shell=True)


### configure parts
def configure():
    print('hello')

### test & analysze parts
def test():
    print('hello')

### doc parts
def doc():
    print('hello')

### run parts
def run():
    os.chdir('bin')
    call(['java main.core.ExcelLent'], shell=True)
    #call(['java -cp "bin:lib/*:." com.sample.DroolsTest'], shell=True)


### clean parts
def clean():
    print('hello')

operations = {
    'make' :        (make, '\t\tcompile the software'),
    'configure':    (configure, '\tconfigure it to adapt it at the architecture'),
    'test':         (test, '\t\trun the unit test and integration test'),
    'doc':          (doc, '\t\tcreate the doc'),
    'run':          (run, '\t\texecute the software'),
    'clean':        (clean, '\t\tclean the project'),
}


if __name__ == "__main__":
    opt = ['make', 'run']
    
    if len(sys.argv) > 1:
        opt = sys.argv[1:]
    
    if 'help' in opt:
        for cmd_name, (stage, help) in operations.items():
            print(cmd_name + ': ' + help)
    else:
        for stage in opt:
            if not stage in operations:
                print('The operation ' + stage + ' doesn\'t exists')
            else:
                current_stage = operations[stage][0]
                current_stage()

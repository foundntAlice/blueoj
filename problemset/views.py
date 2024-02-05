from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Problem
from .forms import CodeSubmissionForm
import subprocess

def problemset(request):
    myproblems = Problem.objects.all().values()
    template = loader.get_template('all_problems.html')
    context = {
        'myproblems': myproblems,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    myproblem = Problem.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myproblem': myproblem,
    }
    return HttpResponse(template.render(context, request))
    
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def isEqual(a, b):
    output = []
    answer = []
    i = 0
    while i < len(a):
        s = ""
        while i < len(a) and a[i] == ' ':
            i += 1
        while i < len(a) and a[i] != ' ':
            s += a[i]
            i += 1
        if len(s):
            output.append(s)

    i = 0
    while i < len(b):
        s = ""
        while i < len(b) and b[i] == ' ':
            i += 1
        while i < len(b) and b[i] != ' ':
            s += b[i]
            i += 1
        if len(s):
            answer.append(s)

    res = True

    if len(output) != len(answer):
        res = False
    
    for i in range(len(output)):
        if output[i] != answer[i]:
            res = False
    return res

def execute_code(problem_id, code):
    my_problem = Problem.objects.get(id=problem_id)
    cpp_file_path = 'blueoj/code_execution/cpp_code.cpp'
    cpp_executable = 'blueoj/code_execution/a.out'
    input_file_path = 'blueoj/code_execution/input.txt'
    output_path = 'blueoj/code_execution/output.txt'
    answer_path = 'blueoj/code_execution/answer.txt'

    #assign test cases to input.txt
    with open(input_file_path, 'w') as input_file:
        input_file.write(my_problem.input_data)

    #assign expected output to answer.txt
    with open(answer_path, 'w') as answer_file:
        answer_file.write(my_problem.expected_output)

    #assign user's code to cpp_file_path
    
    with open(cpp_file_path, 'w') as code_file:
        code_file.write(code)

    compile_command = f'gcc {cpp_file_path} -o {cpp_executable} -lstdc++'
    
    compile_process = subprocess.run(compile_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if compile_process.returncode == 0:
        execution_command = f'{cpp_executable} < {input_file_path} > {output_path}'
        execution_process = subprocess.run(execution_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = ""
        with open(output_path, 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                if line == "\n":
                    continue
                output += line + " "

        answer = ""
        with open(answer_path, 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                if line == "\n":
                    continue
                answer += line + " "

        if isEqual(output, answer):
            res = "Accepted"
        else:
            res = "Wrong answer"
        return HttpResponse(res)
    else:
        error = compile_process.stderr.decode('utf-8')
        return HttpResponse("Compiler error!")

def submit_code(request):
    if request.method == 'POST':
        form = CodeSubmissionForm(request.POST)
        if form.is_valid():
            problem_id = form.cleaned_data['problem_id']
            code = form.cleaned_data['code']
            if not Problem.objects.filter(id=problem_id).exists():
                return HttpResponse("Invalid problem ID!")
            return HttpResponse(execute_code(problem_id, code))
    else:
        form = CodeSubmissionForm()

    return render(request, 'submit_code.html', {'form': form})

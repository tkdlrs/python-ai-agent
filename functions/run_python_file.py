import os
import subprocess
# 
def run_python_file(working_directory, file_path, args=None):
    try:
        #  
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
        # 
        if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        # 
        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        # 
        if not abs_file_path.endswith((".py")):
            return f'Error: "{file_path}" is not a Python file'
        # 
        command = ["python", abs_file_path]
        # 
        if args is not None:
            command.extend(args)
        # 
        output_string = ""
        complete_process = subprocess.run(command, cwd=abs_working_dir, timeout=30, text=True, capture_output=True)
        if complete_process.returncode != 0:
            output_string += f'Process exited with code {complete_process.returncode}'
        if not complete_process.stdout and not complete_process.stderr:
            output_string +=  f'No output produced'
        output_string += f'STDOUT: {complete_process.stdout}'
        output_string += f'STDERR: {complete_process.stderr}'
        # 
        return output_string
        # 
    except Exception as e:
        return f"Error: executing Python file: {e}"

# 
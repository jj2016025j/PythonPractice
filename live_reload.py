from livereload import Server, shell

server = Server()
server.watch('*.py', shell('python file.py', cwd='.'))
server.serve()

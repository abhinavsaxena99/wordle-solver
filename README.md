nginx + guincorn + flask(with jinja2)

solver.service allows controlling the wordle-solver service on the server
For example, "sudo systemctl restart solver"

sites-enabled-solver goes in /etc/nginx/sites-enabled with the name "solver" and then is linked to sites-enabled
using "sudo ln -s /etc/nginx/sites-available/solver /etc/nginx/sites-enabled"

Project built on Python 3.8.10
nginx + guincorn + flask(with jinja2)

solver.service goes in /etc/systemd/system/solver.service
solver.service allows controlling the wordle-solver service on the server
For example, "sudo systemctl restart solver"
To run:
sudo systemctl enable solver
sudo systemctl enable solver
sudo systemctl status solver

sites-enabled-solver goes in /etc/nginx/sites-enabled with the name "solver" and then is linked to sites-enabled
using "sudo ln -s /etc/nginx/sites-available/solver /etc/nginx/sites-enabled"


SSL certs through LetsEncrypt, Certbot (added the lines inside server block in sites-enabled-solver to the certbox server block in sites-enabled/default)

Project built on Python 3.8.10

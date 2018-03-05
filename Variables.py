#Variables
HOST = 'https://10.91.127.194:9182'
PORT = '9182'
USER = 'MSK'
PASS = 'Versa@123'
url = HOST + "/vnms/appliance/appliance?offset=0&limit=3"
task_url = HOST + "/api/operational/tasks/task/"
upgrade_dev_url = HOST + "/api/config/nms/actions/packages/upgrade"
headers = {'Accept': 'application/vnd.yang.data+json'}
headers2 = {'Accept': 'application/vnd.yang.data+json', 'Content-Type': 'application/vnd.yang.data+json'}
headers3 = {'Accept': 'application/json', 'Content-Type': 'application/json'}
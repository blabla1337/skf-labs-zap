import time
import json
from pprint import pprint
from zapv2 import ZAPv2
from urllib.parse import urlparse

proxies = {'http': 'http://localhost:8080', 'https': 'http://localhost:8080'}
zap = ZAPv2(proxies=proxies)


def import_scan_policy(active_scan_policy):
    policy = zap.ascan
    policy.import_scan_policy(active_scan_policy)


def start_zap(target, active_scan_policy_name):
    print(target)
    start_zap = zap.ascan
    scanId = start_zap.scan(
        url = target,
        scanpolicyname = active_scan_policy_name
        )
    print(scanId)
    check_if_scan_is_ready(scanId)


def check_if_scan_is_ready(scanId):
     ready = zap.ascan
     while (int(ready.status(scanId)) < 100):
        print('Active Scan progress: ' + ready.status(scanId) + '%')
        time.sleep(5)


def new_session():
    new_sess = zap.core.new_session
    new_sess("session", True)


def disable_passive_scan():
    zap.pscan.disable_all_scanners()


def enable_passive_scan(passive_scan_id):
    zap.pscan.enable_scanners(passive_scan_id)


def add_custom_alert(messageid, name, riskid, confidenceid, description, solution):
    zap.alert.add_alert(
        messageid = messageid ,
        name = name,
        riskid = riskid,
        confidenceid = confidenceid,
        description = description,
        solution = solution
    )
            

def load_zest_script(script_name, filename, script_type):
    script = zap.script
    script.remove(script_name)
    print(script.load(
        scriptname = script_name, 
        scripttype = script_type,
        scriptengine = "Mozilla Zest",
        filename = filename,
        scriptdescription = "OWASP SKF test automation"
    ))
    #script.enable(scriptname=script_name)

def disable_zest_script(script_name):
    script = zap.script
    script.disable(scriptname=script_name)
    script.remove(script_name)

def run_zest_script(zest_script_name):
    script = zap.script
    print(script.run_stand_alone_script(zest_script_name))

def replace_zest_url(target, zest_script):
    with open(zest_script) as f:
        data = json.load(f)

        for item in data['statements']:
            for key, value in item.items(): 
                if key == "url":
                    path = urlparse(value).path
                    item['url'] = target + path

        with open(zest_script, 'w') as f:
            json.dump(data, f, indent=3)
    
#"/Volumes/OWASP ZAP/OWASP ZAP.app/Contents/Java/zap.sh" \
#-daemon \
#-host 0.0.0.0 \
#-port 8082 \
#-config api.addrs.addr.regex=true \
#-config api.disablekey=true
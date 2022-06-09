from zap_api import *
import argparse
import time

parser = argparse.ArgumentParser(description='Start the OWASP ZAP scanner')
parser.add_argument("-zf", "--zest_script", help="Add location of the zest script you want to use", required=True)
parser.add_argument("-zn", "--zest_script_name", help="Zest script name", required=True)
parser.add_argument("-zt", "--zest_script_type", help="Zest script type", required=True)
parser.add_argument("-hf", "--helper_script", help="Add location of the helper script you want to use", required=False)
parser.add_argument("-hn", "--helper_script_name", help="helper script name", required=False)
parser.add_argument("-ht", "--helper_script_type", help="helper script type", required=False)
parser.add_argument("-ap", "--active_scan_policy", help="Add location of the active scan policy you want to use", required=False)
parser.add_argument("-an", "--active_scan_policy_name", help="Active scan policy name", required=False)
parser.add_argument("-d", "--enable_active_scan", help="Stops the active scan if not necessary", required=False)
parser.add_argument("-e", "--enable_passive_scan", help="Add rule id for passive scanning", required=False)
parser.add_argument("-t", "--target", help="target url", required=True)

def main():
    args = parser.parse_args()
    
    #replace the target url in zest
    #replace_zest_url(args.target, args.zest_script)

    #always run these functions for clean slate
    new_session()
    disable_passive_scan()

    #Some labs require some header manipulation, so we can also include a proxy/httpsender/etc script to do that
    if args.helper_script_name:
        load_zest_script(script_name=args.helper_script_name, filename=args.helper_script, script_type=args.helper_script_type)    

    #ZEST is the backbone for each scan so we always run ZEST (here ZAP learns target + endpoints)
    load_zest_script(script_name=args.zest_script_name, filename=args.zest_script, script_type=args.zest_script_type)
    run_zest_script(args.zest_script_name)
    
    #A subset of labs requires passive scans
    if args.enable_passive_scan:
        enable_passive_scan(args.enable_passive_scan)
        print("Passive scan enabled")

    #A subset of labs requires active scans
    if args.enable_active_scan:
        import_scan_policy(args.active_scan_policy)
        start_zap(args.target, args.active_scan_policy_name)

    if args.helper_script_name:
        disable_zest_script(args.helper_script_name)
        
if __name__ == "__main__":
    main()
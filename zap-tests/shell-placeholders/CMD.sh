python3 runners/QA.py



docker run -v $(pwd):/home/zap:rw -t owasp/zap2docker-stable /home/zap/QA.py \
--zest_script "/Users/riccardo.tencate/Desktop/skf-labs-zap/zap-tests/zest/CMD.zst"  \
--zest_script_name "CMD" \
--zest_script_type "standalone" \
--enable_active_scan "True" \
--active_scan_policy "/Users/riccardo.tencate/Desktop/skf-labs-zap/zap-tests/policies/OS-COMMAND-INJECTION.policy" \
--active_scan_policy_name "OS-COMMAND-INJECTION" \
--target "http://192.168.68.133:5000"
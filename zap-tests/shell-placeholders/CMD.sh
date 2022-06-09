python3 runners/QA.py \
--zest_script "/Users/riccardotencate/Desktop/zap-tests/zest/CMD.zst"  \
--zest_script_name "CMD" \
--zest_script_type "standalone" \
--enable_active_scan "True" \
--active_scan_policy "/Users/riccardotencate/Desktop/zap-tests/policies/OS-COMMAND-INJECTION.policy" \
--active_scan_policy_name "OS-COMMAND-INJECTION" \
--target "http://localhost:4444"
python3 runners/QA.py \
--zest_script "/Users/riccardotencate/Desktop/zap-tests/zest/Auth-bypass-simple.zst"  \
--zest_script_name "Auth-bypass-simple" \
--zest_script_type "standalone" \
--helper_script "/Users/riccardotencate/Desktop/zap-tests/zest/helpers/Auth-bypass-simple-http-intercept.zst" \
--helper_script_name "Auth-bypass-simple-http-intercept" \
--helper_script_type "proxy" \
--target "https://localhost:4444"
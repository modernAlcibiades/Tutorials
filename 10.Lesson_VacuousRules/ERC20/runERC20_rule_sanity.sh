solc-select use 0.8.0

certoraRun ${1}:ERC20 --verify ERC20:Sanity.spec \
--optimistic_loop \
--send_only \
--rule_sanity \
--msg "$2"
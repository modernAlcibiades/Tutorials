solc-select use 0.7.6

certoraRun BankFixed.sol:Bank --verify Bank:invariant.spec \
--rule totalFunds_GE_to_sum_of_all_funds \
--msg "$1" \
--send_only
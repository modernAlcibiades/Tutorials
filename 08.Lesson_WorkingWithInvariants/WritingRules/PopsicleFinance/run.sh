solc-select use 0.8.4

certoraRun popsicle.sol:PopsicleFinance \
--verify PopsicleFinance:popsicle.spec \
--send_only \
--loop_iter 2 \
--msg "$1"
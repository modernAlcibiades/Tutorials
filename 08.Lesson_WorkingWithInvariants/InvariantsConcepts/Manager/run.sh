solc-select use 0.8.6

certoraRun ${1}:Manager \
--verify Manager:ManagerFullSolution.spec \
--send_only \
--msg "$2"
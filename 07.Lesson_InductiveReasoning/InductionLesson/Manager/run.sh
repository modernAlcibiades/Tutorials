
solc-select use 0.8.6

certoraRun ${1}:Manager --verify Manager:ManagerPartialSolution.spec \
--send_only \
--msg "$2"
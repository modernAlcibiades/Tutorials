
solc-select use 0.8.6

certoraRun ${1}:Manager --verify Manager:Manager.spec \
--send_only \
--msg "$2"
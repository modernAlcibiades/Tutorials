solc-select use 0.8.6

certoraRun BallGame.sol:BallGame --verify BallGame:BallGameSolution.spec \
  --send_only \
  --msg "$1"

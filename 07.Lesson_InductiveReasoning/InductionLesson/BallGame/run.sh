<<<<<<< HEAD
solc-select use 0.8.6

certoraRun BallGame.sol:BallGame --verify BallGame:BallGameSolution.spec \
  --send_only \
  --msg "$1"
=======
certoraRun BallGame.sol:BallGame --verify BallGame:BallGame.spec \
--solc solc8.6 \
--msg "$1"
>>>>>>> 3123ecc684f78b8f81e31ab81e256d9c4690a337

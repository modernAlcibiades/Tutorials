solc-select use 0.7.0

certoraRun ../BankLesson1/Bank.sol:Bank \
    --verify Bank:../BankLesson1/Parametric.spec \
    --rule validityOfTotalFundsWithVars \
    --msg "Do not output to terminal" \
    --send_only
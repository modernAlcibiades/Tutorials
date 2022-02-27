solc-select use 0.8.7

certoraRun ../../04.Lesson_Declarations/Methods_Definitions_Functions/MeetingScheduler/MeetingSchedulerFixed.sol:MeetingScheduler \
    --verify MeetingScheduler:../../04.Lesson_Declarations/Methods_Definitions_Functions/MeetingScheduler/meetings.spec \
    --msg "05 Exercise 01 : meetings" \
    --send_only

certoraRun ../../04.Lesson_Declarations/Methods_Definitions_Functions/ERC20/ERC20Fixed.sol:ERC20 \
    --verify ERC20:../../04.Lesson_Declarations/Methods_Definitions_Functions/ERC20/ERC20.spec \
    --msg "05 Exercise 01: ERC20" \
    --send_only

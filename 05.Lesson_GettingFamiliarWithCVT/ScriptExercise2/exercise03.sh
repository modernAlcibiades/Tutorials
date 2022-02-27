solc-select use 0.8.7

certoraRun ../../04.Lesson_Declarations/Methods_Definitions_Functions/MeetingScheduler/MeetingSchedulerFixed.sol:MeetingScheduler \
    --verify MeetingScheduler:../../04.Lesson_Declarations/Methods_Definitions_Functions/MeetingScheduler/meetings.spec \
    --rule startOnTime \
    --msg "05 Exercise 04 : Same parametric rule" \
    --send_only

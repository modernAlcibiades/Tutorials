solc-select use 0.8.7

certoraRun ../../04.Lesson_Declarations/Methods_Definitions_Functions/MeetingScheduler/MeetingSchedulerFixed.sol:MeetingScheduler \
    --verify MeetingScheduler:../../04.Lesson_Declarations/Methods_Definitions_Functions/MeetingScheduler/meetings.spec \
    --rule startOnTime --method "startMeeting(uint256)" \
    --msg "05 Exercise 03 : Parametric rule on startMeeting Method" \
    --send_only

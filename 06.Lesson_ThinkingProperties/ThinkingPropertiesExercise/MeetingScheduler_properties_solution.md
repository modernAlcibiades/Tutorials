## Meeting Scheduler Properties

- Valid States : As defined in MeetingStatus
```
    UNINITIALIZED - Meeting doesn't exist, variables 0 values
    PENDING - Meeting has been scheduled, variables set
    STARTED - Meeting started, can be joined
    ENDED - Meeting has ended, no other changes can be made
    CANCELLED - A pending meeting was not started, instead cancelled
```
- State transitions 
  - (high) `UNINITIALIZED` : on `scheduleMeeting(id, start_time, end_time)` => `PENDING`
  - (high) `PENDING` : on `cancelMeeting(id)` => `CANCELLED`
  - (high) `PENDING` : on `startMeeting(id) && startTime < now` => `STARTED`
  - (high) `STARTED` : on `joinMeeting(id)` => `numOfParticipents++`
  - (high) `STARTED` : on `endMeeting(id) && endTime < now` => `ENDED`
  - (high) No state transitions from `CANCELLED` and `ENDED` 

- Variable transitions
  - (high) MeetingStatus should match corresponding state in the State machine
  - (low) `numOfParticipents` can only change when `STARTED`
  - (medium) `numOfParticipents` can not decrease
  
- High-level properties
  - (low) Ideally `organizer` should trigger state changes
  - (high) Meeting shouldn't start after `endTime`
  - (high) Meeting shouldn't end before `endTime`
  - (high) Same id shouldn't be used for different meetings ie `scheduleMeeting` should check for existing meetings
  - (low) Same address shouldn't be joining the meeting more than once

- Unit tests
  - (high) `startTime < endTime` for all meetings
  - (medium) `numOfParticipants < MAX_UINT256`
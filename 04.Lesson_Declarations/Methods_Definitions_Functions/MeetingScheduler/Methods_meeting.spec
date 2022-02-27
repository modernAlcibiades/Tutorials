methods {
    getStateById(uint256) returns uint8 envfree
    getStartTimeById(uint256) returns uint256 envfree
    getEndTimeById(uint256) returns uint256 envfree
    getNumOfParticipents(uint256) returns uint256 envfree
    getOrganizer(uint256) returns address envfree
    scheduleMeeting(uint256, uint256, uint256)
    startMeeting(uint256) 
    cancelMeeting(uint256)
    endMeeting(uint256)
    joinMeeting(uint256)
}
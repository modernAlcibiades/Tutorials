methods {
       // Gets the number of points a specified contender has
    getPointsOfContender(address) returns(uint256) envfree

    // Gets a boolean indicating whether a voter has voted
    hasVoted(address) returns(bool) envfree

    // Gets the winner at this point of time, and the number of points they have
    getWinner() returns(address, uint256) envfree

    // Gets the full details of a specified voter
    getFullVoterDetails(address) returns(uint8, bool, bool, uint256, bool) envfree
    
    // Gets the full details of a specified contender
    getFullContenderDetails(address) returns(uint8, bool, uint256) envfree

    // Registers a voter so they could cast a vote
    registerVoter(uint8 ) returns (bool)

    // Registers a contender so they could receive votes
    registerContender(uint8) returns (bool)

    /**
    * @dev sends the voting choices of the sender and updates their points accordingly.
    */
    vote(address, address, address) returns(bool)

}
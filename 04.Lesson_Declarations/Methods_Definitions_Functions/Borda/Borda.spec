

function getVoterAge(env e, address voter) returns uint8{
    uint8 age;
    age, _, _, _, _ = getFullVoterDetails(e, voter);
    return age;
}

function getVoterRegistered(env e, address voter) returns bool{
    bool registered;
    _, registered, _, _, _ = getFullVoterDetails(e, voter);
    return registered;
}

function getVoterVoted(env e, address voter) returns bool{
    bool voted;
    _, _, voted, _, _ = getFullVoterDetails(e, voter);
    return voted;
}

function getVoterVoteAttempts(env e, address voter) returns uint256{
    uint256 vote_attempts;
    _, _, _, _, _ = getFullVoterDetails(e, voter);
    return vote_attempts;
}

function getVoterBlocked(env e, address voter) returns bool{
    bool blocked;
    _, _, _, _, blocked = getFullVoterDetails(e, voter);
    return blocked;
}

// Checks that a voter's "registered" mark is changed correctly - 
// If it's false after a call, it was false before
// If it's true after a call, it either started as true or changed from false to true via registerVoter()
rule registeredCannotChangeOnceSet(method f, address voter){
    env e; calldataarg args;
    bool voterRegBefore = getVoterRegistered(e, voter);
    f(e, args);
    bool voterRegAfter = getVoterRegistered(e, voter);

    assert (!voterRegAfter => !voterRegBefore, "voter changed state from registered to not registered after a call");
    assert (voterRegAfter => 
        ((!voterRegBefore && f.selector == registerVoter(uint8).selector) || voterRegBefore), 
            "voter was registered from an unregistered state, by other then registerVoter()");
}

// Checks that each voted contender receieves the correct amount of points after each vote
rule correctPointsIncreaseToContenders(address first, address second, address third){
    env e;
    uint256 firstPointsBefore = getPointsOfContender(e, first);
    uint256 secondPointsBefore = getPointsOfContender(e, second);
    uint256 thirdPointsBefore = getPointsOfContender(e, third);

    vote(e, first, second, third);
    uint256 firstPointsAfter = getPointsOfContender(e, first);
    uint256 secondPointsAfter = getPointsOfContender(e, second);
    uint256 thirdPointsAfter = getPointsOfContender(e, third);
    
    assert (firstPointsAfter - firstPointsBefore == 3, "first choice receieved other amount than 3 points");
    assert (secondPointsAfter - secondPointsBefore == 2, "second choice receieved other amount than 2 points");
    assert ( thirdPointsAfter- thirdPointsBefore == 1, "third choice receieved other amount than 1 points");

}

// Checks that a blocked voter cannot get unlisted
rule onceBlockedNotOut(method f, address voter){
    env e; calldataarg args;
    bool registeredBefore = getVoterRegistered(e, voter);
    bool blocked_before = getVoterBlocked(e, voter);
    require blocked_before => registeredBefore;
    f(e, args);

    bool blocked_after = getVoterBlocked(e, voter);
    
    assert blocked_before => blocked_after, "the specified user got out of the blocked users' list";
}

// Checks that a contender's point count is non-decreasing
rule contendersPointsNondecreasing(method f, address contender){
    env e; calldataarg args;
    uint8 age; bool registeredBefore; uint256 pointsBefore;
    age, registeredBefore, pointsBefore = getFullContenderDetails(e, contender);
    require pointsBefore > 0 => registeredBefore; 
    f(e,args);
    bool registeredAfter; uint256 pointsAfter;
    age, registeredAfter, pointsAfter = getFullContenderDetails(e, contender);

    assert (pointsAfter >= pointsBefore);
}



methods{
    getFullVoterDetails(address) returns (uint8, bool, bool, uint256, bool) envfree
    getFullContenderDetails(address) returns (uint8, bool, uint256) envfree
    getPointsOfContender(address) returns (uint256) envfree
    getWinner() returns (address, uint256) envfree
    registerVoter(uint8) returns bool
}

function getVoterAge(address voter) returns uint8{
   uint8 age; bool voterReg; bool voted; uint256 vote_attempts; bool blocked;
    age, voterReg, voted, vote_attempts, blocked = getFullVoterDetails(voter);
    return age;
}

function getVoterRegistered(address voter) returns bool{
    uint8 age; bool voterReg; bool voted; uint256 vote_attempts; bool blocked;
    age, voterReg, voted, vote_attempts, blocked = getFullVoterDetails(voter);
    return voterReg;
}

function getVoterVoted(address voter) returns bool{
   uint8 age; bool voterReg; bool voted; uint256 vote_attempts; bool blocked;
    age, voterReg, voted, vote_attempts, blocked = getFullVoterDetails(voter);
    return voted;
}

function getVoterVoteAttempts(address voter) returns uint256{
   uint8 age; bool voterReg; bool voted; uint256 vote_attempts; bool blocked;
    age, voterReg, voted, vote_attempts, blocked = getFullVoterDetails(voter);
    return vote_attempts;
}

function getVoterBlocked(address voter) returns bool{
   uint8 age; bool voterReg; bool voted; uint256 vote_attempts; bool blocked;
    age, voterReg, voted, vote_attempts, blocked = getFullVoterDetails(voter);
    return blocked;
}

// ghost count_voter_registered(address) returns uint256 {
//     init_state assuming forall address user. count_voter_registered(user) == 0;
// }

// invariant voterRegisterOnlyOnce(address voter)
//     count_voter_registered(voter) <= 1
//     {
//         preserved 
//     }


rule cannotChangeOnceRegistered(address voter, method f){
    require(getVoterRegistered(voter));
    env e;
    calldataarg args;
    f(e, args);
    assert (getVoterRegistered(voter));
}

rule cannotChangeOnceBlocked(address voter, method f){
    require(getVoterBlocked(voter));
    env e;
    calldataarg args;
    f(e, args);
    assert (getVoterBlocked(voter) || f.selector == registerVoter(uint8).selector);
}

rule cannotChangeOnceVoted(address voter, method f){
    require(getVoterVoted(voter));
    env e;
    calldataarg args;
    f(e, args);
    assert (getVoterVoted(voter) || f.selector == registerVoter(uint8).selector);
}

rule voteAttemptsCannotDecrease(address voter, method f){
    uint256 attemptsBefore = getVoterVoteAttempts(voter);
    env e;
    calldataarg args;
    f(e, args);
    assert (getVoterVoteAttempts(voter) >= attemptsBefore || f.selector == registerVoter(uint8).selector);
}

ghost points_of_contender(address) returns uint256 {
    init_state axiom forall address user. points_of_contender(user) == 0;
}

// hook Sstore _contenders[KEY address con] uint256 new_points 
// (uint256 old_points) STORAGE {
//     havoc points_of_contender assuming points_of_contender(con) == new_points.;
// }

function getWinnerPoints() returns uint256{
    address winner; uint256 points;
    winner, points = getWinner();
    //assert(points_of_contender(winner) == points);
    return points;
}

invariant winnerHasMostVotes(address contender)
    getPointsOfContender(contender) <= getWinnerPoints()


// invariant winnerHasMostVotes(address contender)
//     points_of_contender(contender) <= getWinnerPoints()
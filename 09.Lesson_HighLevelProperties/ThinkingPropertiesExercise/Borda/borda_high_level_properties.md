## Borda Election Properties
- Valid States
  - Voter States
    - Uninitialized : Not registered yet
    - NotVoted : Registered but hasn't voted
    - Voted : Valid voter who voted already
    - Blacklisted : Voter who attempted to vote too many times or broke other rules
  - Winner States
    - Not Started : (0x0, 0) - No votes yet
    - Leader : Address_i, points_i - At present, has the maximum votes

- State Transitions
  - Voter States
    - `Uninitialized` : on `registerVoter` => `NotVoted`
    - `NotVoted` : if `hasVoted` ie on valid vote => `Voted`
    - `NotVoted` or `Voted` : too many vote_attempts => `Blacklisted`
  - Contender States
    - `Not Started` : 0x0
    - `Address_i, points_i`: on `voteTo(Address_j, points)` && `points_i < points_j` => `Address_j, points_j`

- Variable Transitions
  - `pointsOfWinner` should increase monotonically
  - `vote_attempts` should increase monotonically
  - `black_listed`, `voted`, `registered` cannot be altered once set to  `true`
  
  
- High-level properties
  - One address, one vote
  - Vote cannot be changed
  - Blacklisted voters shouldn't be able to vote
  - Only registered Contenders and registered Voters should be able to participate in their respective roles
  - Winner should have the most number of votes. If there is are multiple contenders with same amount of votes, first one to achieve that amount of votes should be the winner.
  - Each unique voter should have a unique id, and each id should correspond to a different (unique) voter
  - Each unique contender should have a unique id, and each id should correspond to a different (unique) contender.

- Unit Tests
  - for all addresses a, `pointsOfWinner >= _contenders[a].points`
  
  
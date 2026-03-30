// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleVoting {

    mapping(string => uint256) votes;
    string lastCandidate;
    uint256 lastVoteCount;

    function vote(string memory _candidate) public {
        votes[_candidate] += 1;
        lastCandidate = _candidate;
        lastVoteCount = votes[_candidate];
    }

    function getVotes(string memory _candidate) public view returns (uint256) {
        return votes[_candidate];
    }

    function checkLastVote() public view returns (string memory, uint256) {
        return (lastCandidate, lastVoteCount);
    }
}

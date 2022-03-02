methods {
    ticketDepot(uint64)
    createEvent(uint64, uint16) returns uint16
    buyNewTicket(uint16, address) returns uint16
    offerTicket(uint16, uint16, uint64, address, uint16)
    buyOfferedTicket(uint16, uint16, address)
    getNumEvents() returns uint16 envfree
    getTicketsRemaining(uint16) returns uint16 envfree
    getTicketAttendee(uint16, uint16) returns address envfree
    getDeadline(uint16 eid, uint16 tid) returns uint256 envfree
}

rule eventsNotDeleted(uint16 eid, method f){
    require eid < getNumEvents();
    env e;
    calldataarg args;
    f(e, args);
    assert eid < getNumEvents(), "Id cannot be more than number of events";
}

rule nonIncreasingTickets(uint16 eid, method f){
    require eid < getNumEvents();
    uint16 ticketsBefore = getTicketsRemaining(eid);
    env e;
    calldataarg args;
    f(e, args);
    uint16 ticketsAfter = getTicketsRemaining(eid);
    assert f.selector != createEvent(uint64, uint16).selector => ticketsBefore >= ticketsAfter, "Number of tickets increased";
}

rule sellerIsAttendee(uint16 eid, uint16 tid, method f){
    env e;
    uint256 old_deadline = getDeadline(eid, tid);
    calldataarg args;
    offerTicket(e, args);
    uint256 new_deadline = getDeadline(eid, tid);
    assert new_deadline != old_deadline => e.msg.sender == getTicketAttendee(eid, tid), "Seller is not ticket owner";
}

rule buyerIsAttendee(uint16 eid, uint16 tid, address new_attendee, method f){
    env e;
    require e.block.number > 0;
    uint256 old_deadline = getDeadline(eid, tid);
    buyOfferedTicket(e, eid, tid, new_attendee);
    uint256 new_deadline = getDeadline(eid, tid);
    assert(old_deadline != 0 && new_deadline == 0) => getTicketAttendee(eid, tid) == new_attendee, "Buyer is not valid";
}

// invariant eventIdLTnumEvents(uint16 eid)
//     eid < getNumEvents()

invariant uniqueAttendee(uint16 eid, uint16 tid1, uint16 tid2)
    getTicketAttendee(eid, tid1) != getTicketAttendee(eid, tid2) && eid < getNumEvents() => tid1 != tid2

methods {
    ticketDepot(uint64)
    createEvent(uint64, uint64) returns uint16
    buyNewTicket(uint16, address) returns uint16
    offerTicket(uint16, uint16, uint64, address, uint16)
    buyOfferedTicket(uint16, uint16, address)
    getNumEvents() returns uint16 envfree
    getTicketsRemaining(uint16) returns uint16 envfree
    getTicketId(uint16, address) return uint16 envfree
}

rule eventsNotDeleted(uint16 eid, method f){
    require eid < getNumEvents();
    env e;
    calldata args;
    f(e, args)
    assert eid < getNumEvents(), "Id cannot be more than number of events"
}

rule nonIncreasingTickets(uint16 eid, method f){
    require eid < getNumEvents();
    uint16 ticketsBefore = getTicketsRemaining(eid);
    env e;
    calldata args;
    f(e, args)
    uint16 ticketsAfter = getTicketsRemaining(eid);
    assert f.method.selector != "createEvent(uint64, uint16)" => ticketsBefore >= ticketsAfter, "Number of tickets increased"
}

invariant uniqueAttendee(uint16 eid, address user1, address user2)
    (user1 != user2 && eid < getNumEvents()) => getTicketId(eid, user1) != getTicketId(eid, user2)

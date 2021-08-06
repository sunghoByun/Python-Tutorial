from collections import deque

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
visitedCity = []

def dfs(tickets, start):
    newTickets = tickets

    for ticket in newTickets:
        if start == ticket[0]:
            newTickets.remove(ticket)
            dfs(newTickets, ticket[1])

# def solution(tickets):
#     queue = deque()
#     answer = []
#     tickets.sort()
#     answer.append("ICN")
#
#     for ticket in tickets:
#         if ticket[0] == "ICN":
#             queue.append(ticket)
#             answer.append(ticket[1])
#             tickets.remove(ticket)
#             break
#
#     while queue:
#         fromTicket, toTicket = queue.popleft()
#
#         for ticket in tickets:
#             if ticket[0] == toTicket:
#                 queue.append(ticket)
#                 answer.append(ticket[1])
#                 tickets.remove(ticket)
#                 break
#
#     return answer

print(solution(tickets))
import heapq


class SeatManager:
    def __init__(self, n: int):
        self.places = [place for place in range(1, n + 1)]

    def reserve(self) -> int:
        return heapq.heappop(self.places)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.places, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

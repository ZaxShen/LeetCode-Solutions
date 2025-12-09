class StockSpanner:

    def __init__(self):
        self.mono_stack = [] # price, span

    def next(self, price: int) -> int:
        mono_stack = self.mono_stack
        span = 1
        while mono_stack and mono_stack[-1][0] <= price:
            span += mono_stack.pop()[1]
        mono_stack.append([price, span])

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
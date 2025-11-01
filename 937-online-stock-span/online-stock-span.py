class StockSpanner:

    def __init__(self):
        self.mono_stack = []  # (price, span)

    def next(self, price: int) -> int:
        span = 1
        mono_stack = self.mono_stack

        while mono_stack and mono_stack[-1][0] <= price:
            span += mono_stack[-1][-1]
            mono_stack.pop()
        mono_stack.append((price, span))

        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
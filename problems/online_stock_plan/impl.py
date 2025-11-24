import numpy as np
class StockSpanner_naive:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        self.arr.append(price)

        span = 0
        for num_i in range(len(self.arr)-1, -1, -1):
            if price >= self.arr[num_i]:
                span += 1
            else:
                return span
        
        return span

class StockSpanner_slighltly_less_naive:

    def __init__(self):
        # The idea is we keep track of the highest stockprice
        # its span and all of the stockprices after that until our last entry
        # We also keep track of the span of the last entry
        self.arr_highest = []
        self.span_highest = 0
        self.span_last = 0
        

    def next(self, price: int) -> int:
        part_of_span_n = len(self.arr_highest)
        if part_of_span_n == 0:
            self.arr_highest = [price]
            self.span_highest = 1
            return 1
        if price >= self.arr_highest[0]:
            self.arr_highest = [price]
            # so we have a new highest stock price
            # in the span of this new ATH we have:
            # all the elements of the old ATH
            # all the elements that came after the ATH
            # 1 for the element we added itself
            self.span_highest = self.span_highest + part_of_span_n
            return self.span_highest
        else:
            self.arr_highest.append(price)
            span_val = 0
            for price_idx in range(len(self.arr_highest)-1, -1, -1):         
                if self.arr_highest[price_idx] <= price:
                    span_val += 1
                else:
                    return span_val
            
            return span_val

class StockSpanner_ugly:

    def __init__(self):
        # Stock tuples keeps track of pairs [price, span] of the peaks we encounter
        self.arr_stock_tuples = []
        

    def next(self, price: int) -> int:
        part_of_span_n = len(self.arr_stock_tuples)
        if part_of_span_n == 0:
            self.arr_stock_tuples.append([price, 1])
            return self.arr_stock_tuples[-1][1]
        
        if price >= self.arr_stock_tuples[-1][0]:
            new_span = 1
            while len(self.arr_stock_tuples) > 0 and price >= self.arr_stock_tuples[-1][0]:
                [old_price, old_span] = self.arr_stock_tuples.pop()
                new_span += old_span
                
            self.arr_stock_tuples.append([price, new_span])
            return self.arr_stock_tuples[-1][1]
        else:
            self.arr_stock_tuples.append([price, 1])
            for price_idx in range(part_of_span_n - 1, -1, -1):         
                if self.arr_stock_tuples[price_idx][0] <= price:
                    self.arr_stock_tuples[-1][1] += self.arr_stock_tuples[price_idx][1] 
                else:
                    return self.arr_stock_tuples[-1][1]
            
            return self.arr_stock_tuples[-1][1]

class StockSpanner_opt:

    def __init__(self):
        # Stock tuples keeps track of pairs [price, span] of the peaks we encounter
        self.stack = []
        

    def next(self, price: int) -> int:
        span = 1
        stack = self.stack

        while stack and price >= stack[-1][0]:
            span += stack.pop()[1]
        
        stack.append([price, span])
        return span

def class_to_solve(class_name: type, stock_prices: list[list[int]]) -> int:
    for i in range(len(stock_prices)):
        if i == 0:
            obj = class_name()
        else:
            param_1 = obj.next(stock_prices[i])
    return param_1

def stsp_opt_solve(stock_prices: list[list[int]]) -> int:
    return class_to_solve(StockSpanner_opt, stock_prices)

def stsp_ugly_solve(stock_prices: list[list[int]]) -> int:
    return class_to_solve(StockSpanner_ugly, stock_prices)

def stsp_subopt_solve(stock_prices: list[list[int]]) -> int:
    return class_to_solve(StockSpanner_slighltly_less_naive, stock_prices)

def stsp_naive_solve(stock_prices: list[list[int]]) -> int:
    return class_to_solve(StockSpanner_naive, stock_prices)

SOLUTIONS = {
    "spanner_optimal": stsp_opt_solve,
    "spanner_ugly": stsp_ugly_solve,
    "spanner_suboptimal": stsp_subopt_solve,
    "spanner_naive": stsp_naive_solve,
}
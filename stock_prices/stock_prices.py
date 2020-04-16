#!/usr/bin/python

import argparse

def find_max_profit(prices):
  for i in range(0, len(prices)-1):
    cur_index = i
    lo = cur_index
    hi = cur_index
    for j in range(0, len(prices)-1):
      if prices[j] < prices[lo]:
        lo = j
    for k in range(lo, len(prices)):
      if prices[k] > prices[hi]:
        hi = k
      if prices[k] == prices[lo]:
        hi = k+1
      profit = prices[hi] - prices[lo]
  print(f"cur_index: {cur_index}, hi: {hi}, lo: {lo}, profit: {profit} ")
  return profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))